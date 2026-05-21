"""
Migrate resource catalogue data from Profile v5 to Profile v6.

This script processes a directory of JSON resource files exported from a v5
catalogue instance and transforms them in place to conform to the v6 schema.

Transformations applied:
  - Normalises resource statuses (approved/rejected/pending)
  - Removes deprecated fields (migrationStatus, transferContactInformation, resourceExtras)
  - Moves catalogueId from the resource payload to the bundle level
  - Replaces the node field with nodePID on every resource
  - Updates resource IDs and cross-references using the prefix mapping in resource_type_mapping
  - Applies resource-type-specific field renames, additions, and removals (see migrate())
  - Renames folders: deployable_service -> deployable_application, provider -> organisation
  - Deletes folders that are no longer part of v6 (see deleteFolders)
  - Removes schema.json files from all remaining folders
  - Reports duplicate IDs detected after migration

Expected input directory structure:
  <path>/
    adapter/
    configuration_template/
    configuration_template_instance/
    datasource/
    deployable_service/
    interoperability_record/
    provider/
    resource_interoperability_record/
    service/
    training_resource/

Before running, review and adjust the following variables at the top of this
file to match your environment:
  - resource_type_mapping  : old-to-new ID prefix mapping
  - contact                : default creator / main-contact used for all resources
  - publishingDate         : set inside each resource-type block (search "2026-03-15")
  - publicContacts         : placeholder email used for all resources

Safety:
  Before any changes are made, the script automatically creates a timestamped
  backup of the input directory at <path>_backup_YYYYMMDD_HHMMSS/.
  Use --dry-run to preview all changes without writing anything.

Usage:
  python migrate_v5_to_v6.py -p <path> -c <catalogue_id> -n <node_pid> [--dry-run]

Examples:
  python migrate_v5_to_v6.py -p /data/export -c eosc -n 21.15999/node1
  python migrate_v5_to_v6.py -p /data/export -c eosc -n 21.15999/node1 --dry-run
"""
import argparse
import json
import os
import shutil
from datetime import datetime, UTC

migrationFolders = [
    'adapter',
    'configuration_template',
    'configuration_template_instance',
    'datasource',
    'deployable_service',
    'interoperability_record',
    'provider',
    'resource_interoperability_record',
    'service',
    'training_resource'
]

deleteFolders = [
    'draft_provider',
    'draft_service',
    'draft_training_resource',
    'draft_interoperability_record',
    'helpdesk',
    'monitoring',
    'vocabulary_curation',
    'catalogue',
    'model',
    'vocabulary',
    'ui_field_display',
    'ui_field_form'
]

# Maps each resource ID prefix used in v5 to its replacement in v6.
# The left-hand side is the prefix that appears before the '/' in existing IDs.
# The right-hand side is the prefix that will be written into the migrated files.
# If a prefix has not changed between versions, keep both sides identical.
#
# Example — if datasource IDs changed from "dat/ds-001" to "21.15136/ds-001":
#   'dat': '21.15136'
# Example — if service IDs stayed the same ("21.15132/svc-001" -> "21.15132/svc-001"):
#   '21.15132': '21.15132'
#
# IMPORTANT: review every entry below and update any prefix that differs in your v6 instance.
resource_type_mapping = {
    '21.15133': '21.15133',  # adapter
    'dat': '21.15136',       # datasource
    '21.11176': '21.11176',  # deployable application (ex deployable service)
    '21.11175': '21.11175',  # interoperability record / guideline
    '21.11174': '21.11174',  # organisation (ex provider)
    '21.15132': '21.15132',  # service
    '21.15134': '21.15134',  # training resource
    'con': 'con',            # configuration template
    'cti': 'cti',            # configuration template instance
    'rir': 'rir',            # resource interoperability record
}

type_mapping = {
    'service': 'Service',
    'datasource': 'DataSource',
    'catalogue': 'Catalogue',
    'adapter': 'Adapter',
    'interoperabilityRecord': 'InteroperabilityGuidelines',
    'trainingResource': 'TrainingMaterial',
    'deployableService': 'DeployableApplication'
}

creator_list = ['adapter', 'interoperabilityRecord', 'deployableService', 'trainingResource']
main_contact_list = ['provider', 'service', 'datasource', 'catalogue']
contact = {
    "email": "default@mail.com",
    "firstName": "name",
    "lastName": "lastname"
}

folder_renames = {
    "deployable_service": "deployable_application",
    "provider": "organisation"
}

all_ids = []
adapter_ids_needing_owner = []


######################################################## GLOBALS #######################################################

##################################################### FUNCTIONS ########################################################
def build_service_owner_map(directory):
    service_owner_map = {}
    service_folder = os.path.join(directory, 'service')
    if not os.path.exists(service_folder):
        return service_owner_map
    for file in os.listdir(service_folder):
        if file.endswith('.json') and file != 'schema.json':
            file_path = os.path.join(service_folder, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
                payload_data = json.loads(json_data['payload'])
                service = payload_data.get('service', {})
                service_id = service.get('id')
                resource_organisation = service.get('resourceOrganisation')
                if service_id and resource_organisation:
                    service_owner_map[service_id] = resource_organisation
    return service_owner_map


def backup_directory(base_path):
    timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")
    backup_path = f"{base_path}_backup_{timestamp}"
    shutil.copytree(base_path, backup_path)
    print(f"Backup created at: {backup_path}")


def folder_selection(directory, default_catalogue, node, service_owner_map, dry_run=False):
    for migrationFolder in migrationFolders:
        folder_path = os.path.join(directory, migrationFolder)
        for file in os.listdir(folder_path):
            if file.endswith('.json') and file != 'schema.json':
                file_path = os.path.join(folder_path, file)
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    json_data = migrate(json_file, migrationFolder, default_catalogue, node, service_owner_map)
                if dry_run:
                    print(f"[DRY RUN] Would migrate: {migrationFolder}/{file}")
                else:
                    with open(file_path, 'w', encoding='utf-8') as json_file:
                        json.dump(json_data, json_file, indent=2, ensure_ascii=False)


def migrate(json_file, resource_type, default_catalogue, node, service_owner_map):
    internal_item = determine_internal_item(resource_type)
    json_data = json.load(json_file)
    payload_str = json_data['payload']
    payload_data = json.loads(payload_str)
    resource = payload_data.get(internal_item)

    # update status
    status = payload_data.get('status')
    if status:
        if status.startswith('approved'):
            payload_data['status'] = 'approved'
        elif status.startswith('rejected'):
            payload_data['status'] = 'rejected'
        elif status.startswith('pending'):
            payload_data['status'] = 'pending'

    # remove old/deprecated fields
    payload_data.pop('migrationStatus', None)
    payload_data.pop('transferContactInformation', None)
    payload_data.pop('resourceExtras', None)

    # move catalogueId to bundle
    catalogue_id = resource.pop('catalogueId', None)
    if catalogue_id:
        if catalogue_id == default_catalogue:
            payload_data['catalogueId'] = None
        else:
            payload_data['catalogueId'] = catalogue_id

    # update node
    resource.pop('node', None)
    resource['nodePID'] = node

    # Creators / Main Contacts
    # remove old
    creators = resource.get("creators")
    if creators:
        resource.pop('creators', None)
    main_contact = resource.get("mainContact")
    if main_contact:
        resource.pop('mainContact', None)
    # add new
    if internal_item in creator_list:
        resource["creators"] = [contact]
    if internal_item in main_contact_list:
        resource["mainContact"] = contact

    # add type
    if internal_item in type_mapping:
        resource['type'] = type_mapping[internal_item]

    # update ID, Identifiers
    metadata = payload_data.get('metadata')
    if metadata:
        published = metadata.get('published')
        identifiers = payload_data.get('identifiers')
        if identifiers:
            originalId = identifiers.get('originalId')
            if originalId:
                identifiers['originalId'] = update_identifier(originalId, force_suffix=True)
            pid = identifiers.get('pid')
            if pid:
                identifiers['pid'] = update_identifier(pid)

        # # update ID
        payload_id = payload_data.get('id')
        new_payload_id = update_identifier(payload_id, published)
        payload_data['id'] = new_payload_id
        resource['id'] = new_payload_id
        # save id to search for duplicates later
        all_ids.append(new_payload_id)

        # resource-specific fields && related IDs
        # adapter
        if internal_item == "adapter":
            resource['resourceOwner'] = "changeme!"
            adapter_ids_needing_owner.append(new_payload_id)

            # add publishingDate
            resource['publishingDate'] = "2026-03-15"

            # refactor lastUpdate (ISO 8601)
            if resource.get("lastUpdate") is not None:
                resource["lastUpdate"] = datetime.fromtimestamp(resource["lastUpdate"] / 1000, UTC).date().isoformat()

            # add public contacts
            resource['publicContacts'] = ["default@example.com"]

            # linkedResource
            linked_resource = resource.get('linkedResource')
            if linked_resource and 'id' in linked_resource:
                linked_resource['id'] = update_identifier(linked_resource['id'], published)
                # linked_resource['linkedResourceId'] = linked_resource.pop('id')
                linked_resource['resource_type'] = linked_resource.pop('type').lower()

            # update repository
            repo = resource.pop('softwareRepository', None)
            if repo:
                resource['repository'] = repo

            # update releases
            releases = resource.pop('releases', None)
            if releases:
                resource['package'] = releases
            else:
                resource['package'] = "https://example.com"

            # remove old license
            resource.pop('license', None)

            # remove admins
            resource.pop('admins', None)

        # configuration template
        if internal_item == "configurationTemplate":
            # interoperability record id
            interoperability_record_id = resource.get('interoperabilityRecordId', None)
            if interoperability_record_id:
                resource['interoperabilityRecordId'] = update_identifier(interoperability_record_id, published)

        # configuration template instance
        if internal_item == "configurationTemplateInstance":
            # resource id
            resource_id = resource.get('resourceId', None)
            if resource_id:
                resource['resourceId'] = update_identifier(resource_id, published)

        # deployable service
        if internal_item == "deployableService":
            # update resourceTypeName
            json_data['resourceTypeName'] = "deployable_application"

            # add publishingDate
            resource['publishingDate'] = "2026-03-15"

            # refactor lastUpdate (ISO 8601)
            if resource.get("lastUpdate") is not None:
                resource["lastUpdate"] = datetime.fromtimestamp(resource["lastUpdate"] / 1000, UTC).date().isoformat()

            # add public contacts
            resource['publicContacts'] = ["default@example.com"]

            # resourceOrganisation
            resource_organisation = resource.pop('resourceOrganisation', None)
            if resource_organisation:
                resource['resourceOwner'] = update_identifier(resource_organisation, published)

            # remove url
            resource.pop('url', None)

            # remove software license
            resource.pop('softwareLicense', None)

            # rename payload to deployableApplication
            payload_data["deployableApplication"] = payload_data.pop("deployableService")

        # interoperability records
        if internal_item == "interoperabilityRecord":
            # add publishingDate
            resource['publishingDate'] = "2026-03-15"

            # add public contacts
            resource['publicContacts'] = ["default@example.com"]

            # provider id
            provider_id = resource.pop('providerId', None)
            if provider_id:
                resource['resourceOwner'] = update_identifier(provider_id, published)

            # update title
            title = resource.pop('title', None)
            if title:
                resource['name'] = title

            # remove old identifier info
            resource.pop('identifierInfo', None)

            # remove publicationYear
            resource.pop('publicationYear', None)

            # refactor resourceTypesInfo
            resource_types_info = resource.pop('resourceTypesInfo', None)
            if resource_types_info:
                if isinstance(resource_types_info, list) and len(resource_types_info) > 0:
                    first = resource_types_info[0]
                else:
                    first = resource_types_info
                first['resourceTypeGeneral'] = "Guideline"
                resource['resourceTypeInfo'] = first

            # remove created
            resource.pop('created', None)

            # remove updated
            resource.pop('updated', None)

            # remove rights
            resource.pop('rights', None)

            # remove status
            resource.pop('status', None)

            # remove domain
            resource.pop('domain', None)

            # remove eoscGuidelineType
            resource.pop('eoscGuidelineType', None)

            # remove eoscIntegrationOptions
            resource.pop('eoscIntegrationOptions', None)

            # remove alternativeIdentifiers
            resource.pop('alternativeIdentifiers', None)

        # provider
        if internal_item == "provider":
            # update resourceTypeName
            json_data['resourceTypeName'] = "organisation"

            # re-introduce public contacts
            resource.pop('publicContacts', None)
            resource['publicContacts'] = ["default@example.com"]

            # remove alternativeIdentifiers
            resource.pop('alternativeIdentifiers', None)

            # remove scientificDomains
            resource.pop('scientificDomains', None)

            # remove tags
            resource.pop('tags', None)

            # remove structureTypes
            resource.pop('structureTypes', None)

            # location
            location = resource.pop("location", None)
            if isinstance(location, dict):
                country = location.get("country")
                if country:
                    resource["country"] = country

            # remove lifeCycleStatus
            resource.pop('lifeCycleStatus', None)

            # remove certifications
            resource.pop('certifications', None)

            # remove participatingCountries
            resource.pop('participatingCountries', None)

            # remove affiliations
            resource.pop('affiliations', None)

            # remove esfriDomains
            resource.pop('esfriDomains', None)

            # remove esfriType
            resource.pop('esfriType', None)

            # remove networks
            resource.pop('networks', None)

            # remove merilScientificDomains
            resource.pop('merilScientificDomains', None)

            # remove areasOfActivity
            resource.pop('areasOfActivity', None)

            # remove societalGrandChallenges
            resource.pop('societalGrandChallenges', None)

            # remove nationalRoadmaps
            resource.pop('nationalRoadmaps', None)

            # rename payload to organisation
            payload_data["organisation"] = payload_data.pop("provider")

        # resource interoperability record
        if internal_item == "resourceInteroperabilityRecord":
            # resource id
            resource_id = resource.get('resourceId', None)
            if resource_id:
                resource['resourceId'] = update_identifier(resource_id, published)

            # interoperability record ids
            interoperability_record_ids = resource.get('interoperabilityRecordIds')
            if isinstance(interoperability_record_ids, list):
                resource['interoperabilityRecordIds'] = [
                    update_identifier(interoperability_record_id, published)
                    for interoperability_record_id in interoperability_record_ids
                    if interoperability_record_id
                ]

        # service
        if internal_item == "service":
            # add publishingDate
            resource['publishingDate'] = "2026-03-15"

            # re-introduce public contacts
            resource.pop('publicContacts', None)
            resource['publicContacts'] = ["default@example.com"]

            # resource organisation
            resource_organisation = resource.pop('resourceOrganisation', None)
            if resource_organisation:
                resource['resourceOwner'] = update_identifier(resource_organisation, published)

            # resource providers
            resource_providers = resource.pop('resourceProviders', None)
            if resource_providers:
                resource['serviceProviders'] = [
                    update_identifier(provider, published)
                    for provider in resource_providers
                    if provider
                ]

            # add jurisdiction
            resource['jurisdiction'] = 'ds_jurisdiction-global'

            # remove abbreviation
            resource.pop('abbreviation', None)

            # remove alternativeIdentifiers
            resource.pop('alternativeIdentifiers', None)

            # remove multimedia
            resource.pop('multimedia', None)

            # remove useCases
            resource.pop('useCases', None)

            # remove targetUsers
            resource.pop('targetUsers', None)

            # remove accessModes
            resource.pop('accessModes', None)

            # remove horizontalService
            resource.pop('horizontalService', None)

            # remove serviceCategories
            resource.pop('serviceCategories', None)

            # remove marketplaceLocations
            resource.pop('marketplaceLocations', None)

            # remove geographicalAvailabilities
            resource.pop('geographicalAvailabilities', None)

            # remove languageAvailabilities
            resource.pop('languageAvailabilities', None)

            # remove resourceGeographicLocations
            resource.pop('resourceGeographicLocations', None)

            # remove helpdeskEmail
            resource.pop('helpdeskEmail', None)

            # remove securityContactEmail
            resource.pop('securityContactEmail', None)

            # remove lifeCycleStatus
            resource.pop('lifeCycleStatus', None)

            # remove certifications
            resource.pop('certifications', None)

            # remove standards
            resource.pop('standards', None)

            # remove openSourceTechnologies
            resource.pop('openSourceTechnologies', None)

            # remove version
            resource.pop('version', None)

            # remove lastUpdate
            resource.pop('lastUpdate', None)

            # remove changeLog
            resource.pop('changeLog', None)

            # remove requiredResources
            resource.pop('requiredResources', None)

            # remove relatedResources
            resource.pop('relatedResources', None)

            # remove relatedPlatforms
            resource.pop('relatedPlatforms', None)

            # remove fundingBody
            resource.pop('fundingBody', None)

            # remove fundingPrograms
            resource.pop('fundingPrograms', None)

            # remove tagline
            resource.pop('tagline', None)

            # remove grantProjectNames
            resource.pop('grantProjectNames', None)

            # remove helpdeskPage
            resource.pop('helpdeskPage', None)

            # remove userManual
            resource.pop('userManual', None)

            # remove resourceLevel
            resource.pop('resourceLevel', None)

            # remove trainingInformation
            resource.pop('trainingInformation', None)

            # remove statusMonitoring
            resource.pop('statusMonitoring', None)

            # remove maintenance
            resource.pop('maintenance', None)

            # remove paymentModel
            resource.pop('paymentModel', None)

            # remove pricing
            resource.pop('pricing', None)

        # datasource
        if internal_item == "datasource":
            # add originalOpenAIREId on alternativePIDs
            if payload_data.get('originalOpenAIREId') is not None:
                pid = payload_data['originalOpenAIREId']
                pidSchema = "openaire"
                resource['alternativePIDs'] = [{"pid": pid, "pidSchema": pidSchema}]

            # add name
            resource['name'] = "Datasource Name - Update me"

            # add description
            resource['description'] = "Datasource description - Update me"

            # add publishingDate
            resource['publishingDate'] = "2026-03-15"

            # re-introduce public contacts
            resource.pop('publicContacts', None)
            resource['publicContacts'] = ["default@example.com"]

            # resource owner
            service_id = resource.pop('serviceId', None)
            if service_id:
                resource_organisation = service_owner_map.get(service_id)
                if resource_organisation:
                    resource['resourceOwner'] = update_identifier(resource_organisation, published)

            # datasource classification
            if resource.get("datasourceClassification") is None:
                resource['datasourceClassification'] = "ds_classification-repository"

            # jurisdiction
            if resource.get("jurisdiction") is None:
                resource['jurisdiction'] = "ds_jurisdiction-global"

            # researchEntityTypes
            research_entity_types = resource.pop('researchEntityTypes', None)
            if research_entity_types:
                resource['researchProductTypes'] = research_entity_types
            else:
                resource['researchProductTypes'] = ['ds_research_entity_type-research_data']

            # add webpage
            resource['webpage'] = "https://example.com"

            # add trl
            resource['trl'] = "trl-9"

            # remove harvestable
            resource.pop('harvestable', None)

            # remove researchProductAccessPolicies
            resource.pop('researchProductAccessPolicies', None)

            # remove researchProductLicensings
            resource.pop('researchProductLicensings', None)

            # remove researchProductMetadataAccessPolicies
            resource.pop('researchProductMetadataAccessPolicies', None)

            # remove researchProductMetadataLicensing
            resource.pop('researchProductMetadataLicensing', None)

            # remove versionControl
            resource.pop('versionControl', None)

        # training resource
        if internal_item == "trainingResource":
            # add publishingDate
            resource['publishingDate'] = "2026-03-15"

            # refactor versionDate (ISO 8601)
            if resource.get("versionDate") is not None:
                resource["versionDate"] = datetime.fromtimestamp(resource["versionDate"] / 1000, UTC).date().isoformat()

            # add public contacts
            resource['publicContacts'] = ["default@example.com"]

            # resource organisation
            resource_organisation = resource.pop('resourceOrganisation', None)
            if resource_organisation:
                resource['resourceOwner'] = update_identifier(resource_organisation, published)

            # eosc related services
            eosc_related_services = resource.get('eoscRelatedServices')
            if isinstance(eosc_related_services, list):
                resource['eoscRelatedServices'] = [
                    update_identifier(eosc_related_service, published)
                    for eosc_related_service in eosc_related_services
                    if eosc_related_service
                ]

            # update title
            title = resource.pop('title', None)
            if title:
                resource['name'] = title

            # remove resourceProviders
            resource.pop('resourceProviders', None)

            # remove authors
            resource.pop('authors', None)

            # remove url
            resource.pop('url', None)

            # remove urlType
            resource.pop('urlType', None)

            # remove alternativeIdentifiers
            resource.pop('alternativeIdentifiers', None)

            # remove license
            resource.pop('license', None)

            # remove geographicalAvailabilities
            resource.pop('geographicalAvailabilities', None)

            # remove contact
            resource.pop('contact', None)

    # update payload
    json_data['payload'] = json.dumps(payload_data)
    return json_data


def determine_internal_item(resourceType):
    if resourceType == 'training_resource':
        internalItem = 'trainingResource'
    elif resourceType == 'deployable_service':
        internalItem = 'deployableService'
    elif resourceType == 'interoperability_record':
        internalItem = 'interoperabilityRecord'
    elif resourceType == 'resource_interoperability_record':
        internalItem = 'resourceInteroperabilityRecord'
    elif resourceType == 'configuration_template':
        internalItem = 'configurationTemplate'
    elif resourceType == 'configuration_template_instance':
        internalItem = 'configurationTemplateInstance'
    else:
        internalItem = resourceType
    return internalItem


def update_identifier(value, published=None, force_suffix=False):
    if not value or '/' not in value:
        return value

    prefix, suffix = value.split('/', 1)
    prefix = resource_type_mapping.get(prefix, prefix)

    if published is False or force_suffix:
        suffix = f"{suffix}00"

    return f"{prefix}/{suffix}"


def find_duplicates(ids):
    seen = set()
    duplicates = set()
    for string in ids:
        if string in seen:
            duplicates.add(string)
        else:
            seen.add(string)
    print("Duplicates: ", list(duplicates))


def rename_folders(base_path, dry_run=False):
    for old, new in folder_renames.items():
        old_path = os.path.join(base_path, old)
        new_path = os.path.join(base_path, new)

        if os.path.exists(old_path):
            if dry_run:
                print(f"[DRY RUN] Would rename folder: {old} -> {new}")
            else:
                os.rename(old_path, new_path)


def delete_folders(base_path, dry_run=False):
    for folder in deleteFolders:
        folder_path = os.path.join(base_path, folder)
        if os.path.exists(folder_path):
            if dry_run:
                print(f"[DRY RUN] Would delete folder: {folder}")
            else:
                shutil.rmtree(folder_path)


def delete_schema_files(base_path, dry_run=False):
    for folder in os.listdir(base_path):
        schema_path = os.path.join(base_path, folder, 'schema.json')
        if os.path.isfile(schema_path):
            if dry_run:
                print(f"[DRY RUN] Would delete: {folder}/schema.json")
            else:
                os.remove(schema_path)


def print_migration_report():
    print("\n" + "=" * 60)
    print("POST-MIGRATION CHECKLIST")
    print("=" * 60)

    if adapter_ids_needing_owner:
        print("[ACTION REQUIRED]")
        print(f"{len(adapter_ids_needing_owner)} adapter(s) have resourceOwner set to 'changeme!'")
        print("Update each one with the correct Organisation ID:")
        for adapter_id in adapter_ids_needing_owner:
            print(f"  - {adapter_id}")

    print("\n[REVIEW]")
    print("The following placeholder values were written to all applicable resources:")
    print("  - contact (email / firstName / lastName)  →  'contact' dict at top of script")
    print("  - publicContacts                          →  'default@example.com'")
    print("  - publishingDate                          →  '2026-03-15'")
    print("  - datasource name / description           →  'Update me' strings")
    print("  - adapter / datasource webpage / package  →  'https://example.com'")
    print("=" * 60)


##################################################### FUNCTIONS ########################################################

######################################################## RUN ###########################################################
parser = argparse.ArgumentParser(
    description="Migrate resource catalogue JSON files from Profile v5 to Profile v6.",
    epilog="A timestamped backup is created automatically before any changes are made. Use --dry-run to preview changes without writing anything."
)
parser.add_argument(
    "-p", "--path",
    help="Path to the root directory containing the exported v5 resource folders.",
    type=str, required=True
)
parser.add_argument(
    "-c", "--catalogue",
    help="Default catalogue ID. Resources belonging to this catalogue will have their catalogueId set to null in the migrated output.",
    type=str, required=True
)
parser.add_argument(
    "-n", "--node",
    help="Node PID to assign to all migrated resources (e.g. 21.15999/node1).",
    type=str, required=True
)
parser.add_argument(
    "--dry-run",
    help="Preview all changes without writing, renaming, or deleting anything.",
    action="store_true"
)
args = parser.parse_args()
if args.dry_run:
    print("[DRY RUN] No files will be modified.\n")
else:
    backup_directory(args.path)
service_owner_map = build_service_owner_map(args.path)
folder_selection(args.path, args.catalogue, args.node, service_owner_map, args.dry_run)
rename_folders(args.path, args.dry_run)
delete_folders(args.path, args.dry_run)
delete_schema_files(args.path, args.dry_run)
find_duplicates(all_ids)
print_migration_report()
######################################################## RUN ###########################################################
