######################################################## IMPORTS #######################################################
import argparse
import json
import os
import random
import string
######################################################## IMPORTS #######################################################

######################################################## GLOBALS #######################################################
migrationFolders = ['/provider/', '/service/', '/datasource/', '/training_resource/', '/interoperability_record/',
                    '/monitoring/', '/resource_interoperability_record/']  # ordering matters!

resourceType_mapping = {
    'service': '21.11161',
    'provider': '21.15120',
    'datasource': 'dat',
    'training_resource': '21.11163',
    'interoperability_record': '21.15121',
    'monitoring': 'mon',
    'resource_interoperability_record': 'rir',
    'configuration_template': 'con',
    'configuration_template_instance': 'cti',
    'helpdesk': 'hel',
    'vocabulary_curation': 'cur'
}

catalogue_list = ['escape_ossr.', 'denbi_services.', 'bkh.', 'eosc.', 'eosc-nordic.', 'ni4os.', 'rdr.', 'essd.',
                  'argo_data_services.', 'ipcc_-_wmo_unep.', 'ierek_press.', 'datasciencespo.']

old_to_new_ids_mapping = {}
######################################################## GLOBALS #######################################################

##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                isVersion = False
                with open(directory + migrationFolder + file, 'r') as json_file:
                    json_data = migrate(json_file, isVersion, migrationFolder.replace("/", ""))
                    # write to file
                    with open(directory + migrationFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
            if file.endswith('-version'):
                isVersion = True
                versionFiles = os.listdir(directory + migrationFolder + file)
                for versionFile in versionFiles:
                    with open(directory + migrationFolder + file + '/' + versionFile, 'r') as json_file:
                        json_data = migrate(json_file, isVersion, migrationFolder.replace("/", ""))
                        # write to file
                        with open(directory + migrationFolder + file + '/' + versionFile, 'w') as json_file:
                            json.dump(json_data, json_file, indent=2)


def migrate(json_file, isVersion, resourceType):
    internalItem = determine_internal_item(resourceType)
    json_data = json.load(json_file)
    payload_str = json_data['payload']
    payload_data = json.loads(payload_str)
    resource = payload_data.get(internalItem)
    resourceId = resource.get('id')

    if resourceType in resourceType_mapping:
        match_found = False
        # publish true
        for cat in catalogue_list:
            if cat in resourceId:
                new_id = cat + resourceType_mapping[resourceType] + '/' + random_generator()
                # Services & Datasources have the same IDs. Need to distinguish, so not to overwrite
                if internalItem == 'datasource':
                    old_to_new_ids_mapping[resourceId + '_datasource'] = new_id
                else:
                    old_to_new_ids_mapping[resourceId] = new_id
                payload_data['id'] = new_id
                resource['id'] = new_id
                match_found = True
                break
        # publish false
        if not match_found:
            new_id = resourceType_mapping[resourceType] + '/' + random_generator()
            if internalItem == 'datasource':
                old_to_new_ids_mapping[resourceId + '_datasource'] = new_id
            else:
                old_to_new_ids_mapping[resourceId] = new_id
            payload_data['id'] = new_id
            resource['id'] = new_id

    # update payload
    json_data['payload'] = json.dumps(payload_data)
    if isVersion:
        json_data['resource']['payload'] = json.dumps(payload_data)

    return json_data


def rerun_folder_selection(directory):
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                isVersion = False
                with open(directory + migrationFolder + file, 'r') as json_file:
                    json_data = migrate_related_resources_ids(json_file, isVersion, migrationFolder.replace("/", ""))
                    # write to file
                    with open(directory + migrationFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
            if file.endswith('-version'):
                isVersion = True
                versionFiles = os.listdir(directory + migrationFolder + file)
                for versionFile in versionFiles:
                    with open(directory + migrationFolder + file + '/' + versionFile, 'r') as json_file:
                        json_data = migrate_related_resources_ids(json_file, isVersion,
                                                                  migrationFolder.replace("/", ""))
                        # write to file
                        with open(directory + migrationFolder + file + '/' + versionFile, 'w') as json_file:
                            json.dump(json_data, json_file, indent=2)


def migrate_related_resources_ids(json_file, isVersion, resourceType):
    internalItem = determine_internal_item(resourceType)
    json_data = json.load(json_file)
    payload_str = json_data['payload']
    payload_data = json.loads(payload_str)
    resource = payload_data.get(internalItem)

    # update originalId on public resources
    identifiers = payload_data.get('identifiers')
    if identifiers is not None:
        originalId = identifiers.get('originalId')
        if originalId is not None and originalId in old_to_new_ids_mapping:
            if internalItem == "datasource":
                identifiers['originalId'] = old_to_new_ids_mapping[originalId + '_datasource']
            else:
                identifiers['originalId'] = old_to_new_ids_mapping[originalId]

    if internalItem == "service":
        resourceOrganisation = resource.get('resourceOrganisation')
        if resourceOrganisation in old_to_new_ids_mapping:
            resource['resourceOrganisation'] = old_to_new_ids_mapping[resourceOrganisation]
        resourceProviders = resource.get('resourceProviders')
        if resourceProviders is not None:
            for i in range(len(resourceProviders)):
                resourceProvider = resourceProviders[i]
                if resourceProvider in old_to_new_ids_mapping:
                    resourceProviders[i] = old_to_new_ids_mapping[resourceProvider]
        requiredResources = resource.get('requiredResources')
        if requiredResources is not None:
            for i in range(len(requiredResources)):
                requiredResource = requiredResources[i]
                if requiredResource in old_to_new_ids_mapping:
                    requiredResources[i] = old_to_new_ids_mapping[requiredResource]
        relatedResources = resource.get('relatedResources')
        if relatedResources is not None:
            for i in range(len(relatedResources)):
                relatedResource = relatedResources[i]
                if relatedResource in old_to_new_ids_mapping:
                    relatedResources[i] = old_to_new_ids_mapping[relatedResource]
    elif internalItem == "datasource":
        serviceId = resource.get('serviceId')
        if serviceId in old_to_new_ids_mapping:
            resource['serviceId'] = old_to_new_ids_mapping[serviceId]
    elif internalItem == "training_resource":
        resourceOrganisation = resource.get('resourceOrganisation')
        if resourceOrganisation in old_to_new_ids_mapping:
            resource['resourceOrganisation'] = old_to_new_ids_mapping[resourceOrganisation]
        resourceProviders = resource.get('resourceProviders')
        if resourceProviders is not None:
            for i in range(len(resourceProviders)):
                resourceProvider = resourceProviders[i]
                if resourceProvider in old_to_new_ids_mapping:
                    resourceProviders[i] = old_to_new_ids_mapping[resourceProvider]
        eoscRelatedServices = resource.get('eoscRelatedServices')
        if eoscRelatedServices is not None:
            for i in range(len(eoscRelatedServices)):
                eoscRelatedService = eoscRelatedServices[i]
                if eoscRelatedService in old_to_new_ids_mapping:
                    eoscRelatedServices[i] = old_to_new_ids_mapping[eoscRelatedService]
    elif internalItem == "interoperability_record":
        providerId = resource.get('providerId')
        if providerId in old_to_new_ids_mapping:
            resource['providerId'] = old_to_new_ids_mapping[providerId]
    elif internalItem == "monitoring":
        serviceId = resource.get('serviceId')
        if serviceId in old_to_new_ids_mapping:
            resource['serviceId'] = old_to_new_ids_mapping[serviceId]
    elif internalItem == "resource_interoperability_record":
        resourceId = resource.get('resourceId')
        if resourceId in old_to_new_ids_mapping:
            resource['resourceId'] = old_to_new_ids_mapping[resourceId]
        interoperabilityRecordIds = resource.get('interoperabilityRecordIds')
        if interoperabilityRecordIds is not None:
            for i in range(len(interoperabilityRecordIds)):
                interoperabilityRecordId = interoperabilityRecordIds[i]
                if interoperabilityRecordId in old_to_new_ids_mapping:
                    interoperabilityRecordIds[i] = old_to_new_ids_mapping[interoperabilityRecordId]

    # update payload
    json_data['payload'] = json.dumps(payload_data)
    if isVersion:
        json_data['resource']['payload'] = json.dumps(payload_data)

    return json_data


def determine_internal_item(resourceType):
    if resourceType == 'training_resource':
        internalItem = 'trainingResource'
    elif resourceType == 'interoperability_record':
        internalItem = 'interoperabilityRecord'
    elif resourceType == 'resource_interoperability_record':
        internalItem = 'resourceInteroperabilityRecord'
    elif resourceType == 'configuration_template':
        internalItem = 'configurationTemplate'
    elif resourceType == 'configuration_template_instance':
        internalItem = 'configurationTemplateInstance'
    elif resourceType == 'vocabulary_curation':
        internalItem = 'vocabularyCuration'
    else:
        internalItem = resourceType
    return internalItem


def random_generator(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
folder_selection(args.path)
rerun_folder_selection(args.path)
######################################################## RUN ###########################################################