######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import SubElement
import os
from bs4 import BeautifulSoup as bs
######################################################## IMPORTS #######################################################


################################################### GLOBAL VARIABLES ###################################################
directory = '/home/mike/Desktop/estella/'
################################################### GLOBAL VARIABLES ###################################################


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

            serviceName = service.find('{http://einfracentral.eu}name')
            abbreviation = ET.Element("tns:abbreviation")
            if serviceName is not None:
                abbreviation.text = serviceName.text
            service.append(abbreviation)

            multimediaEntries = []
            serviceMultimedia = service.find('{http://einfracentral.eu}multimedia')
            if serviceMultimedia is not None:
                for entry in serviceMultimedia:
                    if entry is not None:
                        multimediaEntries.append(entry.text)
                service.remove(serviceMultimedia)
            multimedia = ET.Element("tns:multimedia")
            if multimediaEntries:
                for entry in multimediaEntries:
                    multimediaChild = SubElement(multimedia, 'tns:multimedia')
                    multimediaURL = SubElement(multimediaChild, 'tns:multimediaURL')
                    multimediaURL.text = entry
                    multimediaName = SubElement(multimediaChild, 'tns:multimediaName')
            service.append(multimedia)

            useCaseEntries = []
            serviceUseCases = service.find('{http://einfracentral.eu}useCases')
            if serviceUseCases is not None:
                for entry in serviceUseCases:
                    if entry is not None:
                        useCaseEntries.append(entry.text)
                service.remove(serviceUseCases)
            useCases = ET.Element("tns:useCases")
            if useCaseEntries:
                for entry in useCaseEntries:
                    useCaseChild = SubElement(useCases, 'tns:useCase')
                    useCaseURL = SubElement(useCaseChild, 'tns:useCaseURL')
                    useCaseURL.text = entry
                    useCaseName = SubElement(useCaseChild, 'tns:useCaseName')
            service.append(useCases)

            serviceRelatedPlatforms = service.find('{http://einfracentral.eu}relatedPlatforms')
            if serviceRelatedPlatforms is not None:
                for entry in serviceRelatedPlatforms:
                    entry.text = 'related_platform-tbd'

            serviceTOU = service.find('{http://einfracentral.eu}termsOfUse')
            if serviceTOU is None:
                serviceTOU = ET.Element("tns:termsOfUse")
                serviceTOU.text = 'https://providers.eosc-portal.eu/home'
                service.append(serviceTOU)

            servicePrivacyPolicy = service.find('{http://einfracentral.eu}privacyPolicy')
            if servicePrivacyPolicy is None:
                servicePrivacyPolicy = ET.Element("tns:privacyPolicy")
                servicePrivacyPolicy.text = 'https://providers.eosc-portal.eu/home'
                service.append(servicePrivacyPolicy)

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

                serviceName = service.find('{http://einfracentral.eu}name')
                # # Add default values for the transition to the new model
                abbreviation = ET.Element("tns:abbreviation")
                if serviceName is not None:
                    abbreviation.text = serviceName.text
                service.append(abbreviation)

                multimediaEntries = []
                serviceMultimedia = service.find('{http://einfracentral.eu}multimedia')
                if serviceMultimedia is not None:
                    for entry in serviceMultimedia:
                        if entry is not None:
                            multimediaEntries.append(entry.text)
                    service.remove(serviceMultimedia)
                multimedia = ET.Element("tns:multimedia")
                if multimediaEntries:
                    for entry in multimediaEntries:
                        multimediaChild = SubElement(multimedia, 'tns:multimedia')
                        multimediaURL = SubElement(multimediaChild, 'tns:multimediaURL')
                        multimediaURL.text = entry
                        multimediaName = SubElement(multimediaChild, 'tns:multimediaName')
                service.append(multimedia)

                useCaseEntries = []
                serviceUseCases = service.find('{http://einfracentral.eu}useCases')
                if serviceUseCases is not None:
                    for entry in serviceUseCases:
                        if entry is not None:
                            useCaseEntries.append(entry.text)
                    service.remove(serviceUseCases)
                useCases = ET.Element("tns:useCases")
                if useCaseEntries:
                    for entry in useCaseEntries:
                        useCaseChild = SubElement(useCases, 'tns:useCase')
                        useCaseURL = SubElement(useCaseChild, 'tns:useCaseURL')
                        useCaseURL.text = entry
                        useCaseName = SubElement(useCaseChild, 'tns:useCaseName')
                service.append(useCases)

                serviceRelatedPlatforms = service.find('{http://einfracentral.eu}relatedPlatforms')
                if serviceRelatedPlatforms is not None:
                    for entry in serviceRelatedPlatforms:
                        entry.text = 'related_platform-tbd'

                serviceTOU = service.find('{http://einfracentral.eu}termsOfUse')
                if serviceTOU is None:
                    serviceTOU = ET.Element("tns:termsOfUse")
                    serviceTOU.text = 'https://providers.eosc-portal.eu/home'
                    service.append(serviceTOU)

                servicePrivacyPolicy = service.find('{http://einfracentral.eu}privacyPolicy')
                if servicePrivacyPolicy is None:
                    servicePrivacyPolicy = ET.Element("tns:privacyPolicy")
                    servicePrivacyPolicy.text = 'https://providers.eosc-portal.eu/home'
                    service.append(servicePrivacyPolicy)

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

            serviceName = service.find('{http://einfracentral.eu}name')
            # # Add default values for the transition to the new model
            abbreviation = ET.Element("tns:abbreviation")
            if serviceName is not None:
                abbreviation.text = serviceName.text
            service.append(abbreviation)

            multimediaEntries = []
            serviceMultimedia = service.find('{http://einfracentral.eu}multimedia')
            if serviceMultimedia is not None:
                for entry in serviceMultimedia:
                    if entry is not None:
                        multimediaEntries.append(entry.text)
                service.remove(serviceMultimedia)
            multimedia = ET.Element("tns:multimedia")
            if multimediaEntries:
                for entry in multimediaEntries:
                    multimediaChild = SubElement(multimedia, 'tns:multimedia')
                    multimediaURL = SubElement(multimediaChild, 'tns:multimediaURL')
                    multimediaURL.text = entry
                    multimediaName = SubElement(multimediaChild, 'tns:multimediaName')
            service.append(multimedia)

            useCaseEntries = []
            serviceUseCases = service.find('{http://einfracentral.eu}useCases')
            if serviceUseCases is not None:
                for entry in serviceUseCases:
                    if entry is not None:
                        useCaseEntries.append(entry.text)
                service.remove(serviceUseCases)
            useCases = ET.Element("tns:useCases")
            if useCaseEntries:
                for entry in useCaseEntries:
                    useCaseChild = SubElement(useCases, 'tns:useCase')
                    useCaseURL = SubElement(useCaseChild, 'tns:useCaseURL')
                    useCaseURL.text = entry
                    useCaseName = SubElement(useCaseChild, 'tns:useCaseName')
            service.append(useCases)
            serviceRelatedPlatforms = service.find('{http://einfracentral.eu}relatedPlatforms')
            if serviceRelatedPlatforms is not None:
                for entry in serviceRelatedPlatforms:
                    entry.text = 'related_platform-tbd'

            serviceTOU = service.find('{http://einfracentral.eu}termsOfUse')
            if serviceTOU is None:
                serviceTOU = ET.Element("tns:termsOfUse")
                serviceTOU.text = 'https://providers.eosc-portal.eu/home'
                service.append(serviceTOU)

            servicePrivacyPolicy = service.find('{http://einfracentral.eu}privacyPolicy')
            if servicePrivacyPolicy is None:
                servicePrivacyPolicy = ET.Element("tns:privacyPolicy")
                servicePrivacyPolicy.text = 'https://providers.eosc-portal.eu/home'
                service.append(servicePrivacyPolicy)

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

                serviceName = service.find('{http://einfracentral.eu}name')
                # # Add default values for the transition to the new model
                abbreviation = ET.Element("tns:abbreviation")
                if serviceName is not None:
                    abbreviation.text = serviceName.text
                service.append(abbreviation)

                multimediaEntries = []
                serviceMultimedia = service.find('{http://einfracentral.eu}multimedia')
                if serviceMultimedia is not None:
                    for entry in serviceMultimedia:
                        if entry is not None:
                            multimediaEntries.append(entry.text)
                    service.remove(serviceMultimedia)
                multimedia = ET.Element("tns:multimedia")
                if multimediaEntries:
                    for entry in multimediaEntries:
                        multimediaChild = SubElement(multimedia, 'tns:multimedia')
                        multimediaURL = SubElement(multimediaChild, 'tns:multimediaURL')
                        multimediaURL.text = entry
                        multimediaName = SubElement(multimediaChild, 'tns:multimediaName')
                service.append(multimedia)

                useCaseEntries = []
                serviceUseCases = service.find('{http://einfracentral.eu}useCases')
                if serviceUseCases is not None:
                    for entry in serviceUseCases:
                        if entry is not None:
                            useCaseEntries.append(entry.text)
                    service.remove(serviceUseCases)
                useCases = ET.Element("tns:useCases")
                if useCaseEntries:
                    for entry in useCaseEntries:
                        useCaseChild = SubElement(useCases, 'tns:useCase')
                        useCaseURL = SubElement(useCaseChild, 'tns:useCaseURL')
                        useCaseURL.text = entry
                        useCaseName = SubElement(useCaseChild, 'tns:useCaseName')
                service.append(useCases)

                if serviceRelatedPlatforms is not None:
                    for entry in serviceRelatedPlatforms:
                        entry.text = 'related_platform-tbd'

                serviceTOU = service.find('{http://einfracentral.eu}termsOfUse')
                if serviceTOU is None:
                    serviceTOU = ET.Element("tns:termsOfUse")
                    serviceTOU.text = 'https://providers.eosc-portal.eu/home'
                    service.append(serviceTOU)

                servicePrivacyPolicy = service.find('{http://einfracentral.eu}privacyPolicy')
                if servicePrivacyPolicy is None:
                    servicePrivacyPolicy = ET.Element("tns:privacyPolicy")
                    servicePrivacyPolicy.text = 'https://providers.eosc-portal.eu/home'
                    service.append(servicePrivacyPolicy)

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

            multimediaEntries = []
            providerMultimedia = provider.find('{http://einfracentral.eu}multimedia')
            if providerMultimedia is not None:
                for entry in providerMultimedia:
                    if entry is not None:
                        multimediaEntries.append(entry.text)
                provider.remove(providerMultimedia)
            multimedia = ET.Element("tns:multimedia")
            if multimediaEntries:
                for entry in multimediaEntries:
                    multimediaChild = SubElement(multimedia, 'tns:multimedia')
                    multimediaURL = SubElement(multimediaChild, 'tns:multimediaURL')
                    multimediaURL.text = entry
                    multimediaName = SubElement(multimediaChild, 'tns:multimediaName')
            provider.append(multimedia)

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

                multimediaEntries = []
                providerMultimedia = provider.find('{http://einfracentral.eu}multimedia')
                if providerMultimedia is not None:
                    for entry in providerMultimedia:
                        if entry is not None:
                            multimediaEntries.append(entry.text)
                    provider.remove(providerMultimedia)
                multimedia = ET.Element("tns:multimedia")
                if multimediaEntries:
                    for entry in multimediaEntries:
                        multimediaChild = SubElement(multimedia, 'tns:multimedia')
                        multimediaURL = SubElement(multimediaChild, 'tns:multimediaURL')
                        multimediaURL.text = entry
                        multimediaName = SubElement(multimediaChild, 'tns:multimediaName')
                provider.append(multimedia)

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

            multimediaEntries = []
            providerMultimedia = provider.find('{http://einfracentral.eu}multimedia')
            if providerMultimedia is not None:
                for entry in providerMultimedia:
                    if entry is not None:
                        multimediaEntries.append(entry.text)
                provider.remove(providerMultimedia)
            multimedia = ET.Element("tns:multimedia")
            if multimediaEntries:
                for entry in multimediaEntries:
                    multimediaChild = SubElement(multimedia, 'tns:multimedia')
                    multimediaURL = SubElement(multimediaChild, 'tns:multimediaURL')
                    multimediaURL.text = entry
                    multimediaName = SubElement(multimediaChild, 'tns:multimediaName')
            provider.append(multimedia)

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

                multimediaEntries = []
                providerMultimedia = provider.find('{http://einfracentral.eu}multimedia')
                if providerMultimedia is not None:
                    for entry in providerMultimedia:
                        if entry is not None:
                            multimediaEntries.append(entry.text)
                    provider.remove(providerMultimedia)
                multimedia = ET.Element("tns:multimedia")
                if multimediaEntries:
                    for entry in multimediaEntries:
                        multimediaChild = SubElement(multimedia, 'tns:multimedia')
                        multimediaURL = SubElement(multimediaChild, 'tns:multimediaURL')
                        multimediaURL.text = entry
                        multimediaName = SubElement(multimediaChild, 'tns:multimediaName')
                provider.append(multimedia)

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