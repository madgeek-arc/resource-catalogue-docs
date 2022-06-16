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
                abbreviation.text = serviceName.text
            service.append(abbreviation)

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
                    abbreviation.text = serviceName.text
                service.append(abbreviation)

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
                abbreviation.text = serviceName.text
            service.append(abbreviation)

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
                    abbreviation.text = serviceName.text
                service.append(abbreviation)

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