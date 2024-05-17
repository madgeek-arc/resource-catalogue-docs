######################################################## IMPORTS #######################################################
import json
import os
import argparse
######################################################## IMPORTS #######################################################

##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    migrationFolders = ['/datasource/']
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                isVersion = False
                with open(directory + migrationFolder + file, 'r') as json_file:
                    json_data = migrate(json_file, isVersion)
                    # write to file
                    with open(directory + migrationFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
            if file.endswith('-version'):
                isVersion = True
                versionFiles = os.listdir(directory + migrationFolder + file)
                for versionFile in versionFiles:
                    with open(directory + migrationFolder + file + '/' + versionFile, 'r') as json_file:
                        json_data = migrate(json_file, isVersion)
                        # write to file
                        with open(directory + migrationFolder + file + '/' + versionFile, 'w') as json_file:
                            json.dump(json_data, json_file, indent=2)

def migrate(json_file, isVersion):
    json_data = json.load(json_file)
    payload_str = json_data['payload']
    payload_data = json.loads(payload_str)

    # migrate originalId
    datasource = payload_data.get('datasource')
    if datasource is not None:
        datasource_id = datasource.get('id')
        identifiers = payload_data.get('identifiers')
        if identifiers is not None:
            original_id = identifiers.get('originalId')
            if original_id is not None:
                identifiers['originalId'] = datasource_id.split(".")[1] + "." + datasource_id.split(".")[2]
                payload_data['identifiers'] = identifiers

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