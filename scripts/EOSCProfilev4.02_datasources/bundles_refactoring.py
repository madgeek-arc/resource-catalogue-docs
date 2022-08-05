######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
######################################################## IMPORTS #######################################################


##################################################### FUNCTIONS ########################################################
def service_migration(directory):
    migrationFolders = ['/infra_service/', '/pending_service/']
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                with open(directory + migrationFolder + file, 'r') as json_file:
                    json_data = migrate_services(json_file)
                    # write to file
                    with open(directory + migrationFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)


def migrate_services(json_file):
    json_data = json.load(json_file)
    xml = json_data['payload']

    # resourceTypeName
    if json_data['resourceTypeName'] == 'infra_service':
        json_data['resourceTypeName'] = 'service'

    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))

    # infraService -> serviceBundle
    root.getroot().tag = "{http://einfracentral.eu}serviceBundle"

    root.write('output.xml')
    with open("output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)

    return json_data
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
service_migration(args.path)
######################################################## RUN ###########################################################