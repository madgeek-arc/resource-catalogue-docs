######################################################## IMPORTS #######################################################
import json
import os
import argparse
from datetime import datetime, timezone
######################################################## IMPORTS #######################################################

##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    migrationFolders = ['/provider/', '/service/', '/datasource/']
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
    json_data = json.load(json_file)
    payload = json.loads(json_data['payload'])

    # migrate LoggingInfo
    resource = payload[resourceType]
    if resource is not None:
        resource['catalogueId'] = 'openaire'

    json_data['payload'] = json.dumps(payload, ensure_ascii=False)
    if isVersion:
        json_data['resource']['payload'] = json_data['payload']

    return json_data


def date_to_timestamp(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%a %b %d %H:%M:%S %Z %Y")
        date_utc = date_obj.replace(tzinfo=timezone.utc)
        return int(date_utc.timestamp() * 1000)
    except ValueError:
        return date_str
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
folder_selection(args.path)
######################################################## RUN ###########################################################