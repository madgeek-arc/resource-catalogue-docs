######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
######################################################## IMPORTS #######################################################


################################################### GLOBAL VARIABLES ###################################################
directory = '/home/mike/Desktop/estella/'
################################################### GLOBAL VARIABLES ###################################################


################################################### PROVIDER JSON ######################################################
for file in os.listdir(directory + '/provider/'):
    if file.endswith('.json'):
        with open(directory + '/provider/' + file, 'r') as json_file:

            json_data = json.load(json_file)
            xml = json_data['payload']

            ET.register_namespace("tns", "http://einfracentral.eu")
            root = ET.ElementTree(ET.fromstring(xml))
            tree = root.getroot()
            provider = root.find('{http://einfracentral.eu}provider')

            # metadata -> published
            metadata = root.find('{http://einfracentral.eu}metadata')
            published = metadata.find('{http://einfracentral.eu}published')
            if published is None:
                newPublished = ET.Element("tns:published")
                newPublished.text = 'false'
                metadata.append(newPublished)

            root.write('output.xml')

            content = []
            with open("output.xml", "r") as xml_file:
                content = xml_file.readlines()
                content = "".join(content)
                bs_content = bs(content, "xml")
                json_data['payload'] = str(bs_content)

            # write to file
            with open(directory + '/provider/' + file, 'w') as json_file:
                json.dump(json_data, json_file, indent=2)
################################################### PROVIDER JSON ######################################################


################################################# PROVIDER VERSION #####################################################
for folder in os.listdir(directory + '/provider/'):
    if folder.endswith('-version'):
        files = os.listdir(directory + '/provider/' + folder)
        for file in files:
            with open(directory + '/provider/' + folder + '/' + file,
                      'r') as json_file:

                json_data = json.load(json_file)
                xml = json_data['payload']

                ET.register_namespace("tns", "http://einfracentral.eu")
                root = ET.ElementTree(ET.fromstring(xml))
                tree = root.getroot()
                provider = root.find('{http://einfracentral.eu}provider')

                # metadata -> published
                metadata = root.find('{http://einfracentral.eu}metadata')
                published = metadata.find('{http://einfracentral.eu}published')
                if published is None:
                    newPublished = ET.Element("tns:published")
                    newPublished.text = 'false'
                    metadata.append(newPublished)

                root.write('output.xml')
                content = []
                with open("output.xml", "r") as xml_file:
                    content = xml_file.readlines()
                    content = "".join(content)
                    bs_content = bs(content, "xml")
                    json_data['payload'] = str(bs_content)
                    json_data['resource']['payload'] = json_data['payload']

                # write to file
                with open(directory + '/provider/' + folder + '/' + file,
                          'w') as json_file:
                    json.dump(json_data, json_file, indent=2)
################################################# PROVIDER VERSION #####################################################


##################################################### SERVICE JSON #####################################################
for file in os.listdir(directory + '/infra_service/'):
    if file.endswith('.json'):
        with open(directory + '/infra_service/' + file, 'r') as json_file:

            json_data = json.load(json_file)
            xml = json_data['payload']

            ET.register_namespace("tns", "http://einfracentral.eu")
            root = ET.ElementTree(ET.fromstring(xml))
            tree = root.getroot()
            service = root.find('{http://einfracentral.eu}service')

            # metadata -> published
            metadata = root.find('{http://einfracentral.eu}metadata')
            published = metadata.find('{http://einfracentral.eu}published')
            if published is None:
                newPublished = ET.Element("tns:published")
                newPublished.text = 'false'
                metadata.append(newPublished)

            root.write('output.xml')

            content = []
            with open("output.xml", "r") as xml_file:
                content = xml_file.readlines()
                content = "".join(content)
                bs_content = bs(content, "xml")
                json_data['payload'] = str(bs_content)

            # write to file
            with open(directory + '/infra_service/' + file, 'w') as json_file:
                json.dump(json_data, json_file, indent=2)
##################################################### SERVICE JSON #####################################################


################################################### SERVICE VERSION ####################################################
for folder in os.listdir(directory + '/infra_service/'):
    if folder.endswith('-version'):
        files = os.listdir(directory + '/infra_service/' + folder)
        for file in files:
            with open(directory + '/infra_service/' + folder + '/' + file,
                      'r') as json_file:

                json_data = json.load(json_file)
                xml = json_data['payload']

                ET.register_namespace("tns", "http://einfracentral.eu")
                root = ET.ElementTree(ET.fromstring(xml))
                tree = root.getroot()
                service = root.find('{http://einfracentral.eu}service')

                # metadata -> published
                metadata = root.find('{http://einfracentral.eu}metadata')
                published = metadata.find('{http://einfracentral.eu}published')
                if published is None:
                    newPublished = ET.Element("tns:published")
                    newPublished.text = 'false'
                    metadata.append(newPublished)

                root.write('output.xml')
                content = []
                with open("output.xml", "r") as xml_file:
                    content = xml_file.readlines()
                    content = "".join(content)
                    bs_content = bs(content, "xml")
                    json_data['payload'] = str(bs_content)
                    json_data['resource']['payload'] = json_data['payload']

                # write to file
                with open(directory + '/infra_service/' + folder + '/' + file,
                          'w') as json_file:
                    json.dump(json_data, json_file, indent=2)
################################################### SERVICE VERSION ####################################################


############################################## PENDING PROVIDER JSON ###################################################
for file in os.listdir(directory + '/pending_provider/'):
    if file.endswith('.json'):
        with open(directory + '/pending_provider/' + file, 'r') as json_file:

            json_data = json.load(json_file)
            xml = json_data['payload']

            ET.register_namespace("tns", "http://einfracentral.eu")
            root = ET.ElementTree(ET.fromstring(xml))
            tree = root.getroot()
            provider = root.find('{http://einfracentral.eu}provider')

            # metadata -> published
            metadata = root.find('{http://einfracentral.eu}metadata')
            published = metadata.find('{http://einfracentral.eu}published')
            if published is None:
                newPublished = ET.Element("tns:published")
                newPublished.text = 'false'
                metadata.append(newPublished)

            root.write('output.xml')

            content = []
            with open("output.xml", "r") as xml_file:
                content = xml_file.readlines()
                content = "".join(content)
                bs_content = bs(content, "xml")
                json_data['payload'] = str(bs_content)

            # write to file
            with open(directory + '/pending_provider/' + file, 'w') as json_file:
                json.dump(json_data, json_file, indent=2)
############################################## PENDING PROVIDER JSON ###################################################


############################################ PENDING PROVIDER VERSION ##################################################
for folder in os.listdir(directory + '/pending_provider/'):
    if folder.endswith('-version'):
        files = os.listdir(directory + '/pending_provider/' + folder)
        for file in files:
            with open(directory + '/pending_provider/' + folder + '/' + file,
                      'r') as json_file:

                json_data = json.load(json_file)
                xml = json_data['payload']

                ET.register_namespace("tns", "http://einfracentral.eu")
                root = ET.ElementTree(ET.fromstring(xml))
                tree = root.getroot()
                provider = root.find('{http://einfracentral.eu}provider')

                # metadata -> published
                metadata = root.find('{http://einfracentral.eu}metadata')
                published = metadata.find('{http://einfracentral.eu}published')
                if published is None:
                    newPublished = ET.Element("tns:published")
                    newPublished.text = 'false'
                    metadata.append(newPublished)

                root.write('output.xml')
                content = []
                with open("output.xml", "r") as xml_file:
                    content = xml_file.readlines()
                    content = "".join(content)
                    bs_content = bs(content, "xml")
                    json_data['payload'] = str(bs_content)
                    json_data['resource']['payload'] = json_data['payload']

                # write to file
                with open(directory + '/pending_provider/' + folder + '/' + file,
                          'w') as json_file:
                    json.dump(json_data, json_file, indent=2)
############################################ PENDING PROVIDER VERSION ##################################################


################################################ PENDING SERVICE JSON ##################################################
for file in os.listdir(directory + '/pending_service/'):
    if file.endswith('.json'):
        with open(directory + '/pending_service/' + file, 'r') as json_file:

            json_data = json.load(json_file)
            xml = json_data['payload']

            ET.register_namespace("tns", "http://einfracentral.eu")
            root = ET.ElementTree(ET.fromstring(xml))
            tree = root.getroot()
            service = root.find('{http://einfracentral.eu}service')

            # metadata -> published
            metadata = root.find('{http://einfracentral.eu}metadata')
            published = metadata.find('{http://einfracentral.eu}published')
            if published is None:
                newPublished = ET.Element("tns:published")
                newPublished.text = 'false'
                metadata.append(newPublished)

            root.write('output.xml')

            content = []
            with open("output.xml", "r") as xml_file:
                content = xml_file.readlines()
                content = "".join(content)
                bs_content = bs(content, "xml")
                json_data['payload'] = str(bs_content)

            # write to file
            with open(directory + '/pending_service/' + file, 'w') as json_file:
                json.dump(json_data, json_file, indent=2)
################################################ PENDING SERVICE JSON ##################################################


############################################## PENDING SERVICE VERSION #################################################
for folder in os.listdir(directory + '/pending_service/'):
    if folder.endswith('-version'):
        files = os.listdir(directory + '/pending_service/' + folder)
        for file in files:
            with open(directory + '/pending_service/' + folder + '/' + file,
                      'r') as json_file:

                json_data = json.load(json_file)
                xml = json_data['payload']

                ET.register_namespace("tns", "http://einfracentral.eu")
                root = ET.ElementTree(ET.fromstring(xml))
                tree = root.getroot()
                service = root.find('{http://einfracentral.eu}service')

                # metadata -> published
                metadata = root.find('{http://einfracentral.eu}metadata')
                published = metadata.find('{http://einfracentral.eu}published')
                if published is None:
                    newPublished = ET.Element("tns:published")
                    newPublished.text = 'false'
                    metadata.append(newPublished)

                root.write('output.xml')
                content = []
                with open("output.xml", "r") as xml_file:
                    content = xml_file.readlines()
                    content = "".join(content)
                    bs_content = bs(content, "xml")
                    json_data['payload'] = str(bs_content)
                    json_data['resource']['payload'] = json_data['payload']

                # write to file
                with open(directory + '/pending_service/' + folder + '/' + file,
                          'w') as json_file:
                    json.dump(json_data, json_file, indent=2)
############################################## PENDING SERVICE VERSION #################################################