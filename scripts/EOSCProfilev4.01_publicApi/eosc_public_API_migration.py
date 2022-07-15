######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
######################################################## IMPORTS #######################################################


##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    migrationFolders = ['/provider/', '/pending_provider/', '/infra_service/', '/pending_service/']
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
    resourceCoreId = json_data['id']

    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    tree = root.getroot()
    resource = root.find('{http://einfracentral.eu}provider')
    if resource is None:
        resource = root.find('{http://einfracentral.eu}service')
    resourceId = resource.find('{http://einfracentral.eu}id').text

    # metadata -> ADD published, REMOVE source, originalId
    metadata = root.find('{http://einfracentral.eu}metadata')
    if metadata is not None:
        published = metadata.find('{http://einfracentral.eu}published')
        if published is None:
            newPublished = ET.Element("tns:published")
            newPublished.text = 'false'
            metadata.append(newPublished)
        source = metadata.find('{http://einfracentral.eu}source')
        if source is not None:
            metadata.remove(source)
        originalId = metadata.find('{http://einfracentral.eu}originalId')
        if originalId is not None:
            metadata.remove(originalId)
    else:
        print("Resource with id: [", resourceCoreId, "]-[", resourceId, "] has null Metadata. Creating them..")
        newMetadata = ET.Element("tns:metadata")
        newPublished = ET.Element("tns:published")
        newPublished.text = 'false'
        newMetadata.append(newPublished)
        tree.append(newMetadata)

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