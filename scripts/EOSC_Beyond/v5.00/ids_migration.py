######################################################## IMPORTS #######################################################
import json
import os
import argparse
import random
import string
######################################################## IMPORTS #######################################################

######################################################## GLOBALS #######################################################
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
######################################################## GLOBALS #######################################################

##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    migrationFolders = ['/service/', '/provider/', '/datasource/', '/training_resource/', '/interoperability_record/',
                        '/monitoring/', '/resource_interoperability_record/']
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


#TODO: Migrate related resource IDs
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
                payload_data['id'] = cat + resourceType_mapping[resourceType] + '/' + random_generator()
                resource['id'] = payload_data['id']
                match_found = True
                break
        # publish false
        if not match_found:
            payload_data['id'] = resourceType_mapping[resourceType] + '/' + random_generator()
            resource['id'] = payload_data['id']

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
######################################################## RUN ###########################################################