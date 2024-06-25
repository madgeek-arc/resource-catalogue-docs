######################################################## IMPORTS #######################################################
import argparse
import json
import os
import random
import string
######################################################## IMPORTS #######################################################

# DELETE 6677b037-2ef2-46e9-aa75-62f7fc08ef3c, 9c39baa9-cf4c-4f31-abf1-18de1e1f0456

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
                    json_data = migrate_lower_layer(json_file, isVersion, migrationFolder.replace("/", ""))
                    # write to file
                    with open(directory + migrationFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
            if file.endswith('-version'):
                isVersion = True
                versionFiles = os.listdir(directory + migrationFolder + file)
                for versionFile in versionFiles:
                    with open(directory + migrationFolder + file + '/' + versionFile, 'r') as json_file:
                        json_data = migrate_lower_layer(json_file, isVersion, migrationFolder.replace("/", ""))
                        # write to file
                        with open(directory + migrationFolder + file + '/' + versionFile, 'w') as json_file:
                            json.dump(json_data, json_file, indent=2)


def migrate_lower_layer(json_file, isVersion, resourceType):
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
                # new_id = cat + resourceType_mapping[resourceType] + '/' + random_generator()
                # # Services & Datasources have the same IDs. Need to distinguish, so not to overwrite
                # if internalItem == 'datasource':
                #     old_to_new_ids_mapping[resourceId + '_datasource'] = new_id
                # else:
                #     old_to_new_ids_mapping[resourceId] = new_id
                # payload_data['id'] = new_id
                # resource['id'] = new_id
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
    core_id = json_data['id']
    payload_data = json.loads(payload_str)
    resource = payload_data.get(internalItem)

    # update public resources
    identifiers = payload_data.get('identifiers')
    if identifiers is not None:
        # update IDs
        resourceId = resource.get('id')
        try:
            for cat in catalogue_list:
                if cat in resourceId:
                    catalogueId, id = resourceId.split('.', 1)
            if id in old_to_new_ids_mapping:
                if internalItem == "datasource":
                    resource['id'] = catalogueId + old_to_new_ids_mapping[id + '_datasource']
                else:
                    resource['id'] = catalogueId + "." + old_to_new_ids_mapping[id]
                payload_data['id'] = resource['id']
        except ValueError as e:
            print(core_id)
        # update originalId
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
        else:
            try:
                catalogueId, id = resourceOrganisation.split('.', 1)
                if id in old_to_new_ids_mapping:
                    resource['resourceOrganisation'] = catalogueId + "." + old_to_new_ids_mapping[id]
            except ValueError as e:
                print(core_id)
        resourceProviders = resource.get('resourceProviders')
        if resourceProviders is not None:
            for i in range(len(resourceProviders)):
                resourceProvider = resourceProviders[i]
                if resourceProvider in old_to_new_ids_mapping:
                    resourceProviders[i] = old_to_new_ids_mapping[resourceProvider]
                else:
                    try:
                        catalogueId, id = resourceProvider.split('.', 1)
                        if id in old_to_new_ids_mapping:
                            resourceProviders[i] = catalogueId + "." + old_to_new_ids_mapping[id]
                    except ValueError as e:
                        print(core_id)
        requiredResources = resource.get('requiredResources')
        if requiredResources is not None:
            for i in range(len(requiredResources)):
                requiredResource = requiredResources[i]
                if requiredResource in old_to_new_ids_mapping:
                    requiredResources[i] = old_to_new_ids_mapping[requiredResource]
                else:
                    try:
                        catalogueId, id = requiredResource.split('.', 1)
                        if id in old_to_new_ids_mapping:
                            requiredResources[i] = catalogueId + "." + old_to_new_ids_mapping[id]
                    except ValueError as e:
                        print(core_id)
        relatedResources = resource.get('relatedResources')
        if relatedResources is not None:
            for i in range(len(relatedResources)):
                relatedResource = relatedResources[i]
                if relatedResource in old_to_new_ids_mapping:
                    relatedResources[i] = old_to_new_ids_mapping[relatedResource]
                else:
                    try:
                        catalogueId, id = relatedResource.split('.', 1)
                        if id in old_to_new_ids_mapping:
                            relatedResources[i] = catalogueId + "." + old_to_new_ids_mapping[id]
                    except ValueError as e:
                        print(core_id)
    elif internalItem == "datasource":
        serviceId = resource.get('serviceId')
        if serviceId in old_to_new_ids_mapping:
            resource['serviceId'] = old_to_new_ids_mapping[serviceId]
        else:
            try:
                catalogueId, id = serviceId.split('.', 1)
                if id in old_to_new_ids_mapping:
                    resource['serviceId'] = catalogueId + "." + old_to_new_ids_mapping[id]
            except ValueError as e:
                print(core_id)
    elif internalItem == "training_resource":
        resourceOrganisation = resource.get('resourceOrganisation')
        if resourceOrganisation in old_to_new_ids_mapping:
            resource['resourceOrganisation'] = old_to_new_ids_mapping[resourceOrganisation]
        else:
            try:
                catalogueId, id = resourceOrganisation.split('.', 1)
                if id in old_to_new_ids_mapping:
                    resource['resourceOrganisation'] = catalogueId + "." + old_to_new_ids_mapping[id]
            except ValueError as e:
                print(core_id)
        resourceProviders = resource.get('resourceProviders')
        if resourceProviders is not None:
            for i in range(len(resourceProviders)):
                resourceProvider = resourceProviders[i]
                if resourceProvider in old_to_new_ids_mapping:
                    resourceProviders[i] = old_to_new_ids_mapping[resourceProvider]
                else:
                    try:
                        catalogueId, id = resourceProvider.split('.', 1)
                        if id in old_to_new_ids_mapping:
                            resourceProviders[i] = catalogueId + "." + old_to_new_ids_mapping[id]
                    except ValueError as e:
                        print(core_id)
        eoscRelatedServices = resource.get('eoscRelatedServices')
        if eoscRelatedServices is not None:
            for i in range(len(eoscRelatedServices)):
                eoscRelatedService = eoscRelatedServices[i]
                if eoscRelatedService in old_to_new_ids_mapping:
                    eoscRelatedServices[i] = old_to_new_ids_mapping[eoscRelatedService]
                else:
                    try:
                        catalogueId, id = eoscRelatedService.split('.', 1)
                        if id in old_to_new_ids_mapping:
                            eoscRelatedServices[i] = catalogueId + "." + old_to_new_ids_mapping[id]
                    except ValueError as e:
                        print(core_id)
    elif internalItem == "interoperability_record":
        providerId = resource.get('providerId')
        if providerId in old_to_new_ids_mapping:
            resource['providerId'] = old_to_new_ids_mapping[providerId]
        else:
            try:
                catalogueId, id = providerId.split('.', 1)
                if id in old_to_new_ids_mapping:
                    resource['providerId'] = catalogueId + "." + old_to_new_ids_mapping[id]
            except ValueError as e:
                print(core_id)
    elif internalItem == "monitoring":
        serviceId = resource.get('serviceId')
        if serviceId in old_to_new_ids_mapping:
            resource['serviceId'] = old_to_new_ids_mapping[serviceId]
        else:
            try:
                catalogueId, id = serviceId.split('.', 1)
                if id in old_to_new_ids_mapping:
                    resource['serviceId'] = catalogueId + "." + old_to_new_ids_mapping[id]
            except ValueError as e:
                print(core_id)
    elif internalItem == "resource_interoperability_record":
        resourceId = resource.get('resourceId')
        if resourceId in old_to_new_ids_mapping:
            resource['resourceId'] = old_to_new_ids_mapping[resourceId]
        else:
            try:
                catalogueId, id = resourceId.split('.', 1)
                if id in old_to_new_ids_mapping:
                    resource['resourceId'] = catalogueId + "." + old_to_new_ids_mapping[id]
            except ValueError as e:
                print(core_id)
        interoperabilityRecordIds = resource.get('interoperabilityRecordIds')
        if interoperabilityRecordIds is not None:
            for i in range(len(interoperabilityRecordIds)):
                interoperabilityRecordId = interoperabilityRecordIds[i]
                if interoperabilityRecordId in old_to_new_ids_mapping:
                    interoperabilityRecordIds[i] = old_to_new_ids_mapping[interoperabilityRecordId]
                else:
                    try:
                        catalogueId, id = interoperabilityRecordId.split('.', 1)
                        if id in old_to_new_ids_mapping:
                            interoperabilityRecordIds[i] = catalogueId + "." + old_to_new_ids_mapping[id]
                    except ValueError as e:
                        print(core_id)

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