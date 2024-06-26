######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
######################################################## IMPORTS #######################################################

##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    migrationFolders = ['/catalogue/', '/provider/', '/service/', '/training_resource/', '/interoperability_record/']
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
    tree = root.getroot()

    # migrate audit state
    auditState = root.find('{http://einfracentral.eu}auditState')
    if auditState is None:
        newAuditState = ET.Element("tns:auditState")

        # if audit functionality restart on Beyond / LOT1
        # newAuditState.text = "Not audited"
        # if audit functionality resumes from EOSC Future
        newAuditState.text = get_latest_audit_state(root)

        tree.append(newAuditState)

    root.write('output.xml')
    with open("output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)
        if isVersion:
            json_data['resource']['payload'] = json_data['payload']

    return json_data


def get_latest_audit_state(root):
    sortedLoggingInfo = sorted(root.findall('.//{http://einfracentral.eu}loggingInfo'),
                                 key=lambda x: int(x.find('{http://einfracentral.eu}date').text))
    for loggingInfo in sortedLoggingInfo:
        if loggingInfo is not None:
            type = loggingInfo.find('{http://einfracentral.eu}type')
            if type is not None:
                if type.text == "audit":
                    actionType = loggingInfo.find('{http://einfracentral.eu}actionType')
                    if actionType is not None:
                        if actionType.text == "valid":
                            return "Valid"
                        else:
                            return "Invalid and not updated"
    return "Not audited"

##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
folder_selection(args.path)
######################################################## RUN ###########################################################