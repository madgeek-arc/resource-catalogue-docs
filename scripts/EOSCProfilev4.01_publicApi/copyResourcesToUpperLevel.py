######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
import uuid
######################################################## IMPORTS #######################################################


################################################### GLOBAL VARIABLES ###################################################
global directory
################################################### GLOBAL VARIABLES ###################################################


##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    migrationFolders = ['/provider/', '/infra_service/']
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                with open(directory + migrationFolder + file, 'r') as json_file:
                    migrated_data = migrate(json_file)
                    json_data = update_core_id(migrated_data)
                    fileName = json_data.get("id")
                    # write to file
                    with open(directory + migrationFolder + fileName + '.json', 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)


def migrate(json_file):
    json_data = json.load(json_file)
    xml = json_data['payload']

    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    tree = root.getroot()

    # copy to upper level
    service = root.find('{http://einfracentral.eu}service')
    isService = False
    if service is not None:
        isService = True
    active = root.find('{http://einfracentral.eu}active')
    status = root.find('{http://einfracentral.eu}status')
    metadata = root.find('{http://einfracentral.eu}metadata')
    published = metadata.find('{http://einfracentral.eu}published')
    identifiers = root.find('{http://einfracentral.eu}identifiers')
    if isService:
        latest = root.find('{http://einfracentral.eu}latest')
        service = root.find('{http://einfracentral.eu}service')
        id = service.find('{http://einfracentral.eu}id')
        catalogueId = service.find('{http://einfracentral.eu}catalogueId')
    else:
        provider = root.find('{http://einfracentral.eu}provider')
        id = provider.find('{http://einfracentral.eu}id')
        catalogueId = provider.find('{http://einfracentral.eu}catalogueId')
    if active is not None and active.text == 'true':
        if (status is not None and status.text == 'approved provider') or \
                (status is not None and status.text == 'approved resource' and latest is not None and latest.text == 'true'):
            if identifiers is not None:
                originalId = identifiers.find('{http://einfracentral.eu}originalId')
                if originalId is not None:
                    originalId.text = id.text
            else:
                newIdentifier = ET.Element("tns:identifiers")
                tree.append(newIdentifier)
                originalId = ET.Element("tns:originalId")
                originalId.text = id.text
                newIdentifier.append(originalId)
            if id is not None and catalogueId is not None:
                id.text = catalogueId.text+'.'+id.text
            if published is not None:
                published.text = 'true'
            else:
                published = ET.Element("tns:published")
                published.text = 'true'
                metadata.append(published)

    root.write('output.xml')
    with open("output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)

    return json_data


def update_core_id(json_data):
    newId = str(uuid.uuid4())
    updateDict = {"id": newId}
    json_data.update(updateDict)
    return json_data
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
directory = args.path
folder_selection(args.path)
######################################################## RUN ###########################################################