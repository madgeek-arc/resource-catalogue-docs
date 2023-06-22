######################################################## IMPORTS #######################################################
import os
from dotenv import load_dotenv
import requests
import json
import argparse
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs
import uuid
######################################################## IMPORTS #######################################################


###################################################### PROPERTIES ######################################################
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, 'properties.env'))
username = os.getenv('PID_USERNAME')
key = os.getenv('PID_KEY')
auth = os.getenv('PID_AUTH')
prefix = os.getenv('PID_PREFIX')
api = os.getenv('PID_API')
###################################################### PROPERTIES ######################################################


##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    migrationFolders = ['service/']
    # migrationFolders = ['catalogue/', 'provider/', 'service/', 'datasource/', 'training_resource/',
    #                     'interoperability_record/']
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                isVersion = False
                with open(directory + migrationFolder + file, 'r') as json_file:
                    json_data = migrate(json_file, isVersion, migrationFolder.replace("/", ""))
                    # write to file
                    with open(directory + migrationFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
            if file.endswith('-version'):
                isVersion = True
                versionFiles = os.listdir(directory + migrationFolder + file)
                for versionFile in versionFiles:
                    with open(directory + migrationFolder + file + '/' + versionFile, 'r') as json_file:
                        json_data = migrate(json_file, isVersion, migrationFolder.replace("/", ""))
                        # write to file
                        with open(directory + migrationFolder + file + '/' + versionFile, 'w') as json_file:
                            json.dump(json_data, json_file, indent=2)

def migrate(json_file, isVersion, resourceType):
    global resource
    isPublic = False
    json_data = json.load(json_file)
    xml = json_data['payload']
    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    tree = root.getroot()

    # get resource ID from resource type
    match resourceType:
        case "catalogue":
            resource = root.find('{http://einfracentral.eu}catalogue')
        case "provider":
            resource = root.find('{http://einfracentral.eu}provider')
        case "service":
            resource = root.find('{http://einfracentral.eu}service')
        case "datasource":
            resource = root.find('{http://einfracentral.eu}datasource')
        case "training_resource":
            resource = root.find('{http://einfracentral.eu}training_resource')
        case "interoperability_record":
            resource = root.find('{http://einfracentral.eu}interoperability_record')
    resourceId = resource.find('{http://einfracentral.eu}id')
    identifiers = root.find('{http://einfracentral.eu}identifiers')
    if identifiers is not None:
        originalId = identifiers.find('{http://einfracentral.eu}originalId')
        if originalId is not None:
            isPublic = True  # USE IT IF WE NEED DIFFERENT STRATEGY FOR PUBLIC ENTITIES
        alternativeIdentifiers = identifiers.find('{http://einfracentral.eu}alternativeIdentifiers')
        if alternativeIdentifiers is not None:
            create_alternative_identifier(alternativeIdentifiers, resourceId)
        else:
            newAlternativeIdentifiers = ET.Element("tns:alternativeIdentifiers")
            create_alternative_identifier(newAlternativeIdentifiers, resourceId)
            identifiers.append(newAlternativeIdentifiers)
    else:
        newIdentifiers = ET.Element("tns:identifiers")
        newAlternativeIdentifiers = ET.Element("tns:alternativeIdentifiers")
        create_alternative_identifier(newAlternativeIdentifiers, resourceId)
        newIdentifiers.append(newAlternativeIdentifiers)
        tree.append(newIdentifiers)

    root.write('output.xml')
    with open("output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)
        if isVersion:
            json_data['resource']['payload'] = json_data['payload']

    return json_data

def create_alternative_identifier(alternativeIdentifiers, resourceId):
    newAlternativeIdentifier = ET.Element("tns:alternativeIdentifier")
    alternativeIdentifierType = ET.Element("tns:type")
    alternativeIdentifierType.text = "PID"
    alternativeIdentifierValue = ET.Element("tns:value")
    alternativeIdentifierValue.text = create_pid(resourceId)
    newAlternativeIdentifier.append(alternativeIdentifierType)
    newAlternativeIdentifier.append(alternativeIdentifierValue)
    alternativeIdentifiers.append(newAlternativeIdentifier)

def create_pid(resourceId):
    pid = str(uuid.uuid4())  # DECIDE PID CREATION STRATEGY
    print(pid)
    url = api + prefix + "/" + pid

    payload = json.dumps({
      "values": [
        {
          "index": 100,
          "type": "HS_ADMIN",
          "data": {
            "value": {
              "index": 301,
              "handle": prefix + "/" + username,
              # [create hdl,delete hdl,read val,modify val,del val,add val,modify admin,del admin,add admin]
              "permissions": "011111110011",
              "format": "admin"
            },
            "format": "admin"
          }
        },
        {
          "index": 1,
          "type": "id",
          "data": resourceId.text
        }
        # WE CAN ALSO ADD THE RESOURCE'S URL AS A VALUE
      ]
    })
    headers = {
      'Content-Type': 'application/json',
      'Authorization': auth
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    print(payload)
    print(response)
    return pid
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
folder_selection(args.path)
######################################################## RUN ###########################################################