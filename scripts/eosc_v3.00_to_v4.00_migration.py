######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import SubElement
import os
from bs4 import BeautifulSoup as bs
import argparse
######################################################## IMPORTS #######################################################


##################################################### FUNCTIONS ########################################################
def provider_migration(directory):
    migrationFolders = ['/provider/', '/pending_provider/']
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                isVersion = False
                with open(directory + migrationFolder + file, 'r') as json_file:
                    json_data = migrate_providers(json_file, isVersion)
                    # write to file
                    with open(directory + migrationFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
            if file.endswith('-version'):
                isVersion = True
                versionFiles = os.listdir(directory + migrationFolder + file)
                for versionFile in versionFiles:
                    with open(directory + migrationFolder + file + '/' + versionFile, 'r') as json_file:
                        json_data = migrate_providers(json_file, isVersion)
                        # write to file
                        with open(directory + migrationFolder + file + '/' + versionFile, 'w') as json_file:
                            json.dump(json_data, json_file, indent=2)

def migrate_providers(json_file, isVersion):
    json_data = json.load(json_file)
    xml = json_data['payload']

    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    provider = root.find('{http://einfracentral.eu}provider')

    # catalogueId
    catalogueId = provider.find('{http://einfracentral.eu}catalogueId')
    if catalogueId is None:
        newCatalogueId = ET.Element("tns:catalogueId")
        newCatalogueId.text = 'eosc'
        provider.append(newCatalogueId)

    # multimedia
    multimediaEntries = []
    providerMultimedia = provider.find('{http://einfracentral.eu}multimedia')
    if providerMultimedia is not None:
        for entry in providerMultimedia:
            if entry is not None:
                multimediaEntries.append(entry.text)
        provider.remove(providerMultimedia)
    multimedia = ET.Element("tns:multimedia")
    if multimediaEntries:
        enum = 1
        for entry in multimediaEntries:
            multimediaChild = SubElement(multimedia, 'tns:multimedia')
            multimediaURL = SubElement(multimediaChild, 'tns:multimediaURL')
            multimediaURL.text = entry
            multimediaName = SubElement(multimediaChild, 'tns:multimediaName')
            multimediaName.text = 'Multimedia ' + str(enum)
            enum = enum + 1
    provider.append(multimedia)

    # hosting legal entity
    # hostingLegalEntity = provider.find('{http://einfracentral.eu}hostingLegalEntity')
    # if hostingLegalEntity is not None:
    #     hostingLegalEntity.text = 'provider_hosting_legal_entity-tbd'

    root.write('output.xml')
    with open("output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)
        if isVersion:
            json_data['resource']['payload'] = json_data['payload']

    return json_data


def service_migration(directory):
    migrationFolders = ['/infra_service/', '/pending_service/']
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                isVersion = False
                with open(directory + migrationFolder + file, 'r') as json_file:
                    json_data = migrate_services(json_file, isVersion)
                    # write to file
                    with open(directory + migrationFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
            if file.endswith('-version'):
                isVersion = True
                versionFiles = os.listdir(directory + migrationFolder + file)
                for versionFile in versionFiles:
                    with open(directory + migrationFolder + file + '/' + versionFile, 'r') as json_file:
                        json_data = migrate_services(json_file, isVersion)
                        # write to file
                        with open(directory + migrationFolder + file + '/' + versionFile, 'w') as json_file:
                            json.dump(json_data, json_file, indent=2)


def migrate_services(json_file, isVersion):
    json_data = json.load(json_file)
    xml = json_data['payload']

    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    service = root.find('{http://einfracentral.eu}service')

    # catalogueId
    catalogueId = service.find('{http://einfracentral.eu}catalogueId')
    if catalogueId is None:
        newCatalogueId = ET.Element("tns:catalogueId")
        newCatalogueId.text = 'eosc'
        service.append(newCatalogueId)

    # abbreviation
    serviceName = service.find('{http://einfracentral.eu}name')
    abbreviation = ET.Element("tns:abbreviation")
    if serviceName is not None:
        if serviceName.text is not None:
            if len(serviceName.text) < 30:
                abbreviation.text = serviceName.text
            else:
                words = serviceName.text.split()
                letters = [word[0] for word in words]
                abbreviation.text = "".join(letters)
    service.append(abbreviation)

    # serviceLevel
    serviceName = service.find('{http://einfracentral.eu}serviceLevel')
    if serviceName is not None:
        serviceName.tag = 'resourceLevel'

    # multimedia
    multimediaEntries = []
    serviceMultimedia = service.find('{http://einfracentral.eu}multimedia')
    if serviceMultimedia is not None:
        for entry in serviceMultimedia:
            if entry is not None:
                multimediaEntries.append(entry.text)
        service.remove(serviceMultimedia)
    multimedia = ET.Element("tns:multimedia")
    if multimediaEntries:
        enum = 1
        for entry in multimediaEntries:
            multimediaChild = SubElement(multimedia, 'tns:multimedia')
            multimediaURL = SubElement(multimediaChild, 'tns:multimediaURL')
            multimediaURL.text = entry
            multimediaName = SubElement(multimediaChild, 'tns:multimediaName')
            multimediaName.text = 'Multimedia ' + str(enum)
            enum = enum + 1
    service.append(multimedia)

    # use cases
    useCaseEntries = []
    serviceUseCases = service.find('{http://einfracentral.eu}useCases')
    if serviceUseCases is not None:
        for entry in serviceUseCases:
            if entry is not None:
                useCaseEntries.append(entry.text)
        service.remove(serviceUseCases)
    useCases = ET.Element("tns:useCases")
    if useCaseEntries:
        enum = 1
        for entry in useCaseEntries:
            useCaseChild = SubElement(useCases, 'tns:useCase')
            useCaseURL = SubElement(useCaseChild, 'tns:useCaseURL')
            useCaseURL.text = entry
            useCaseName = SubElement(useCaseChild, 'tns:useCaseName')
            useCaseName.text = 'Use Case ' + str(enum)
            enum = enum + 1
    service.append(useCases)

    # related platforms
    # serviceRelatedPlatforms = service.find('{http://einfracentral.eu}relatedPlatforms')
    # if serviceRelatedPlatforms is not None:
    #     for entry in serviceRelatedPlatforms:
    #         entry.text = 'related_platform-tbd'

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
parser.add_argument("-p", "--path", help="Run command 'python3 eosc_v3.00_to_v4.00_migration.py' --path [path/to/folder]",
                    type=str, required=True)
args = parser.parse_args()
provider_migration(args.path)
service_migration(args.path)
######################################################## RUN ###########################################################