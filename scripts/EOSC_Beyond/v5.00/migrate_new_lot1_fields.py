# Service -> classTier -> level = 3, accessPolicy = null, costModel = null
# Datasource -> softwareRepository = false?
# Everything except Vocabulary -> legacy = true

######################################################## IMPORTS #######################################################
import json
import os
import argparse
######################################################## IMPORTS #######################################################


##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    migrationFolders = ['/catalogue/', '/configuration_template/', '/configuration_template_instance/','/provider/',
                        '/service/', '/training_resource/', '/interoperability_record/', '/datasource/', '/monitoring/',
                        '/resource_interoperability_record/']
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                isVersion = False
                with open(directory + migrationFolder + file, 'r') as json_file:
                    json_data = migrate(json_file, isVersion, migrationFolder.replace("/", ""))
                    # # write to file
                    with open(directory + migrationFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
            # if file.endswith('-version'):
            #     isVersion = True
            #     versionFiles = os.listdir(directory + migrationFolder + file)
            #     for versionFile in versionFiles:
            #         with open(directory + migrationFolder + file + '/' + versionFile, 'r') as json_file:
            #             json_data = migrate(json_file, isVersion, migrationFolder.replace("/", ""))
            #             # write to file
            #             with open(directory + migrationFolder + file + '/' + versionFile, 'w') as json_file:
            #                 json.dump(json_data, json_file, indent=2)


def migrate(json_file, isVersion, resourceType):
    internalItem = determine_internal_item(resourceType)
    json_data = json.load(json_file)
    payload_str = json_data['payload']
    payload_data = json.loads(payload_str)
    resource = payload_data.get(internalItem)

    # new field legacy
    payload_data['legacy'] = True

    # new field softwareRepository
    if internalItem == 'datasource':
        payload_data['softwareRepository'] = False

    # new field classTier
    if internalItem == 'service':
        class_tier_instance = ClassTier(level=3, accessPolicy=None, costModel=None, offerings=None)
        resource['classTier'] = class_tier_instance.to_dict()


    # update payload
    json_data['payload'] = json.dumps(payload_data)
    if isVersion:
        json_data['resource']['payload'] = json.dumps(payload_data)

    return json_data


def determine_internal_item(resourceType):
    if resourceType == 'configuration_template':
        internalItem = 'configurationTemplate'
    elif resourceType == 'configuration_template_instance':
        internalItem = 'configurationTemplateInstance'
    elif resourceType == 'training_resource':
        internalItem = 'trainingResource'
    elif resourceType == 'interoperability_record':
        internalItem = 'interoperabilityRecord'
    elif resourceType == 'resource_interoperability_record':
        internalItem = 'resourceInteroperabilityRecord'
    else:
        internalItem = resourceType
    return internalItem


class ClassTier:
    def __init__(self, level, accessPolicy, costModel, offerings):
        self.level = level
        self.accessPolicy = accessPolicy
        self.costModel = costModel
        self.offerings = offerings

    def to_dict(self):
        return {
            'level': self.level,
            'accessPolicy': self.accessPolicy,
            'costModel': self.costModel,
            'offerings': self.offerings
        }
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
folder_selection(args.path)
######################################################## RUN ###########################################################