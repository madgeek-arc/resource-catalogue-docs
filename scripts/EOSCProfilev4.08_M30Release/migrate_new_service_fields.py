######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
######################################################## IMPORTS #######################################################

###################################################### GLOBALS #########################################################
datasourceIds = []
datasourceFolder = '/datasource/'
serviceFolder = '/service/'
###################################################### GLOBALS #########################################################

##################################################### FUNCTIONS ########################################################
def get_datasource_ids():
    for file in os.listdir(args.path + datasourceFolder):
        if file.endswith('.json'):
            with open(args.path + datasourceFolder + file, 'r') as json_file:
                json_data = json.load(json_file)
                xml = json_data['payload']
                ET.register_namespace("tns", "http://einfracentral.eu")
                root = ET.ElementTree(ET.fromstring(xml))

                datasource = root.find('{http://einfracentral.eu}datasource')
                id = datasource.find('{http://einfracentral.eu}id')
                if id is not None:
                    if id.text not in datasourceIds:
                        datasourceIds.append(id.text)


def folder_selection(directory):
    for file in os.listdir(directory + serviceFolder):
        if file.endswith('.json'):
            isVersion = False
            with open(directory + serviceFolder + file, 'r') as json_file:
                json_data = migrate(json_file, isVersion)
                # write to file
                with open(directory + serviceFolder + file, 'w') as json_file:
                    json.dump(json_data, json_file, indent=2)
        if file.endswith('-version'):
            isVersion = True
            versionFiles = os.listdir(directory + serviceFolder + file)
            for versionFile in versionFiles:
                with open(directory + serviceFolder + file + '/' + versionFile, 'r') as json_file:
                    json_data = migrate(json_file, isVersion)
                    # write to file
                    with open(directory + serviceFolder + file + '/' + versionFile, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)


def migrate(json_file, isVersion):
    json_data = json.load(json_file)
    xml = json_data['payload']
    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    service = root.find('{http://einfracentral.eu}service')
    id = service.find('{http://einfracentral.eu}id')

    # serviceCategory field
    serviceCategories = ET.Element("tns:serviceCategories")
    serviceCategory = ET.Element("tns:serviceCategory")
    if id in datasourceIds:
        serviceCategory.text = "service_category-data_source"
    else:
        categories = service.find('{http://einfracentral.eu}categories')
        if categories is not None:
            for category in categories:
                if category is not None:
                    categoryEntry = category.find('{http://einfracentral.eu}category')
                    if categoryEntry is not None:
                        if categoryEntry.text == "category-access_physical_and_eInfrastructures-compute":
                            serviceCategory.text = "service_category-compute"
                            break
                        elif categoryEntry.text == "category-access_physical_and_eInfrastructures-data_storage":
                            serviceCategory.text = "service_category-storage"
                            break
    if serviceCategory.text is None:
        serviceCategory.text = "service_category-other"
    serviceCategories.append(serviceCategory)
    service.append(serviceCategories)

    # marketplaceLocation field
    marketplaceLocations = ET.Element("tns:marketplaceLocations")
    marketplaceLocation = ET.Element("tns:marketplaceLocation")
    resourceExtras = root.find('{http://einfracentral.eu}resourceExtras')
    if resourceExtras is not None:
        researchCategories = resourceExtras.find('{http://einfracentral.eu}researchCategories')
        if researchCategories is not None:
            for researchCategory in researchCategories:
                if researchCategory is not None:
                    if researchCategory.text == "research_category-dro":
                        marketplaceLocation.text = "marketplace_location-discover_research_outputs"
                    elif researchCategory.text == "research_category-pro":
                        marketplaceLocation.text = "marketplace_location-publish_research_outputs"
                    elif researchCategory.text == "research_category-pa":
                        marketplaceLocation.text = "marketplace_location-process_and_analyze"
                    elif researchCategory.text == "research_category-acr":
                        marketplaceLocation.text = "marketplace_location-access_computing_and_storage_resources"
                    elif researchCategory.text == "research_category-fie":
                        marketplaceLocation.text = "marketplace_location-find_instruments_and_equipment"
                    elif researchCategory.text == "research_category-atm":
                        marketplaceLocation.text = "marketplace_location-access_training_material"
                    elif researchCategory.text == "research_category-ari":
                        marketplaceLocation.text = "marketplace_location-access_research_infrastructures"
                    elif researchCategory.text == "research_category-mrd":
                        marketplaceLocation.text = "marketplace_location-manage_research_data"
    marketplaceLocations.append(marketplaceLocation)
    service.append(marketplaceLocations)

    # horizontalService
    horizontalService = ET.Element("tns:horizontalService")
    resourceExtras = root.find('{http://einfracentral.eu}resourceExtras')
    if resourceExtras is not None:
        existingHorizontalService = root.find('{http://einfracentral.eu}horizontalService')
        if existingHorizontalService is not None:
            horizontalService.text = existingHorizontalService.text
    service.append(horizontalService)

    # alternativeIdentifiers
    identifiers = root.find('{http://einfracentral.eu}identifiers')
    if identifiers is not None:
        alternativeIdentifiers = identifiers.find('{http://einfracentral.eu}alternativeIdentifiers')
        if alternativeIdentifiers is not None:
            for alternativeIdentifier in alternativeIdentifiers:
                if alternativeIdentifier is not None:
                    alternativeIdentifierType = alternativeIdentifier.find('{http://einfracentral.eu}type')
                    if alternativeIdentifierType is not None:
                        if alternativeIdentifierType.text == "openaire":
                            alternativeIdentifiers.remove(alternativeIdentifier)
            service.append(alternativeIdentifiers.__copy__())
            identifiers.remove(alternativeIdentifiers)

    root.write('output.xml')
    with open("../EOSCProfilev4.08_M30Release/output.xml", "r") as xml_file:
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
get_datasource_ids()
folder_selection(args.path)
######################################################## RUN ###########################################################