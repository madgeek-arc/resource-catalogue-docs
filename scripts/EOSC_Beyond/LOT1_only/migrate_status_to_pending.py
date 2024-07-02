# Provider, Service, Datasource, Training Resource, Interoperability Record -> status = PENDING? (template_status?)

######################################################## IMPORTS #######################################################
import json
import os
import argparse
######################################################## IMPORTS #######################################################

##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    migrationFolders = ['/provider/', '/service/', '/datasource/', '/training_resource/', '/interoperability_record/']
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                isVersion = False
                with open(directory + migrationFolder + file, 'r') as json_file:
                    json_data = migrate(json_file, isVersion)
                    # write to file
                    with open(directory + migrationFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
            # if file.endswith('-version'):
            #     isVersion = True
            #     versionFiles = os.listdir(directory + migrationFolder + file)
            #     for versionFile in versionFiles:
            #         with open(directory + migrationFolder + file + '/' + versionFile, 'r') as json_file:
            #             json_data = migrate(json_file, isVersion)
            #             # write to file
            #             with open(directory + migrationFolder + file + '/' + versionFile, 'w') as json_file:
            #                 json.dump(json_data, json_file, indent=2)


def migrate(json_file, isVersion):
    json_data = json.load(json_file)
    payload_str = json_data['payload']
    payload_data = json.loads(payload_str)
    core_id = json_data['id']

    # set 'status' to PENDING
    status = payload_data.get('status')
    if status is not None:
        payload_data['status'] = 'PENDING'
    else:
        print(f"Resource with CORE ID {core_id} has no 'status' field")

    # update payload
    json_data['payload'] = json.dumps(payload_data)
    if isVersion:
        json_data['resource']['payload'] = json.dumps(payload_data)

    return json_data
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
folder_selection(args.path)
######################################################## RUN ###########################################################