######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import SubElement
import os
from bs4 import BeautifulSoup as bs
import argparse
######################################################## IMPORTS #######################################################


##################################################### DICTIONARIES ####################################################
relatedPlatformsDict = {
  'related_platform-artportalen': 'ArtPortalen',
  'related_platform-arxiv': 'arXiv',
  'related_platform-ala': 'Atlas of Living Australia',
  'related_platform-avp': 'AV-Portal',
  'related_platform-aws': 'AWS',
  'related_platform-bluecloud': 'Blue-Cloud',
  'related_platform-cdl': 'California Digital Library',
  'related_platform-ccdc': 'CCDC',
  'related_platform-cessda': 'CESSDA',
  'related_platform-collabwith': 'COLLABWITH',
  'related_platform-cccs': 'Copernicus Climate Change Service',
  'related_platform-crossref': 'Crossref',
  'related_platform-dariahteach': 'dariahTeach',
  'related_platform-dice': 'Data Infrastructure Capacity for EOSC (DICE)',
  'related_platform-datacite': 'DataCite',
  'related_platform-ds': 'Digital Science',
  'related_platform-doab': 'DOAB',
  'related_platform-einfracz': 'e-INFRA CZ',
  'related_platform-eirgspp': 'e-IRGSP projects',
  'related_platform-edugain': 'eduGAIN',
  'related_platform-eduteams': 'eduTEAMS',
  'related_platform-egi': 'EGI',
  'related_platform-egifc': 'EGI Federated Cloud',
  'related_platform-egiace': 'EGI-ACE',
  'related_platform-elixir': 'ELIXIR',
  'related_platform-emodnetc': 'EMODnet Chemistry',
  'related_platform-eol': 'Encyclopedia of Life',
  'related_platform-enc': 'Endemia New Caledonia',
  'related_platform-envri': 'ENVRI Hub',
  'related_platform-eoscl': 'EOSC-Life',
  'related_platform-eoscn': 'EOSC-Nordic',
  'related_platform-eoscp': 'EOSC-Pillar',
  'related_platform-eudatcdi': 'EUDAT CDI',
  'related_platform-elg': 'European Language Grid',
  'related_platform-evs': 'European Values Study (EVS)',
  'related_platform-garrcp': 'GARR Container Platform',
  'related_platform-gatep': 'GATE platform',
  'related_platform-gbif': 'GBIF',
  'related_platform-geonames': 'GeoNames',
  'related_platform-grin': 'Germplasm Resources Information Network (GRIN)',
  'related_platform-geoss': 'Global Earth Observation system of Systems (GEOSS)',
  'related_platform-hal': 'HAL',
  'related_platform-hamelin': 'Hamelin',
  'related_platform-infnc': 'INFN-Cloud',
  'related_platform-ispot': 'iSpot',
  'related_platform-jisc': 'JISC',
  'related_platform-metacentrum': 'MetaCentrum',
  'related_platform-natusfera': 'Natusfera',
  'related_platform-openairee': 'OpenAIRE EXPLORE',
  'related_platform-openairem': 'OpenAIRE MONITOR',
  'related_platform-openairerg': 'OpenAIRE research graph',
  'related_platform-oc': 'OpenCitations',
  'related_platform-pogo': 'Partnership for Observation of the Global Oceans (POGO)',
  'related_platform-pnp': 'Pl@ntNet platform',
  'related_platform-pc': 'PolicyCloud',
  'related_platform-rjb': 'Real Jardín Botánico',
  'related_platform-scopus': 'Scopus',
  'related_platform-seadatanet': 'SeaDataNet',
  'related_platform-tsd': 'Service for Sensitive Data (TSD)',
  'related_platform-sshom': 'SSH Open Marketplace',
  'related_platform-surf': 'SURF',
  'related_platform-share': 'Survey of Health, Ageing and Retirement in Europe (SHARE)',
  'related_platform-tf': 'Taylor&Francis',
  'related_platform-tb': 'Tela Botanica',
  'related_platform-tdp': 'The Dataverse Project',
  'related_platform-tnomadl': 'The NOMAD Laboratory',
  'related_platform-tpg': 'the Plant Game',
  'related_platform-tibp': 'TIB Portal',
  'related_platform-tripleh': 'TRIPLE H2020 project',
  'related_platform-tubitakcc': 'TÜBITAK cloud compute',
  'related_platform-vlab': 'Virtual Earth Laboratory (VLab)',
  'related_platform-zbwice': 'ZBW Information Centre for Economics',
  'related_platform-zenodo': 'Zenodo'
}

hostingLegalEntityDict = {
  'provider_hosting_legal_entity-cdrc': 'Centre de recherche Crem',
  'provider_hosting_legal_entity-cnrs': 'Centre National de la Recherche Scientifique (CNRS)',
  'provider_hosting_legal_entity-cesnet': 'CESNET',
  'provider_hosting_legal_entity-cci': 'Cineca Consorzio Interuniversitario',
  'provider_hosting_legal_entity-cf': 'CloudFerro',
  'provider_hosting_legal_entity-cnio': 'CNIO - Spanish National Cancer Research Centre',
  'provider_hosting_legal_entity-collabwith': 'COLLABWITH',
  'provider_hosting_legal_entity-coard': 'Collaborative Open Access Research and Development (COARD)',
  'provider_hosting_legal_entity-capsh': 'Committee for the Accessibility of Publications in Sciences and Humanities (CAPSH)',
  'provider_hosting_legal_entity-cite': 'Communication & Information Technologies Experts SA Consulting and Development Services (CITE)',
  'provider_hosting_legal_entity-csic': 'Consejo Superior de Investigaciones Científicas (CSIC)',
  'provider_hosting_legal_entity-earthwatch': 'Conservation Education and Research Trust (Earthwatch)',
  'provider_hosting_legal_entity-cells': 'Consortium for the Construction, Equipping and Exploitation of a synchrotron light source (CELLS)',
  'provider_hosting_legal_entity-cessdaeric': 'Consortium of European Social Science Data Archives ERIC',
  'provider_hosting_legal_entity-csip': 'Consorzio per il Sistema Informativo (CSI Piemonte)',
  'provider_hosting_legal_entity-ccsl': 'CORONIS COMPUTING SL',
  'provider_hosting_legal_entity-csg': 'CS GROUP',
  'provider_hosting_legal_entity-csc': 'CSC – IT CENTER FOR SCIENCE',
  'provider_hosting_legal_entity-cybcebbruc': 'CY-Biobank Center of Excellence in Biobanking and Biomedical Research - University of Cyprus',
  'provider_hosting_legal_entity-cyberbotics': 'Cyberbotics',
  'provider_hosting_legal_entity-dariaheric': 'DARIAH ERIC (Digital Research Infrastructure for the Arts and Humanities)',
  'provider_hosting_legal_entity-dr': 'Data Revenue',
  'provider_hosting_legal_entity-datacite': 'DataCite',
  'provider_hosting_legal_entity-ddqbv': 'DDQ B.V.',
  'provider_hosting_legal_entity-desy': 'Deutsches Elektronen-Synchrotron (DESY)',
  'provider_hosting_legal_entity-dkrz': 'Deutsches Klimarechenzentrum (DKRZ)',
  'provider_hosting_legal_entity-dlsltd': 'Diamond Light Source Ltd',
  'provider_hosting_legal_entity-dcc': 'Digital Curation Centre (DCC)',
  'provider_hosting_legal_entity-doabf': 'DOAB Foundation',
  'provider_hosting_legal_entity-dal': 'DynAikon Limited',
  'provider_hosting_legal_entity-eodc': 'Earth Observation Data Centre for Water Resources Monitoring (EODC)',
  'provider_hosting_legal_entity-ecgmbh': 'Edelweiss Connect GmbH',
  'provider_hosting_legal_entity-egif': 'EGI Foundation',
  'provider_hosting_legal_entity-eiscatsa': 'EISCAT Scientific Association',
  'provider_hosting_legal_entity-ebv': 'Elsevier BV',
  'provider_hosting_legal_entity-enhancer': 'EnhanceR',
  'provider_hosting_legal_entity-eoxitsgmbh': 'EOX IT Services GmbH',
  'provider_hosting_legal_entity-epot': 'EPOT',
  'provider_hosting_legal_entity-emc': 'Erasmus Medical Center',
  'provider_hosting_legal_entity-eudat': 'EUDAT',
  'provider_hosting_legal_entity-er': 'Eurac Research',
  'provider_hosting_legal_entity-cmcc': 'Euro-Mediterranean Center on Climate Change (CMCC)',
  'provider_hosting_legal_entity-emblebi': 'European Molecular Biology Laboratory - European Bioinformatics Institute (EMBL-EBI)',
  'provider_hosting_legal_entity-emso': 'European Multidisciplinary Seafloor and water column Observatory (EMSO)',
  'provider_hosting_legal_entity-cern': 'EUROPEAN ORGANIZATION FOR NUCLEAR RESEARCH (CERN)',
  'provider_hosting_legal_entity-clarineric': 'European Research Infrastructure for Language Resources and Technology (CLARIN ERIC)',
  'provider_hosting_legal_entity-esseric': 'European Social Survey, European Research Infrastructure Consortium',
  'provider_hosting_legal_entity-essoeric': 'European Spallation Source ERIC',
  'provider_hosting_legal_entity-esrf': 'European Synchrotron Radiation Facility (ESRF)',
  'provider_hosting_legal_entity-ef': 'Europeana Foundation',
  'provider_hosting_legal_entity-exoscale': 'EXOSCALE',
  'provider_hosting_legal_entity-expertai': 'expert.ai',
  'provider_hosting_legal_entity-f6sn': 'F6S Network',
  'provider_hosting_legal_entity-fairdi': 'FAIR Data Infrastructure for Physics, Chemistry, Materials Science, and Astronomy (FAIR-DI)',
  'provider_hosting_legal_entity-figshare': 'Figshare',
  'provider_hosting_legal_entity-fnsp': 'Fondation Nationale des Sciences Politiques (Sciences Po)',
  'provider_hosting_legal_entity-forth': 'Foundation for Research and Technology, Hellas (FORTH)',
  'provider_hosting_legal_entity-fscai': 'Fraunhofer SCAI',
  'provider_hosting_legal_entity-cesga': 'Fundacion Centro Tecnologico de Supercomputacion de Galicia (CESGA)',
  'provider_hosting_legal_entity-gccumcg': 'Genomics Coordination Center, University Medical Center Groningen (GCC UMCG)',
  'provider_hosting_legal_entity-gwdg': 'Gesellschaft für wissenschaftliche Datenverarbeitung mbH Göttingen (GWDG)',
  'provider_hosting_legal_entity-gesisliss': 'GESIS Leibniz Institute for the Social Sciences',
  'provider_hosting_legal_entity-gbif': 'Global Biodiversity Information Facility (GBIF)',
  'provider_hosting_legal_entity-gsihsgmbh': 'GSI Helmholtzzentrum für Schwerionenforschung GmbH',
  'provider_hosting_legal_entity-geant': 'GÉANT Association',
  'provider_hosting_legal_entity-hzdr': 'Helmholtz-Zentrum Dresden-Rossendorf e.V. (HZDR)',
  'provider_hosting_legal_entity-ifinhh': 'Horia Hulubei National Institute for R&D in Physics and Nuclear Engineering (IFIN-HH)',
  'provider_hosting_legal_entity-hostkeybv': 'HOSTKEY B.V. - Dedicated servers in Amsterdam DC',
  'provider_hosting_legal_entity-ideaconsult': 'IDEAconsult',
  'provider_hosting_legal_entity-ifnios': 'Ifremer, the French National Institute for Ocean Science',
  'provider_hosting_legal_entity-infrafrontier': 'INFRAFRONTIER',
  'provider_hosting_legal_entity-ill': 'Institut Laue Langevin (ILL)',
  'provider_hosting_legal_entity-inria': 'Institut national de recherche en informatique et en automatique (INRIA)',
  'provider_hosting_legal_entity-sztaki': 'INSTITUTE FOR COMPUTER SCIENCE AND CONTROL (SZTAKI)',
  'provider_hosting_legal_entity-isti': "Institute for Information Science and Technologies 'Alessandro Faedo' - ISTI",
  'provider_hosting_legal_entity-iasa': 'Institute of Accelerating Systems and Applications (IASA)',
  'provider_hosting_legal_entity-cnriia': 'Institute of Atmospheric Pollution Research - National Research Council of Italy (CNR IIA)',
  'provider_hosting_legal_entity-ibiomcnr': 'Institute of Biomembranes, Bioenergetics and Molecular Biotechnologies, National Research Council (IBIOM-CNR)',
  'provider_hosting_legal_entity-iisas': 'Institute of Informatics - Slovak Academy of Sciences (IISAS)',
  'provider_hosting_legal_entity-iict': 'Institute of Information and Communication Technologies (IICT)',
  'provider_hosting_legal_entity-isaul': 'Instituto Superior de Agronomia da Universidade de Lisboa',
  'provider_hosting_legal_entity-ieric': 'Instruct-ERIC',
  'provider_hosting_legal_entity-icoseric': 'Integrated Carbon Observation System European Research Infrastructure Consortium (ICOS ERIC)',
  'provider_hosting_legal_entity-inaf': 'Istituto Nazionale di Astrofisica (INAF)',
  'provider_hosting_legal_entity-infn': 'Italian National Institute of Nuclear Physics (INFN)',
  'provider_hosting_legal_entity-jelastic': 'Jelastic',
  'provider_hosting_legal_entity-jsc': 'Jülich Supercomputing Centre (JSC)',
  'provider_hosting_legal_entity-kit': 'Karlsruhe Institute of Technology (KIT)',
  'provider_hosting_legal_entity-komanord': 'Koma Nord',
  'provider_hosting_legal_entity-lsdufcg': 'Laboratório de Sistemas Distribuídos - Universidade Federal de Campina Grande (LSD-UFCG)',
  'provider_hosting_legal_entity-lnec': 'Laboratório Nacional de Engenharia Civil (LNEC)',
  'provider_hosting_legal_entity-tib': 'Leibniz Information Centre for Science and Technology (TIB)',
  'provider_hosting_legal_entity-libnovasl': 'LIBNOVA SL',
  'provider_hosting_legal_entity-lifewatcheric': 'LifeWatch ERIC',
  'provider_hosting_legal_entity-cirmmp': 'Magnetic Resonance Center of the University of Florence - CERM, Interuniversity consortium CIRMMP',
  'provider_hosting_legal_entity-mandati': 'Mandat International',
  'provider_hosting_legal_entity-mz': 'Materials Zone',
  'provider_hosting_legal_entity-meeo': 'Meteorological Environmental Earth Observation (MEEO)',
  'provider_hosting_legal_entity-msw': 'MyScienceWork',
  'provider_hosting_legal_entity-naesu': 'National Academy of Educational Sciences (NAES) of Ukraine',
  'provider_hosting_legal_entity-cines': 'National Computing Center for Higher Education (CINES)',
  'provider_hosting_legal_entity-incd': 'National Distributed Computing Infrastructure (INCD)',
  'provider_hosting_legal_entity-grnet': 'National Infrastructures for Research and Technology (GRNET)',
  'provider_hosting_legal_entity-niod': 'NIOD Institute for War, Genocide and Holocaust Studies',
  'provider_hosting_legal_entity-norce': 'NORCE Norwegian Research Centre',
  'provider_hosting_legal_entity-odp': 'Observatoire de Paris',
  'provider_hosting_legal_entity-olosa': 'OLOS Association',
  'provider_hosting_legal_entity-obp': 'Open Book Publishers (OBP)',
  'provider_hosting_legal_entity-okm': 'Open Knowledge Maps',
  'provider_hosting_legal_entity-openaire': 'OpenAIRE',
  'provider_hosting_legal_entity-operasaisbl': 'OPERAS AISBL',
  'provider_hosting_legal_entity-prace': 'Partnership For Advanced Computing in Europe (PRACE)',
  'provider_hosting_legal_entity-psnc': 'Poznan Supercomputing and Networking Center (PSNC)',
  'provider_hosting_legal_entity-pidssl': 'Predictia Intelligent Data Solutions SL',
  'provider_hosting_legal_entity-rasdaman': 'RASDAMAN',
  'provider_hosting_legal_entity-readcoop': 'READ-COOP SCE',
  'provider_hosting_legal_entity-rsu': 'Riga Stradins University',
  'provider_hosting_legal_entity-rbi': 'Ruđer Bošković Institute',
  'provider_hosting_legal_entity-ciemat': 'Scientific IT Research Activities and Knowledge, ICT Division, CIEMAT',
  'provider_hosting_legal_entity-sks': 'Scientific Knowledge Services (SKS)',
  'provider_hosting_legal_entity-scipedia': 'SCIPEDIA',
  'provider_hosting_legal_entity-seadatanet': 'SeaDataNet',
  'provider_hosting_legal_entity-sdgmbh': 'Secure Dimensions GmbH',
  'provider_hosting_legal_entity-sinergise': 'Sinergise',
  'provider_hosting_legal_entity-sirisasl': 'SIRIS Academic SL',
  'provider_hosting_legal_entity-sixsq': 'SixSq',
  'provider_hosting_legal_entity-suite5': 'Suite5 Data Intelligence Solutions',
  'provider_hosting_legal_entity-surf': 'SURF',
  'provider_hosting_legal_entity-cscs': 'Swiss National Supercomputing Centre (CSCS)',
  'provider_hosting_legal_entity-switch': 'SWITCH',
  'provider_hosting_legal_entity-soleil': 'Synchrotron SOLEIL',
  'provider_hosting_legal_entity-tsystems': 'T-Systems International',
  'provider_hosting_legal_entity-tut': 'Tallinn University of Technology',
  'provider_hosting_legal_entity-tm': 'Teledyne Marine',
  'provider_hosting_legal_entity-terradue': 'Terradue',
  'provider_hosting_legal_entity-tci': 'The Cyprus Institute',
  'provider_hosting_legal_entity-tos': 'Tree of Science',
  'provider_hosting_legal_entity-trustits': 'Trust-IT Services',
  'provider_hosting_legal_entity-tanic': 'Turkish Academic Network and Information Center',
  'provider_hosting_legal_entity-upltd': 'Ubiquity Press Ltd',
  'provider_hosting_legal_entity-ubiwhere': 'Ubiwhere',
  'provider_hosting_legal_entity-uit': 'UiT The Arctic University of Norway',
  'provider_hosting_legal_entity-ukaea': 'UK Atomic Energy Authority (UKAEA)',
  'provider_hosting_legal_entity-ukristfc': 'UK Research and Innovation - Science and Technology Facilities Council (UKRI - STFC)',
  'provider_hosting_legal_entity-upv': 'Universitat Politècnica de València',
  'provider_hosting_legal_entity-upf': 'Universitat Pompeu Fabra',
  'provider_hosting_legal_entity-ufdisitlab': 'University of Florence, DISIT Lab',
  'provider_hosting_legal_entity-uof': 'University of Freiburg',
  'provider_hosting_legal_entity-uog': 'University of Geneva',
  'provider_hosting_legal_entity-ugr': 'University of Granada – UGR',
  'provider_hosting_legal_entity-umb': 'University of Milano-Bicocca',
  'provider_hosting_legal_entity-umg': 'University of Minas Gerais',
  'provider_hosting_legal_entity-uoo': 'University of Oslo',
  'provider_hosting_legal_entity-uot': 'University of Tartu',
  'provider_hosting_legal_entity-vecma': 'Verified Exascale Computing for Multiscale Applications (VECMA)',
  'provider_hosting_legal_entity-vu': 'Vilnius University'
}

inv_hle = {v: k for k, v in hostingLegalEntityDict.items()}
inv_rp = {v: k for k, v in relatedPlatformsDict.items()}
##################################################### DICTIONARIES #####################################################


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
    providerId = provider.find('{http://einfracentral.eu}id')

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
    hostingLegalEntity = provider.find('{http://einfracentral.eu}hostingLegalEntity')
    if hostingLegalEntity is not None:
        try:
            hostingLegalEntity.text = inv_hle[hostingLegalEntity.text]
        except:
            print('Could not update the Hosting Legal Entity value ', hostingLegalEntity.text, 'for the Provider with id ', providerId)

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
    serviceId = service.find('{http://einfracentral.eu}id')

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
    serviceRelatedPlatforms = service.find('{http://einfracentral.eu}relatedPlatforms')
    if serviceRelatedPlatforms is not None:
        for entry in serviceRelatedPlatforms:
            if entry is not None:
                try:
                    entry.text = inv_rp[entry.text]
                except:
                    print('Could not update the Related Platform value ', entry.text, 'for the Service with id ', serviceId)

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