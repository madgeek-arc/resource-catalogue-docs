######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
import uuid
######################################################## IMPORTS #######################################################


################################################### GLOBAL VARIABLES ###################################################
global directory
servicesToBeTransformedToDatasources = ['aabd83a5-2a60-496a-a029-022027ac5bf9', 'fe9915c7-3cb7-45f1-92f7-c9168ae765c0',
                                        '42ae1a2e-c15d-4225-8d00-7a0f449b2741', '29b302bf-9b00-44b2-b30d-4d7e70bd7d81',
                                        '7a0e74e3-94b0-417d-9170-a203ba6cdf36', '7af25fbb-4814-4448-9dd1-a7333bc1994c',
                                        '4210138b-82b9-45be-8bbf-a28df5ebe2e7', 'd80efcea-89d2-461c-a7c6-36953a239c22',
                                        'e0fadb4e-bdcb-45ea-92cb-bede7076ee73', '947c9ac3-4238-4852-a12f-a14aeb348b0d',
                                        '3a6ebdb2-d716-4384-b352-0a83a0fc448a', '89091014-d6d1-492b-b05f-422d3f491144',
                                        '666442b5-a6b5-4830-9353-056a3929f171', '691f07a5-d33e-451e-b1a4-87eef594ec71',
                                        '28f520c7-254d-46c7-93af-53043ee93563', '2c07d4d2-06df-472f-8cd4-4db4f6e9eee0',
                                        'fb617202-6388-4c47-82b5-6fea57c89263', 'f15c11bc-4eb7-4826-8b6f-627f636d6da6',
                                        '4a061471-9902-4ae2-abe1-a9fc12c00c99', '6183a8e7-ad92-4099-a222-023661f1c401',
                                        'bb96fa65-af9f-4ae3-be2f-cdd4cc3b8900', 'b8198a0d-f284-43a4-ab8a-8cebbc6d5bc9',
                                        '3e16b530-4cef-4267-a4c2-2e63a92848ea', 'cfda12f1-737d-400b-b94d-ccc83e5011e2',
                                        '960e53e2-b2c9-48eb-b936-4da2574bdf71', '427d7afe-c39a-4016-bf22-8baeda200b67']
################################################### GLOBAL VARIABLES ###################################################


##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    migrationFolders = ['/provider/', '/infra_service/']
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                with open(directory + migrationFolder + file, 'r') as json_file:
                    toBePrinted = False
                    migrated_data = migrate(json_file)
                    if migrated_data[1]:
                        if migrated_data[0].get("id") in servicesToBeTransformedToDatasources:
                            print(migrated_data[0].get("id"))
                            toBePrinted = True
                        json_data = update_core_id(migrated_data[0])
                        fileName = json_data.get("id")
                        if (toBePrinted):
                            print(fileName)
                        # write to file
                        with open(directory + migrationFolder + fileName + '.json', 'w') as json_file:
                            json.dump(json_data, json_file, indent=2)


def migrate(json_file):
    json_data = json.load(json_file)
    xml = json_data['payload']

    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    tree = root.getroot()

    # copy to upper level
    service = root.find('{http://einfracentral.eu}service')
    isService = False
    if service is not None:
        isService = True
    active = root.find('{http://einfracentral.eu}active')
    status = root.find('{http://einfracentral.eu}status')
    metadata = root.find('{http://einfracentral.eu}metadata')
    published = metadata.find('{http://einfracentral.eu}published')
    identifiers = root.find('{http://einfracentral.eu}identifiers')
    if isService:
        latest = root.find('{http://einfracentral.eu}latest')
        service = root.find('{http://einfracentral.eu}service')
        id = service.find('{http://einfracentral.eu}id')
        catalogueId = service.find('{http://einfracentral.eu}catalogueId')
    else:
        provider = root.find('{http://einfracentral.eu}provider')
        id = provider.find('{http://einfracentral.eu}id')
        catalogueId = provider.find('{http://einfracentral.eu}catalogueId')
    entered = False
    if active is not None and active.text == 'true':
        if (status is not None and status.text == 'approved provider') or \
                (status is not None and status.text == 'approved resource' and latest is not None and latest.text == 'true'):
            entered = True
            if identifiers is not None:
                originalId = identifiers.find('{http://einfracentral.eu}originalId')
                if originalId is not None:
                    originalId.text = id.text
            else:
                newIdentifier = ET.Element("tns:identifiers")
                tree.append(newIdentifier)
                originalId = ET.Element("tns:originalId")
                originalId.text = id.text
                newIdentifier.append(originalId)
            if id is not None and catalogueId is not None:
                id.text = catalogueId.text+'.'+id.text
            if published is not None:
                published.text = 'true'
            else:
                published = ET.Element("tns:published")
                published.text = 'true'
                metadata.append(published)

    root.write('output.xml')
    with open("output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)

    return json_data, entered


def update_core_id(json_data):
    newId = str(uuid.uuid4())
    updateDict = {"id": newId}
    json_data.update(updateDict)
    return json_data
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
directory = args.path
folder_selection(args.path)
######################################################## RUN ###########################################################