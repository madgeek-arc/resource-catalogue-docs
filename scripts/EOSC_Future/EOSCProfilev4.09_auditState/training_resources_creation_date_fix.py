######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
######################################################## IMPORTS #######################################################
#TODO: IF WORKS AS EXPECTED ADD MIGRATION FUNCTIONALITY FOR ALL THE OTHER RESOURCES THAT GET AUDITED
##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    migrationFolders = ['/training_resource/']
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

    metadata = root.find('{http://einfracentral.eu}metadata')
    if metadata is not None:
        registeredAt = metadata.find('{http://einfracentral.eu}registeredAt')
        registeredBy = metadata.find('{http://einfracentral.eu}registeredBy')
        if registeredAt is not None:
            registeredAt.text = find_registration_date_and_user(root, True)
        if registeredBy is not None:
            registeredBy.text = find_registration_date_and_user(root, False)

    root.write('output.xml')
    with open("output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)
        if isVersion:
            json_data['resource']['payload'] = json_data['payload']

    return json_data


def find_registration_date_and_user(root, dateOrUser):
    sorted_logging_info = sorted(root.findall('.//{http://einfracentral.eu}loggingInfo'),
                                 key=lambda x: int(x.find('{http://einfracentral.eu}date').text))
    for logging_info in sorted_logging_info:
        actionType = logging_info.find('{http://einfracentral.eu}actionType')
        if actionType is not None:
            if actionType.text == 'registered':
                if dateOrUser:
                    date = logging_info.find('{http://einfracentral.eu}date')
                    if date is not None:
                        return date.text
                else:
                    userFullName = logging_info.find('{http://einfracentral.eu}userFullName')
                    if userFullName is not None:
                        return userFullName.text
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
folder_selection(args.path)
######################################################## RUN ###########################################################