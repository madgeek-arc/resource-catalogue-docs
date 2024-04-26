######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
######################################################## IMPORTS #######################################################

##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    migrationFolders = ['/service/', '/datasource/']
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

    # set dummy value to termsOfUse field
    termsOfUse = resource.find('{http://einfracentral.eu}termsOfUse')
    if termsOfUse is None:
        newtermsOfUse = ET.Element("tns:termsOfUse")
        newtermsOfUse.text = 'https://wiki.eoscfuture.eu/display/PUBLIC/About+ToU+and+PP'
        resource.append(newtermsOfUse)
    # set dummy value to privacyPolicy field
    privacyPolicy = resource.find('{http://einfracentral.eu}privacyPolicy')
    if privacyPolicy is None:
        newprivacyPolicy = ET.Element("tns:privacyPolicy")
        newprivacyPolicy.text = 'https://wiki.eoscfuture.eu/display/PUBLIC/About+ToU+and+PP'
        resource.append(newprivacyPolicy)

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