######################################################## Changes #######################################################
# ServiceBundle -> added "status", "resourceExtras" (previously on ResourceBundle)
# Datasource -> added "serviceId", "catalogueId"
# DatasourceBundle -> added "datasourceStatus", removed "status", "resourceExtras"

# Strategy -> each Datasource json file to be split into 2 different json files (1 Service and 1 Datasource)

      # NO NEED TO KEEP VERSION FOLDERS, MAKES IT MORE COMPLICATED WITH FILE/FOLDER RENAMES AND PARENT IDS #

######################################################## Changes #######################################################

######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
from distutils.dir_util import copy_tree
import uuid
from unidecode import unidecode  # removes accents
######################################################## IMPORTS #######################################################

##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    global isVersion

    # existing Datasoure folder. Its contents will be updated according to the new Datasource object
    datasourceFolder = '/datasource/'
    # existing Datasoure folder (copy). Its contents will be updated to Services
    serviceFolder = '/datasource_to_service/'
    copy_tree(directory + datasourceFolder, directory + serviceFolder)

    # Migrate Datasources
    for file in os.listdir(directory + datasourceFolder):
        if file.endswith('.json'):
            isVersion = False
            with open(directory + datasourceFolder + file, 'r') as json_file:
                data = migrate_to_datasource(json_file, isVersion)
                json_data = data[0]
                # write to file
                with open(directory + datasourceFolder + file, 'w') as json_file:
                    json.dump(json_data, json_file, indent=2)
        if file.endswith('-version'):
            isVersion = True
            versionFiles = os.listdir(directory + datasourceFolder + file)
            for versionFile in versionFiles:
                with open(directory + datasourceFolder + file + '/' + versionFile, 'r') as json_file:
                    data = migrate_to_datasource(json_file, isVersion)
                    json_data = data[0]
                    # write to file
                    with open(directory + datasourceFolder + file + '/' + versionFile, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
                # JSON files rename
                os.rename(directory + datasourceFolder + file + '/' + versionFile,
                          directory + datasourceFolder + file + '/' + data[1])
        if not isVersion:
            # print("Rename Version Folder for " + file + " to " + data[1])
            os.rename(directory + datasourceFolder + file, directory + datasourceFolder + data[1])

    # Migrate Services
    for file in os.listdir(directory + serviceFolder):
        if file.endswith('.json'):
            isVersion = False
            with open(directory + serviceFolder + file, 'r') as json_file:
                json_data = migrate_to_service(json_file, isVersion)
                # write to file
                with open(directory + serviceFolder + file, 'w') as json_file:
                    json.dump(json_data, json_file, indent=2)
        if file.endswith('-version'):
            isVersion = True
            versionFiles = os.listdir(directory + serviceFolder + file)
            for versionFile in versionFiles:
                with open(directory + serviceFolder + file + '/' + versionFile, 'r') as json_file:
                    json_data = migrate_to_service(json_file, isVersion)
                    # write to file
                    with open(directory + serviceFolder + file + '/' + versionFile, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)

def migrate_to_datasource(json_file, isVersion):
    json_data = json.load(json_file)
    xml = json_data['payload']
    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    tree = root.getroot()

    datasource = root.find('{http://einfracentral.eu}datasource')

    # migrate status to datasourceStatus
    status = root.find('{http://einfracentral.eu}status')
    if status is not None:
        match status.text:
            case "approved resource":
                status.text = "approved datasource"
            case "rejected resource":
                status.text = "rejected datasource"
            case "pending resource":
                status.text = "pending datasource"

    # remove resourceExtras field
    resourceExtras = root.find('{http://einfracentral.eu}resourceExtras')
    if resourceExtras is not None:
        tree.remove(resourceExtras)

    # remove identifiers field
    identifiers = root.find('{http://einfracentral.eu}identifiers')
    if identifiers is not None:
        tree.remove(identifiers)

    # create Datasource ID
    id = datasource.find('{http://einfracentral.eu}id')
    if id is not None:
        if id.text is not None:
            id.text = create_new_id()

    # create Service ID (concerning the Service ID creation process)
    abbreviation = datasource.find('{http://einfracentral.eu}abbreviation')
    resourceOrganisation = datasource.find('{http://einfracentral.eu}resourceOrganisation')
    serviceId = ET.Element("tns:serviceId")
    if abbreviation is not None and resourceOrganisation is not None:
        if abbreviation.text is not None and resourceOrganisation.text is not None:
            serviceId.text = format_string(resourceOrganisation.text, abbreviation.text)
    datasource.append(serviceId)

    # migrate catalogueId
    # same field name no need to do anything

    # delete Service related fields
    name = datasource.find('{http://einfracentral.eu}name')
    resourceProviders = datasource.find('{http://einfracentral.eu}resourceProviders')
    webpage = datasource.find('{http://einfracentral.eu}webpage')
    description = datasource.find('{http://einfracentral.eu}description')
    tagline = datasource.find('{http://einfracentral.eu}tagline')
    logo = datasource.find('{http://einfracentral.eu}logo')
    multimedia = datasource.find('{http://einfracentral.eu}multimedia')
    useCases = datasource.find('{http://einfracentral.eu}useCases')
    scientificDomains = datasource.find('{http://einfracentral.eu}scientificDomains')
    categories = datasource.find('{http://einfracentral.eu}categories')
    targetUsers = datasource.find('{http://einfracentral.eu}targetUsers')
    accessTypes = datasource.find('{http://einfracentral.eu}accessTypes')
    accessModes = datasource.find('{http://einfracentral.eu}accessModes')
    tags = datasource.find('{http://einfracentral.eu}tags')
    geographicalAvailabilities = datasource.find('{http://einfracentral.eu}geographicalAvailabilities')
    languageAvailabilities = datasource.find('{http://einfracentral.eu}languageAvailabilities')
    resourceGeographicLocations = datasource.find('{http://einfracentral.eu}resourceGeographicLocations')
    mainContact = datasource.find('{http://einfracentral.eu}mainContact')
    publicContacts = datasource.find('{http://einfracentral.eu}publicContacts')
    helpdeskEmail = datasource.find('{http://einfracentral.eu}helpdeskEmail')
    securityContactEmail = datasource.find('{http://einfracentral.eu}securityContactEmail')
    trl = datasource.find('{http://einfracentral.eu}trl')
    lifeCycleStatus = datasource.find('{http://einfracentral.eu}lifeCycleStatus')
    certifications = datasource.find('{http://einfracentral.eu}certifications')
    standards = datasource.find('{http://einfracentral.eu}standards')
    openSourceTechnologies = datasource.find('{http://einfracentral.eu}openSourceTechnologies')
    version = datasource.find('{http://einfracentral.eu}version')
    lastUpdate = datasource.find('{http://einfracentral.eu}lastUpdate')
    changeLog = datasource.find('{http://einfracentral.eu}changeLog')
    requiredResources = datasource.find('{http://einfracentral.eu}requiredResources')
    relatedResources = datasource.find('{http://einfracentral.eu}relatedResources')
    relatedPlatforms = datasource.find('{http://einfracentral.eu}relatedPlatforms')
    fundingBody = datasource.find('{http://einfracentral.eu}fundingBody')
    fundingPrograms = datasource.find('{http://einfracentral.eu}fundingPrograms')
    grantProjectNames = datasource.find('{http://einfracentral.eu}grantProjectNames')
    helpdeskPage = datasource.find('{http://einfracentral.eu}helpdeskPage')
    userManual = datasource.find('{http://einfracentral.eu}userManual')
    termsOfUse = datasource.find('{http://einfracentral.eu}termsOfUse')
    privacyPolicy = datasource.find('{http://einfracentral.eu}privacyPolicy')
    accessPolicy = datasource.find('{http://einfracentral.eu}accessPolicy')
    resourceLevel = datasource.find('{http://einfracentral.eu}resourceLevel')
    trainingInformation = datasource.find('{http://einfracentral.eu}trainingInformation')
    statusMonitoring = datasource.find('{http://einfracentral.eu}statusMonitoring')
    maintenance = datasource.find('{http://einfracentral.eu}maintenance')
    orderType = datasource.find('{http://einfracentral.eu}orderType')
    order = datasource.find('{http://einfracentral.eu}order')
    paymentModel = datasource.find('{http://einfracentral.eu}paymentModel')
    pricing = datasource.find('{http://einfracentral.eu}pricing')
    fields = [abbreviation, name, resourceOrganisation, resourceProviders, webpage, description, tagline, logo,
              multimedia, useCases, scientificDomains, categories, targetUsers, accessTypes, accessModes, tags,
              geographicalAvailabilities, languageAvailabilities, resourceGeographicLocations, mainContact,
              publicContacts, helpdeskEmail, securityContactEmail, trl, lifeCycleStatus, certifications, standards,
              openSourceTechnologies, version, lastUpdate, changeLog, requiredResources, relatedResources,
              relatedPlatforms, fundingBody, fundingPrograms, grantProjectNames, helpdeskPage, userManual, termsOfUse,
              privacyPolicy, accessPolicy, resourceLevel, trainingInformation, statusMonitoring, maintenance, orderType,
              order, paymentModel, pricing]
    remove_service_related_fields(datasource, fields)

    # change core ID
    newCoreId = create_new_id()
    oldCoreId = json_data['id']
    json_data['id'] = newCoreId
    if isVersion:
        json_data["resource"]["id"] = newCoreId
        # print("After the execution .json file and -version folder names must change from", oldCoreId, "to", newCoreId)
    # else:
        # print("After the execution .json file must change from", oldCoreId, "to", newCoreId)

    root.write('output.xml')
    with open("output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)
        if isVersion:
            json_data['resource']['payload'] = json_data['payload']

    return json_data, newCoreId+'.json'

def migrate_to_service(json_file, isVersion):
    json_data = json.load(json_file)
    xml = json_data['payload']
    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))

    datasource = root.find('{http://einfracentral.eu}datasource')

    # delete Datasource related fields
    submissionPolicyURL = datasource.find('{http://einfracentral.eu}submissionPolicyURL')
    preservationPolicyURL = datasource.find('{http://einfracentral.eu}preservationPolicyURL')
    versionControl = datasource.find('{http://einfracentral.eu}versionControl')
    persistentIdentitySystems = datasource.find('{http://einfracentral.eu}persistentIdentitySystems')
    jurisdiction = datasource.find('{http://einfracentral.eu}jurisdiction')
    datasourceClassification = datasource.find('{http://einfracentral.eu}datasourceClassification')
    researchEntityTypes = datasource.find('{http://einfracentral.eu}researchEntityTypes')
    thematic = datasource.find('{http://einfracentral.eu}thematic')
    researchProductLicensings = datasource.find('{http://einfracentral.eu}researchProductLicensings')
    researchProductAccessPolicies = datasource.find('{http://einfracentral.eu}researchProductAccessPolicies')
    researchProductMetadataLicensing = datasource.find('{http://einfracentral.eu}researchProductMetadataLicensing')
    researchProductMetadataAccessPolicies = datasource.find('{http://einfracentral.eu}researchProductMetadataAccessPolicies')
    fields = [submissionPolicyURL, preservationPolicyURL, versionControl, persistentIdentitySystems, jurisdiction,
              datasourceClassification, researchEntityTypes, thematic, researchProductLicensings,
              researchProductAccessPolicies, researchProductMetadataLicensing, researchProductMetadataAccessPolicies]
    remove_service_related_fields(datasource, fields)

    # migrate serviceType to Datasource
    resourceExtras = root.find('{http://einfracentral.eu}resourceExtras')
    if resourceExtras is not None:
        serviceType = resourceExtras.find('{http://einfracentral.eu}serviceType')
        if serviceType is not None:
            serviceType.text = 'service_type-service'

    # format ID
    id = datasource.find('{http://einfracentral.eu}id')
    if id is not None:
        abbreviation = datasource.find('{http://einfracentral.eu}abbreviation')
        resourceOrganisation = datasource.find('{http://einfracentral.eu}resourceOrganisation')
        if abbreviation is not None and resourceOrganisation is not None:
            if abbreviation.text is not None and resourceOrganisation.text is not None:
                id.text = format_string(resourceOrganisation.text, abbreviation.text)

    # change Payload's tags
    root.getroot().tag = "{http://einfracentral.eu}serviceBundle"
    datasource.tag = '{http://einfracentral.eu}service'

    # change resourceTypeName
    json_data['resourceTypeName'] = 'service'
    if isVersion:
        json_data["resource"]["resourceTypeName"] = 'service'

    root.write('output.xml')
    with open("output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content)
        if isVersion:
            json_data['resource']['payload'] = json_data['payload']

    return json_data

def create_new_id():
    return str(uuid.uuid4())

def remove_service_related_fields(datasource, fields):
    for field in fields:
        if field is not None:
            datasource.remove(field)

def format_string(provider, serviceId):
    # Remove accents, replace consecutive whitespaces with a single space, strip trailing whitespaces
    formatted_serviceId = unidecode(serviceId).strip().replace("\n", " ").replace("\t", " ").strip()

    # Remove non-alphanumeric characters, replace spaces with underscores, convert to lowercase
    formatted_serviceId = ''.join(c if c.isalnum() or c in [' ', '-', '_'] else '' for c in formatted_serviceId)
    formatted_serviceId = formatted_serviceId.replace(" ", "_").lower()

    return f"{provider}.{formatted_serviceId}"
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
folder_selection(args.path)
######################################################## RUN ###########################################################