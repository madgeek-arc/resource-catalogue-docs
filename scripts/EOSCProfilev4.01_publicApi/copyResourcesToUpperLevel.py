######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring
import os
from bs4 import BeautifulSoup as bs
import argparse
import uuid
from xml.dom import minidom
######################################################## IMPORTS #######################################################


################################################### GLOBAL VARIABLES ###################################################
global directory
################################################### GLOBAL VARIABLES ###################################################


##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    # migrationFolders = ['/provider/', '/pending_provider/', '/infra_service/', '/pending_service/']
    migrationFolders = ['/provider/']
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

    # copy to upper level
    service = root.find('{http://einfracentral.eu}service')
    isService = False
    if service is not None:
        isService = True
    active = root.find('{http://einfracentral.eu}active')
    status = root.find('{http://einfracentral.eu}status')
    if isService:
        latest = root.find('{http://einfracentral.eu}latest')
    if not isVersion:
        if active is not None and active.text == 'true':
            if status is not None and status.text == 'approved provider':
                provider = root.find('{http://einfracentral.eu}provider')
                id = provider.find('{http://einfracentral.eu}id')
                catalogueId = provider.find('{http://einfracentral.eu}catalogueId')
                metadata = root.find('{http://einfracentral.eu}metadata')
                published = metadata.find('{http://einfracentral.eu}metadata')
                # identifier = root.find('{http://einfracentral.eu}identifier')
                # if identifier is not None:
                #     originalId = identifier.find('{http://einfracentral.eu}originalId')
                # else:
                #     newIdentifier = ET.Element("tns:identifier")
                #     originalId = ET.Element("tns:originalId")
                #     originalId.text = id.text
                #     newIdentifier.append(originalId)
                # if originalId is not None:
                #     originalId.text = id.text
                # else:
                #     newOriginalId = ET.Element("tns:originalId")
                #     newOriginalId.text = id.text
                #     identifier.append(newOriginalId)
                if id is not None and catalogueId is not None:
                    id.text = catalogueId+'.'+id
                if published is not None:
                    published.text = 'true'
                json_data = copyToUpperLevel(json_data)
            elif isService and status.text == 'approved resource' and latest is not None and latest.text == 'true':
                json_data = copyToUpperLevel(json_data)

    root.write('output.xml')
    with open("output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)
        if isVersion:
            json_data['resource']['payload'] = json_data['payload']

    return json_data

def copyToUpperLevel(json_data):
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