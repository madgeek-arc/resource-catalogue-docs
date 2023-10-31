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
otherFolders = ['/provider/', '/training_resource/', '/interoperability_record/']
###################################################### GLOBALS #########################################################

##################################################### FUNCTIONS ########################################################
def datasource_migration(directory):
    for file in os.listdir(args.path + datasourceFolder):
        if file.endswith('.json'):
            isVersion = False
            with open(directory + datasourceFolder + file, 'r') as json_file:
                json_data = migrate_datasources(json_file, isVersion)
                # write to file
                with open(directory + datasourceFolder + file, 'w') as json_file:
                    json.dump(json_data, json_file, indent=2)
        if file.endswith('-version'):
            isVersion = True
            versionFiles = os.listdir(directory + datasourceFolder + file)
            for versionFile in versionFiles:
                with open(directory + datasourceFolder + file + '/' + versionFile, 'r') as json_file:
                    json_data = migrate_datasources(json_file, isVersion)
                    # write to file
                    with open(directory + datasourceFolder + file + '/' + versionFile, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)


def other_resources_migration(directory):
    for otherFolder in otherFolders:
        for file in os.listdir(args.path + otherFolder):
            if file.endswith('.json'):
                isVersion = False
                with open(directory + otherFolder + file, 'r') as json_file:
                    json_data = migrate_other_resources(json_file, otherFolder.replace("/", ""), isVersion)
                    # write to file
                    with open(directory + otherFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
            if file.endswith('-version'):
                isVersion = True
                versionFiles = os.listdir(directory + otherFolder + file)
                for versionFile in versionFiles:
                    with open(directory + otherFolder + file + '/' + versionFile, 'r') as json_file:
                        json_data = migrate_other_resources(json_file, otherFolder.replace("/", ""), isVersion)
                        # write to file
                        with open(directory + otherFolder + file + '/' + versionFile, 'w') as json_file:
                            json.dump(json_data, json_file, indent=2)

def service_migration(directory):
    for file in os.listdir(directory + serviceFolder):
        if file.endswith('.json'):
            isVersion = False
            with open(directory + serviceFolder + file, 'r') as json_file:
                json_data = migrate_services(json_file, isVersion)
                # write to file
                with open(directory + serviceFolder + file, 'w') as json_file:
                    json.dump(json_data, json_file, indent=2)
        if file.endswith('-version'):
            isVersion = True
            versionFiles = os.listdir(directory + serviceFolder + file)
            for versionFile in versionFiles:
                with open(directory + serviceFolder + file + '/' + versionFile, 'r') as json_file:
                    json_data = migrate_services(json_file, isVersion)
                    # write to file
                    with open(directory + serviceFolder + file + '/' + versionFile, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)


def migrate_datasources(json_file, isVersion):
    json_data = json.load(json_file)
    xml = json_data['payload']
    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    datasource = root.find('{http://einfracentral.eu}datasource')

    # prefill DatasourceIDs to migrate Service's serviceCategory later
    if not isVersion:
        datasourceId = datasource.find('{http://einfracentral.eu}id')
        if datasourceId is not None:
            if datasourceId.text not in datasourceIds:
                datasourceIds.append(datasourceId.text)

    # alternativeIdentifiers
    identifiers = root.find('{http://einfracentral.eu}identifiers')
    if identifiers is not None:
        alternativeIdentifiers = identifiers.find('{http://einfracentral.eu}alternativeIdentifiers')
        if alternativeIdentifiers is not None:
            for alternativeIdentifier in alternativeIdentifiers:
                alternativeIdentifierValue = alternativeIdentifier.find('{http://einfracentral.eu}value')
                if alternativeIdentifierValue is not None:
                    originalOpenAIREId = ET.Element("tns:originalOpenAIREId")
                    originalOpenAIREId.text = alternativeIdentifierValue.text
                    datasource.append(originalOpenAIREId)
                    break
            identifiers.remove(alternativeIdentifiers)

    root.write('output.xml')
    with open("../EOSCProfilev4.08_M30Release/output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)
        if isVersion:
            json_data['resource']['payload'] = json_data['payload']


def migrate_other_resources(json_file, resourceType, isVersion):
    global resource
    json_data = json.load(json_file)
    xml = json_data['payload']
    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    match resourceType:
        case "provider":
            resource = root.find('{http://einfracentral.eu}provider')
        case "training_resource":
            resource = root.find('{http://einfracentral.eu}trainingResource')
        case "interoperability_record":
            resource = root.find('{http://einfracentral.eu}interoperabilityRecord')
    migrate_alternative_identifiers(root, resource)

    root.write('output.xml')
    with open("../EOSCProfilev4.08_M30Release/output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)
        if isVersion:
            json_data['resource']['payload'] = json_data['payload']

    return json_data


def migrate_services(json_file, isVersion):
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

    # marketplaceLocation field / remove ResourceExtras -> researchCategories
    marketplaceLocations = ET.Element("tns:marketplaceLocations")
    resourceExtras = root.find('{http://einfracentral.eu}resourceExtras')
    if resourceExtras is not None:
        researchCategories = resourceExtras.find('{http://einfracentral.eu}researchCategories')
        if researchCategories is not None:
            for researchCategory in researchCategories:
                if researchCategory is not None:
                    marketplaceLocation = ET.Element("tns:marketplaceLocation")
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
        resourceExtras.remove(researchCategories)
    service.append(marketplaceLocations)

    # horizontalService / remove ResourceExtras -> horizontalService
    horizontalService = ET.Element("tns:horizontalService")
    if resourceExtras is not None:
        existingHorizontalService = resourceExtras.find('{http://einfracentral.eu}horizontalService')
        if existingHorizontalService is not None:
            horizontalService.text = existingHorizontalService.text
    service.append(horizontalService)
    resourceExtras.remove(horizontalService)

    # alternativeIdentifiers
    migrate_alternative_identifiers(root, service)

    root.write('output.xml')
    with open("../EOSCProfilev4.08_M30Release/output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)
        if isVersion:
            json_data['resource']['payload'] = json_data['payload']

    return json_data


def migrate_alternative_identifiers(root, resource):
    # alternativeIdentifiers
    identifiers = root.find('{http://einfracentral.eu}identifiers')
    if identifiers is not None:
        alternativeIdentifiers = identifiers.find('{http://einfracentral.eu}alternativeIdentifiers')
        if alternativeIdentifiers is not None:
            for alternativeIdentifier in alternativeIdentifiers:
                if alternativeIdentifier is not None:
                    alternativeIdentifierType = alternativeIdentifier.find('{http://einfracentral.eu}type')
                    if alternativeIdentifierType.text == 'PID':
                        alternativeIdentifierType.text = 'EOSC PID'
        resource.append(alternativeIdentifiers.__copy__())
        identifiers.remove(alternativeIdentifiers)
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
datasource_migration(args.path)
other_resources_migration(args.path)
service_migration(args.path)
######################################################## RUN ###########################################################