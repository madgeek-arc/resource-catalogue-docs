######################################################## IMPORTS #######################################################
import os
import threading
import time
from dotenv import load_dotenv
import requests
import json
import argparse
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs
import uuid
import hashlib
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
def folder_selection(directory, migrationFolder):
    for file in os.listdir(directory + migrationFolder):
        if file.endswith('.json'):
            isVersion = False
            with open(directory + migrationFolder + file, 'r') as json_file:
                json_data = migrate(json_file, isVersion, migrationFolder.replace("/", ""))
                if json_data is not None:
                    # write to file
                    with open(directory + migrationFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
        if file.endswith('-version'):
            isVersion = True
            versionFiles = os.listdir(directory + migrationFolder + file)
            for versionFile in versionFiles:
                with open(directory + migrationFolder + file + '/' + versionFile, 'r') as json_file:
                    json_data = migrate(json_file, isVersion, migrationFolder.replace("/", ""))
                    if json_data is not None:
                        # write to file
                        with open(directory + migrationFolder + file + '/' + versionFile, 'w') as json_file:
                            json.dump(json_data, json_file, indent=2)
    return  # close thread


def migrate(json_file, isVersion, resourceType):
    global resource
    json_data = json.load(json_file)
    xml = json_data['payload']
    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    tree = root.getroot()

    # continue migration ONLY for Public resources
    metadata = root.find('{http://einfracentral.eu}metadata')
    if metadata is not None:
        published = metadata.find('{http://einfracentral.eu}published')
        if published is not None:
            if published.text == "false":
                return None

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
            resource = root.find('{http://einfracentral.eu}trainingResource')
        case "interoperability_record":
            resource = root.find('{http://einfracentral.eu}interoperabilityRecord')
    resourceId = resource.find('{http://einfracentral.eu}id')
    identifiers = root.find('{http://einfracentral.eu}identifiers')
    if identifiers is not None:
        alternativeIdentifiers = identifiers.find('{http://einfracentral.eu}alternativeIdentifiers')
        if alternativeIdentifiers is not None:
            create_alternative_identifier(alternativeIdentifiers, resourceId.text)
        else:
            newAlternativeIdentifiers = ET.Element("tns:alternativeIdentifiers")
            create_alternative_identifier(newAlternativeIdentifiers, resourceId.text)
            identifiers.append(newAlternativeIdentifiers)
    else:
        newIdentifiers = ET.Element("tns:identifiers")
        newAlternativeIdentifiers = ET.Element("tns:alternativeIdentifiers")
        create_alternative_identifier(newAlternativeIdentifiers, resourceId.text)
        newIdentifiers.append(newAlternativeIdentifiers)
        tree.append(newIdentifiers)

    root.write(resourceType + '-output.xml')
    with open(resourceType + "-output.xml", "r") as xml_file:
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


def generate_short_hash(input_str):
    try:
        # Create MD5 hash instance
        md = hashlib.md5()

        # Generate hash value for the input string
        md.update(input_str.encode())
        hash_bytes = md.digest()

        # Convert byte array to a hexadecimal string
        hash_str = ''.join(format(byte, '02x') for byte in hash_bytes)

        # Return the first 8 characters of the hash string
        return hash_str[:8]
    except:
        # Handle algorithm not found exception
        print("An error occurred during hash generation. Generating UUID4 instead" + input_str)
        return str(uuid.uuid4())


def create_pid(resourceId):
    pid = generate_short_hash(resourceId)
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
          "data": resourceId
        }
        # WE CAN ALSO ADD THE RESOURCE'S URL AS A VALUE
      ]
    })

    headers = {
      'Content-Type': 'application/json',
      'Authorization': auth
    }

    response = requests.request("PUT", url, headers=headers, data=payload)
    if response.status_code != 200 and response.status_code != 201:
        print(response.status_code)
    return pid


def create_threads(directory):
    start = time.process_time()
    print("Starting at:", start)
    migrationFolders = ['provider/', 'service/', 'datasource/', 'training_resource/', 'interoperability_record/']
    t1 = threading.Thread(target=folder_selection, args=(directory, migrationFolders[0]))
    t2 = threading.Thread(target=folder_selection, args=(directory, migrationFolders[1]))
    t3 = threading.Thread(target=folder_selection, args=(directory, migrationFolders[2]))
    t4 = threading.Thread(target=folder_selection, args=(directory, migrationFolders[3]))
    t5 = threading.Thread(target=folder_selection, args=(directory, migrationFolders[4]))
    threads = [t1, t2, t3, t4, t5]
    start_multithreading_execution(threads, start)


def start_multithreading_execution(threads, start):
    for thread in threads:
        thread.start()
    check_if_threads_have_finished(threads, start)


def check_if_threads_have_finished(threads, start):
    finished_threads = []
    while any(thread.is_alive() for thread in threads):
        for i, thread in enumerate(threads):
            if not thread.is_alive() and thread not in finished_threads:
                finished_threads.append(thread)
                if i == 0:
                    print("Provider thread has finished at", time.process_time() - start)
                elif i == 1:
                    print("Service thread has finished at", time.process_time() - start)
                elif i == 2:
                    print("Datasource thread has finished at", time.process_time() - start)
                elif i == 3:
                    print("Training Resource thread has finished at", time.process_time() - start)
                elif i == 4:
                    print("Interoperability Record thread has finished at", time.process_time() - start)

    print("All threads have finished at", time.process_time() - start)
    return
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
create_threads(args.path)
######################################################## RUN ###########################################################
