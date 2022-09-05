######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
import shutil
######################################################## IMPORTS #######################################################


##################################################### FUNCTIONS ########################################################
def versions_deletion(directory):
    allDumpFolders = ['/catalogue/', '/event/', '/infra_service/', '/pending_provider/', '/pending_service/',
                      '/provider/', '/vocabulary/', '/vocabulary_curation/']
    serviceRelatedFolders = ['/pending_service/', '/infra_service/']
    count = 0
    for resourceFolder in allDumpFolders:
        for file in os.listdir(directory + resourceFolder):
            if file.endswith('.json'):
                if serviceRelatedFolders.__contains__(resourceFolder):
                    with open(directory + resourceFolder + file, 'r') as json_file:
                        coreId, serviceId = find_all_versions(json_file)
                        if coreId is not None and serviceId is not None:
                            os.remove(directory + resourceFolder + file)
                            count = count + 1
            else:
                try:
                    # remove version folders
                    print("Deleting .version file", file)
                    shutil.rmtree(directory + resourceFolder + file)
                except OSError as e:
                    print("Error: %s - %s." % (e.filename, e.strerror))
    print("Total old versioned Services deleted:", count)


def find_all_versions(json_file):
    json_data = json.load(json_file)
    xml = json_data['payload']
    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    service = root.find('{http://einfracentral.eu}service')

    latest = root.find('{http://einfracentral.eu}latest')
    if latest is not None:
        if latest.text == 'false':
            service_id = service.find('{http://einfracentral.eu}id')
            if service_id is not None:
                return json_data.get("id"), service_id.text

    return None, None
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
versions_deletion(args.path)
######################################################## RUN ###########################################################