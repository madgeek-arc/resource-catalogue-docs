######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
######################################################## IMPORTS #######################################################


##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    migrationFolders = ['/infra_service/', '/datasource/']  #TODO: Change folder name to '/infra_service/' for PROD
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
    xml = json_data['payload']
    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    resource = root.find('{http://einfracentral.eu}service')
    if resource is None:
        resource = root.find('{http://einfracentral.eu}datasource')
    catalogueId = resource.find('{http://einfracentral.eu}catalogueId')
    resourceOrganisation = resource.find('{http://einfracentral.eu}resourceOrganisation')
    resourceProviders = resource.find('{http://einfracentral.eu}resourceProviders')
    requiredResources = resource.find('{http://einfracentral.eu}requiredResources')
    relatedResources = resource.find('{http://einfracentral.eu}relatedResources')

    # service/datasource bundle -> update IDs of various fields with Public IDs
    # (resourceOrganisation / resourceProviders / requiredResources / relatedResources)
    metadata = root.find('{http://einfracentral.eu}metadata')
    if metadata is not None:
        published = metadata.find('{http://einfracentral.eu}published')
        if published is not None:
            if published.text == 'true':
                if catalogueId is not None:
                    if resourceOrganisation is not None and resourceOrganisation != "":
                        resourceOrganisation.text = catalogueId.text + '.' + resourceOrganisation.text
                    if resourceProviders is not None:
                        for resourceProvider in resourceProviders:
                            if resourceProvider is not None and resourceProvider != "":
                                if resourceProvider.text is not None:
                                    resourceProvider.text = catalogueId.text + '.' + resourceProvider.text
                    if requiredResources is not None:
                        for requiredResource in requiredResources:
                            if requiredResource is not None and requiredResource != "":
                                if requiredResource.text is not None:
                                    requiredResource.text = catalogueId.text + '.' + requiredResource.text
                    if relatedResources is not None:
                        for relatedResource in relatedResources:
                            if relatedResource is not None and relatedResource != "":
                                if relatedResource.text is not None:
                                    relatedResource.text = catalogueId.text + '.' + relatedResource.text


    root.write('output.xml')
    with open("output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)
        if isVersion:
            json_data['resource']['payload'] = json_data['payload']

    return json_data
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
folder_selection(args.path)
######################################################## RUN ###########################################################