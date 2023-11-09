######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
from datetime import datetime
######################################################## IMPORTS #######################################################

###################################################### GLOBALS #########################################################
migrationFolders = ['/provider/', '/service/', '/training_resource/', '/interoperability_record/']
###################################################### GLOBALS #########################################################

##################################################### FUNCTIONS ########################################################
def datasource_migration(directory):
    for folder in migrationFolders:
        for file in os.listdir(directory + folder):
            if file.endswith('.json'):
                isVersion = False
                with open(directory + folder + file, 'r') as json_file:
                    json_data = latest_logging_info_migration(json_file, isVersion)
                    # write to file
                    with open(directory + folder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
            if file.endswith('-version'):
                isVersion = True
                versionFiles = os.listdir(directory + folder + file)
                for versionFile in versionFiles:
                    with open(directory + folder + file + '/' + versionFile, 'r') as json_file:
                        json_data = latest_logging_info_migration(json_file, isVersion)
                        # write to file
                        with open(directory + folder + file + '/' + versionFile, 'w') as json_file:
                            json.dump(json_data, json_file, indent=2)


def latest_logging_info_migration(json_file, isVersion):
    json_data = json.load(json_file)
    xml = json_data['payload']
    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    tree = root.getroot()

    # update LatestAuditInfo registry
    latestAuditInfo = root.find('{http://einfracentral.eu}latestAuditInfo')
    allLoggingInfo = root.findall('{http://einfracentral.eu}loggingInfo')
    allLoggingInfo.sort(key=sort_key, reverse=True)
    for loggingInfo in allLoggingInfo:
        if loggingInfo is not None:
            loggingInfoType = loggingInfo.find('{http://einfracentral.eu}type')
            if loggingInfoType is not None:
                if loggingInfoType.text == 'audit' and latestAuditInfo is None:
                    newLatestAuditInfo = loggingInfo.__copy__()
                    newLatestAuditInfo.tag = '{http://einfracentral.eu}latestAuditInfo'
                    tree.append(newLatestAuditInfo)
                    break

    for existingLoggingInfo in tree.findall('{http://einfracentral.eu}loggingInfo'):
        tree.remove(existingLoggingInfo)
    allLoggingInfo.sort(key=sort_key)
    for sortedLoggingInfo in allLoggingInfo:
        tree.append(sortedLoggingInfo)

    root.write('output.xml')
    with open("output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)
        if isVersion:
            json_data['resource']['payload'] = json_data['payload']

    return json_data


def sort_key(element):
    date_str = element.find('{http://einfracentral.eu}date').text
    return datetime.utcfromtimestamp(int(date_str) / 1000)
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
datasource_migration(args.path)
######################################################## RUN ###########################################################