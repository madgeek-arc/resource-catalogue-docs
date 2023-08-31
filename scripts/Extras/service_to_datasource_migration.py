######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
######################################################## IMPORTS #######################################################

##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    for file in os.listdir(directory):
        if file.endswith('.json'):
            isVersion = False
            with open(directory + file, 'r') as json_file:
                json_data = migrate(json_file, isVersion)
                # write to file
                with open(directory + file, 'w') as json_file:
                    json.dump(json_data, json_file, indent=2)
        if file.endswith('-version'):
            isVersion = True
            versionFiles = os.listdir(directory + file)
            for versionFile in versionFiles:
                with open(directory + file + '/' + versionFile, 'r') as json_file:
                    json_data = migrate(json_file, isVersion)
                    # write to file
                    with open(directory + file + '/' + versionFile, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)

def migrate(json_file, isVersion):
    json_data = json.load(json_file)
    xml = json_data['payload']
    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))

    # change resourceType
    json_data['resourceTypeName'] = 'datasource'
    if isVersion:
        json_data["resource"]["resourceTypeName"] = "datasource"

    # serviceBundle -> datasourceBundle / service -> datasource
    root.getroot().tag = "{http://einfracentral.eu}datasourceBundle"
    service = root.find('{http://einfracentral.eu}service')
    service.tag = '{http://einfracentral.eu}datasource'

    # serviceType
    resourceExtras = root.find('{http://einfracentral.eu}resourceExtras')
    if resourceExtras is not None:
        serviceType = resourceExtras.find('{http://einfracentral.eu}serviceType')
        if serviceType is not None:
            serviceType.text = 'service_type-datasource'

    ## MANDATORY FIELDS ##

    # jurisdiction field
    jurisdiction = ET.Element("tns:jurisdiction")
    jurisdiction.text = "ds_jurisdiction-global"

    # datasourceClassification field
    datasourceClassification = ET.Element("tns:datasourceClassification")
    datasourceClassification.text = "ds_classification-aggregators"

    # researchEntityTypes field
    researchEntityTypes = ET.Element("tns:researchEntityTypes")
    researchEntityType1 = ET.Element("tns:researchEntityType")
    researchEntityType1.text = "ds_research_entity_type-research_publication"
    researchEntityType2 = ET.Element("tns:researchEntityType")
    researchEntityType2.text = "ds_research_entity_type-research_data"
    researchEntityType3 = ET.Element("tns:researchEntityType")
    researchEntityType3.text = "ds_research_entity_type-research_software"
    researchEntityTypes.append(researchEntityType1)
    researchEntityTypes.append(researchEntityType2)
    researchEntityTypes.append(researchEntityType3)

    # thematic field
    thematic = ET.Element("tns:thematic")
    thematic.text = "false"

    service.append(jurisdiction)
    service.append(datasourceClassification)
    service.append(researchEntityTypes)
    service.append(thematic)


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