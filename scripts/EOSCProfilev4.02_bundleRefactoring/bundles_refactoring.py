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
                isVersion = False
                with open(directory + migrationFolder + file, 'r') as json_file:
                    json_data = migrate_services(json_file, isVersion)
                    # write to file
                    with open(directory + migrationFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
            if file.endswith('-version'):
                isVersion = True
                versionFiles = os.listdir(directory + migrationFolder + file)
                for versionFile in versionFiles:
                    with open(directory + migrationFolder + file + '/' + versionFile, 'r') as json_file:
                        json_data = migrate_services(json_file, isVersion)
                        # write to file
                        with open(directory + migrationFolder + file + '/' + versionFile, 'w') as json_file:
                            json.dump(json_data, json_file, indent=2)


    # rename infra_service folder to service
    os.rename(directory + '/infra_service/', directory + '/service/')


def migrate_services(json_file, isVersion):
    json_data = json.load(json_file)
    xml = json_data['payload']

    # resourceTypeName
    if json_data['resourceTypeName'] == 'infra_service':
        json_data['resourceTypeName'] = 'service'

    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    tree = root.getroot()

    # infraService -> serviceBundle
    root.getroot().tag = "{http://einfracentral.eu}serviceBundle"

    # remove latest field
    latest = root.find('{http://einfracentral.eu}latest')
    if latest is not None:
        tree.remove(latest)

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
service_migration(args.path)
######################################################## RUN ###########################################################