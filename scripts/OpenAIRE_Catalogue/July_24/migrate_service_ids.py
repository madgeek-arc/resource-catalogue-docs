######################################################## IMPORTS #######################################################
import argparse
import json
import os
from datetime import datetime, timezone
######################################################## IMPORTS #######################################################

old_to_new_ids_mapping = {
    'openaire.amnesia': 'athenarc.amnesia',
    'openaire.zenodo': 'cern.zenodo',
    'openaire.openaire_login': 'openaire.aai',
    'openaire.research_community_dashboard': 'openaire.connect',
    'openaire.data_provider_dashboard': 'openaire.provide',
    'openaire.validator': 'openaire.metadata_validator',
    'openaire.usage_statistics': 'openaire.usagecounts',
    'openaire.funder_dashboard': 'openaire.monitor',
    'openaire.episciences': 'ccsd.episciences',
    'openaire.opencitations': 'unibo.opencitations',
    'openaire.openapc': 'unibi-ub.openapc',
    'openaire.discovery_portal': 'openaire.explore'
}

##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    migrationFolders = ['/service/', '/datasource/']
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json') and file != 'schema.json':
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
    payload_str = json_data['payload']
    payload_data = json.loads(payload_str)
    resource = payload_data.get(resourceType)

    resourceId = resource.get('id')
    if resourceId in old_to_new_ids_mapping:
        payload_data['id'] = old_to_new_ids_mapping[resourceId]
        resource['id'] = payload_data['id']
    # providerId = resource['id'].split(".")[0]

    if resourceType == "service":
        # resource['resourceOrganisation'] = providerId
        # resourceProviders = resource.get('resourceProviders')
        # if resourceProviders and any(resourceProviders):
        #     for i in range(len(resourceProviders)):
        #         resourceProvider = resourceProviders[i]
        #         if resourceProvider == resourceId:
        #             resourceProviders[i] = providerId
        requiredResources = resource.get('requiredResources')
        if requiredResources and any(requiredResources):
            for i in range(len(requiredResources)):
                requiredResource = requiredResources[i]
                if requiredResource in old_to_new_ids_mapping:
                    requiredResources[i] = old_to_new_ids_mapping[requiredResource]
        relatedResources = resource.get('relatedResources')
        if relatedResources and any(relatedResources):
            for i in range(len(relatedResources)):
                relatedResource = relatedResources[i]
                if relatedResource in old_to_new_ids_mapping:
                    relatedResources[i] = old_to_new_ids_mapping[relatedResource]

    if resourceType == "datasource":
        serviceId = resource.get('serviceId')
        if serviceId in old_to_new_ids_mapping:
            resource['serviceId'] = old_to_new_ids_mapping[serviceId]

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
