######################################################## IMPORTS #######################################################
import json
import os
import argparse
from datetime import datetime, timezone
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
    payload = json.loads(json_data['payload'])

    # migrate Status
    if payload['status'] is None:
        payload['status'] = 'approved datasource'

    # migrate Active
    if payload['active'] is not None:
        payload['active'] = True

    # remove necessary fields
    if payload.get('resourceExtras') is None:
        payload.pop('resourceExtras', None)
    datasource = payload.get('datasource')
    if datasource:
        datasource.pop('name', None)
        datasource.pop('abbreviation', None)
        datasource.pop('resourceOrganisation', None)
        datasource.pop('resourceProviders', None)
        datasource.pop('webpage', None)
        datasource.pop('description', None)
        datasource.pop('tagline', None)
        datasource.pop('logo', None)
        datasource.pop('multimedia', None)
        datasource.pop('useCases', None)
        datasource.pop('scientificDomains', None)
        datasource.pop('categories', None)
        datasource.pop('targetUsers', None)
        datasource.pop('accessTypes', None)
        datasource.pop('accessModes', None)
        datasource.pop('tags', None)
        datasource.pop('geographicalAvailabilities', None)
        datasource.pop('languageAvailabilities', None)
        datasource.pop('resourceGeographicLocations', None)
        datasource.pop('mainContact', None)
        datasource.pop('publicContacts', None)
        datasource.pop('helpdeskEmail', None)
        datasource.pop('securityContactEmail', None)
        datasource.pop('trl', None)
        datasource.pop('lifeCycleStatus', None)
        datasource.pop('certifications', None)
        datasource.pop('standards', None)
        datasource.pop('openSourceTechnologies', None)
        datasource.pop('version', None)
        datasource.pop('lastUpdate', None)
        datasource.pop('changeLog', None)
        datasource.pop('requiredResources', None)
        datasource.pop('relatedResources', None)
        datasource.pop('relatedPlatforms', None)
        datasource.pop('fundingBody', None)
        datasource.pop('fundingPrograms', None)
        datasource.pop('grantProjectNames', None)
        datasource.pop('helpdeskPage', None)
        datasource.pop('userManual', None)
        datasource.pop('termsOfUse', None)
        datasource.pop('privacyPolicy', None)
        datasource.pop('accessPolicy', None)
        datasource.pop('resourceLevel', None)
        datasource.pop('trainingInformation', None)
        datasource.pop('statusMonitoring', None)
        datasource.pop('maintenance', None)
        datasource.pop('orderType', None)
        datasource.pop('order', None)
        datasource.pop('paymentModel', None)
        datasource.pop('pricing', None)
        datasource.pop('extras', None)

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