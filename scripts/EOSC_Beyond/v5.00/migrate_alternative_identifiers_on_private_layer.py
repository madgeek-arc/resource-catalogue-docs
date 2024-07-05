# ######################################################## IMPORTS #######################################################
# import json
# import os
# import argparse
# ######################################################## IMPORTS #######################################################
#
# TODO: LOT1 DOES NOT NEED THIS
# TODO: BEYOND NEEDS TO MIGRATE AND REGISTER NEW PIDS AFTER TOMBSTONE HAS BEEN SET FOR OLD IDS
# TODO: BACKUP -> old_pids.zip
# TODO: NEEDS TESTING
#
# ##################################################### FUNCTIONS ########################################################
# def folder_selection(directory):
#     migrationFolders = ['/provider/', '/service/', '/training_resource/', '/interoperability_record/']
#     for migrationFolder in migrationFolders:
#         for file in os.listdir(directory + migrationFolder):
#             if file.endswith('.json'):
#                 isVersion = False
#                 with open(directory + migrationFolder + file, 'r') as json_file:
#                     json_data = migrate(json_file, isVersion, migrationFolder.replace("/", ""))
#                     # write to file
#                     # with open(directory + migrationFolder + file, 'w') as json_file:
#                     #     json.dump(json_data, json_file, indent=2)
#             # if file.endswith('-version'):
#             #     isVersion = True
#             #     versionFiles = os.listdir(directory + migrationFolder + file)
#             #     for versionFile in versionFiles:
#             #         with open(directory + migrationFolder + file + '/' + versionFile, 'r') as json_file:
#             #             json_data = migrate(json_file, isVersion, migrationFolder.replace("/", ""))
#             #             # write to file
#             #             with open(directory + migrationFolder + file + '/' + versionFile, 'w') as json_file:
#             #                 json.dump(json_data, json_file, indent=2)
#
#
# def migrate(json_file, isVersion, resourceType):
#     internalItem = determine_internal_item(resourceType)
#     json_data = json.load(json_file)
#     payload_str = json_data['payload']
#     payload_data = json.loads(payload_str)
#     metadata = payload_data.get('metadata')
#     if metadata is not None:
#         published = metadata.get('published')
#     resource = payload_data.get(internalItem)
#     resourceId = resource.get('id')
#     alternativeIdentifiers = resource.get('alternativeIdentifiers')
#
#     if not published: #TODO: probably remove this and enable for both layers
#         # Migrate alternativeIdentifiers field
#         if alternativeIdentifiers is None or len(alternativeIdentifiers) == 0:
#             alternative_identifiers_list = AlternativeIdentifierHelper()
#             new_identifier = AlternativeIdentifier(typee='EOSC PID', value=resourceId)
#             alternative_identifiers_list.add_type(new_identifier)
#             resource['alternativeIdentifiers'] = alternative_identifiers_list.to_dict()
#         else:
#             alternative_identifiers_list = AlternativeIdentifierHelper(alternativeIdentifiers)
#             new_identifier = AlternativeIdentifier(typee='EOSC PID', value=resourceId)
#             alternative_identifiers_list.add_type(new_identifier)
#             resource['alternativeIdentifiers'] = alternative_identifiers_list.to_dict()
#
#     # update payload
#     # json_data['payload'] = json.dumps(payload_data)
#     # if isVersion:
#     #     json_data['resource']['payload'] = json.dumps(payload_data)
#
#     return json_data
#
#
# def determine_internal_item(resourceType):
#     if resourceType == 'training_resource':
#         internalItem = 'trainingResource'
#     elif resourceType == 'interoperability_record':
#         internalItem = 'interoperabilityRecord'
#     else:
#         internalItem = resourceType
#     return internalItem
#
#
# class AlternativeIdentifier:
#     def __init__(self, typee, value):
#         self.type = typee
#         self.value = value
#
#     def to_dict(self):
#         return {
#             'type': self.type,
#             'value': self.value
#         }
#
#
# class AlternativeIdentifierHelper:
#     def __init__(self, alternative_identifier=None):
#         if alternative_identifier is None:
#             alternative_identifier = []
#         self.alternative_identifier = alternative_identifier
#
#     def to_dict(self):
#         return [identifier.to_dict() for identifier in self.alternative_identifier]
#
#     def add_type(self, identifier):
#         self.alternative_identifier.append(identifier)
# ##################################################### FUNCTIONS ########################################################
#
#
# ######################################################## RUN ###########################################################
# parser = argparse.ArgumentParser()
# parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
# args = parser.parse_args()
# folder_selection(args.path)
# ######################################################## RUN ###########################################################