######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
######################################################## IMPORTS #######################################################

##################################################### FUNCTIONS ########################################################
headers = {}

def folder_selection(directory):
    for file in os.listdir(directory):
        if file.endswith('.json'):
            isVersion = False
            with open(directory + '/' + file, 'r') as json_file:
                json_data = migrate(json_file, isVersion)
                # write to file
                with open(directory + '/' + file, 'w') as json_file:
                    json.dump(json_data, json_file, indent=2)
        if file.endswith('-version'):
            isVersion = True
            versionFiles = os.listdir(directory + '/' + file)
            for versionFile in versionFiles:
                with open(directory + '/' + file + '/' + versionFile, 'r') as json_file:
                    json_data = migrate(json_file, isVersion)
                    # write to file
                    with open(directory + '/' + file + '/' + versionFile, 'w') as json_file:
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

    serviceId = service.find('{http://einfracentral.eu}id').text
    with open(args.csvPath, mode='r') as csv_file:
        headersIndex = 0
        for row_number, row in enumerate(csv_file.readlines()):
            if row_number == 0:
                header_data = row.split(',')
                for column in header_data:
                    headers[headersIndex] = column
                    headersIndex = headersIndex + 1
            else:
                data = row.split(',')
                if data[0] == serviceId:

                    ## OPTIONAL FIELDS ##
                    submissionPolicyURL = ET.Element("tns:submissionPolicyURL")
                    submissionPolicyURL.text = data[1]

                    preservationPolicyURL = ET.Element("tns:preservationPolicyURL")
                    preservationPolicyURL.text = data[2]

                    versionControl = ET.Element("tns:versionControl")
                    versionControl.text = data[3].lower()

                    persistentIdentitySystems = ET.Element("tns:persistentIdentitySystems")
                    persistentIdentitySystems.text = data[4]
                    ## OPTIONAL FIELDS ##

                    ## MANDATORY FIELDS ##
                    jurisdiction = ET.Element("tns:jurisdiction")
                    jurisdiction.text = data[5]

                    datasourceClassification = ET.Element("tns:datasourceClassification")
                    datasourceClassification.text = data[6]

                    researchEntityTypes = ET.Element("tns:researchEntityTypes")
                    researchEntityTypes.text = data[7]

                    thematic = ET.Element("tns:thematic")
                    thematic.text = data[8].lower()

                    researchProductLicensings = ET.Element("tns:researchProductLicensings")
                    researchProductLicensings.text = data[9]

                    researchProductAccessPolicies = ET.Element("tns:researchProductAccessPolicies")
                    researchProductAccessPolicies.text = data[10]

                    researchProductMetadataLicensing = ET.Element("tns:researchProductMetadataLicensing")
                    researchProductMetadataLicensing.text = data[11]

                    researchProductMetadataAccessPolicies = ET.Element("tns:researchProductMetadataAccessPolicies")
                    researchProductMetadataAccessPolicies.text = data[12]
                    ## MANDATORY FIELDS ##

                    service.append(submissionPolicyURL)
                    service.append(preservationPolicyURL)
                    service.append(versionControl)
                    service.append(persistentIdentitySystems)
                    service.append(jurisdiction)
                    service.append(datasourceClassification)
                    service.append(researchEntityTypes)
                    service.append(thematic)
                    service.append(researchProductLicensings)
                    service.append(researchProductAccessPolicies)
                    service.append(researchProductMetadataLicensing)
                    service.append(researchProductMetadataAccessPolicies)


    root.write('output.xml')
    with open("output.xml", "r") as xml_file:
        content = xml_file.readlines()
        content = "".join(content)
        bs_content = bs(content, "xml")
        json_data['payload'] = str(bs_content).replace("&lt;", "<").replace("&gt;", ">").replace("\n", "")
        if isVersion:
            json_data['resource']['payload'] = json_data['payload']

    return json_data
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-fp", "--folderPath", help="sets the folder path", type=str, required=True)
    parser.add_argument("-cp", "--csvPath", help="sets the csv path", type=str, required=True)
    args = parser.parse_args()
    folder_selection(args.folderPath)
######################################################## RUN ###########################################################