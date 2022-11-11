######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
######################################################## IMPORTS #######################################################

servicesToResearchCategories = {
"WorkflowHub": ["research_category-dro"],
"AMBER-based Portal Server for NMR structures (AMPS-NMR)": ["research_category-pa"],
"Plant Classification": ["research_category-acr"],
"OCRE Cloud Services by AWS": ["research_category-acr"],
"EGI Online Storage": ["research_category-mrd"],
"EDC EOxHub Workspace": ["research_category-mrd"],
"ePouta Virtual Private Cloud": ["research_category-acr"],
"100 Percent IT Trusted Cloud": ["research_category-acr"],
"PAN gitlab": ["research_category-acr","research_category-dro"],
"ARIS": ["research_category-dro"],
"European Cloud Hosting": ["research_category-dro "],
"Ubora": ["research_category-dro"],
"Open Knowledge Maps": ["research_category-acr"],
"INFN-Cloud Object Storage Service for DICE": ["research_category-acr"],
"MetaCentrum Cloud": ["research_category-mrd"],
"SurveyCodings.org": ["research_category-mrd"],
"cPouta Community Cloud": ["research_category-ari"],
"CSIC Cloud": ["research_category-dro"],
"EGI DataHub": ["research_category-mrd"],
"ARIS - Archival service": ["research_category-mrd"],
"Embassy Cloud": ["research_category-mrd"],
"UT Rocket": ["research_category-mrd"],
"CyVerse UK": ["research_category-mrd"],
"Arkivum Digital Archiving and Preservation Solution": ["research_category-mrd"],
"Open Energy Platform": ["research_category-mrd"],
"EGI Workload Manager": ["research_category-mrd"],
"robotbenchmark": ["research_category-mrd"],
"fedcloudclient: EGI FedCloud client": ["research_category-dro"],
"GPU Grant Program for scientific research projects and prospective startups": ["research_category-mrd"],
"IFCA-CSIC Cloud Infrastructure": ["research_category-mrd"],
"CSCS Object Storage": ["research_category-mrd"],
"Infrastructure Manager (IM)": ["research_category-mrd"],
"PROMINENCE": ["research_category-mrd"],
"SWITCHengines": ["research_category-acr"],
"Laniakea@ReCaS": ["research_category-mrd"],
"STFC Rucio Data Management Service": ["research_category-mrd"],
"Nuvla.io B2B SaaS edge-to-cloud management platform and marketplace of business applications": ["research_category-mrd"],
"EGI Cloud Container Compute": ["research_category-mrd"],
"FinisTerrae": ["research_category-acr"],
"SCIGNE Cloud Compute": ["research_category-acr"],
"Clouds Service": ["research_category-acr"],
"CloudFerro Infrastructure": ["research_category-acr"],
"EGI Cloud Compute": ["research_category-acr"],
"Rahti Container Cloud": ["research_category-acr"],
"EGI High-Throughput Compute": ["research_category-acr"],
"CLOUDIFIN": ["research_category-acr","research_category-ari"],
"PSI Remote Desktop Service": ["research_category-pa","research_category-ari"],
"PaaS Orchestrator": ["research_category-acr"],
"CESNET DataCare - Object Based Storage": ["research_category-mrd"],
"EGI Training Infrastructure": ["research_category-acr","research_category-atm"],
"B2DROP": ["research_category-mrd"],
"symbIoTe": ["research_category-dro","research_category-ari"],
"Dynamic On Demand Analysis Service (DODAS Portal)": ["research_category-pa"],
"RPrototypingLab Virtual Research Environment": ["research_category-pa"],
"LINDAT/CLARIAH-CZ Repository": ["research_category-dro","research_category-pro"],
"B2SHARE": ["research_category-pro"],
"RSU Dataverse": ["research_category-dro","research_category-pro"],
"Elastic Cloud Compute Cluster (EC3)": ["research_category-ari","research_category-acr"],
"Distributed Deep Learning by Horovod": ["research_category-ari"],
"PRACE Massive Open Online Courses (MOOC)": ["research_category-atm"],
"Pan-Learning.org": ["research_category-atm"],
"E-Learning Platform of GBIF Spain": ["research_category-atm"],
"eduMEET - Webbased videoconferencing platform": None,
"INFRAFRONTIER Training in mouse functional genomics": ["research_category-atm"],
"Open Science MOOC": ["research_category-atm"],
"PRACE Seasonal Schools and International Summer School": ["research_category-atm"],
"UBORA e-platform": ["research_category-atm"],
"EGI ISO 27001 Training": ["research_category-atm"],
"EGI FitSM Training": ["research_category-atm"],
"PRACE Training Portal": ["research_category-atm"],
"Digital production for conferences, workshops, roundtables and other academic and professional events": ["research_category-atm"],
"PRACE Training Centres": ["research_category-atm"],
"TRANSITS Training": ["research_category-atm"],
"DARIAH-Campus": ["research_category-atm"],
"Open Science Training": ["research_category-atm"],
"PRACE Advanced Training Centres": ["research_category-atm"],
"WORSICA - Water Monitoring Sentinel Cloud Platform": ["research_category-dro"],
"SSH Open Marketplace": ["research_category-dro"],
"Cloudferro Data related Services - EO Finder": ["research_category-dro"],
"ADAM Platform": ["research_category-dro"],
"STFC CVMFS Content Distribution Service": ["research_category-dro"],
"eduVPN": None,
"FANTEN (Finding Anisotropy TENsor)": ["research_category-pa"],
"NOMAD repository": ["research_category-dro"],
"European Marine Science OpenAIRE Community Gateway": ["research_category-dro"],
"The European Synchrotron Radiation Facility Data Portal": ["research_category-dro"],
"SIMBAD": ["research_category-dro"],
"GoTriple Discovery platform": ["research_category-dro"],
"Early Holocaust Testimony": ["research_category-dro"],
"Machine Translation": ["research_category-pa"],
"Climadjust": ["research_category-dro"],
"Greek Sustainable Development Solutions Network (SDSN) OpenAIRE Community Gateway": ["research_category-dro"],
"The Tromsø Repository of Language and Linguistics (TROLLing)": ["research_category-dro"],
"BDRC - Barcelona Dust Regional Center": ["research_category-dro"],
"INODE Open Data Dialog": ["research_category-dro"],
"GBIF Spain Species Portal": ["research_category-dro"],
"OpenCitations": ["research_category-dro"],
"Software Heritage archive": ["research_category-dro"],
"GBIF Spain Collections Registry": ["research_category-dro"],
"NiMMBus: Geospatial User Feedback": ["research_category-dro"],
"Cloudferro Data related Services - EO browser": ["research_category-dro"],
"eduGAIN": None,
"Diplomatic Reports": ["research_category-dro"],
"Europeana APIs": ["research_category-ari"],
"Argo marine floats dashboard, fleet monitoring": ["research_category-acr"],
"Argo marine floats OpenSearch API": ["research_category-acr"],
"BeGrenzte Flucht": ["research_category-dro"],
"GBIF Species Occurrence Data": ["research_category-dro"],
"O3as: ozone assessment": ["research_category-pa"],
"Web Panel Sample Service (WPSS) for the European Social Survey (ESS ERIC)": ["research_category-pa"],
"DisVis web portal": ["research_category-pa"],
"OpenAIRE Usage Counts": ["research_category-dro"],
"IRP2": ["research_category-dro"],
"Kuha2 metadata server": ["research_category-dro"],
"PaNOSC Software Catalogue": ["research_category-dro"],
"Multilingual Corpus of Survey Questionnaires": ["research_category-dro"],
"GBIF Portugal Occurrence Records": ["research_category-dro"],
"Thoth": ["research_category-mrd"],
"NameTag": ["research_category-mrd"],
"Bielefeld Academic Search Engine (BASE)": ["research_category-dro"],
"Identifiers.org Resolution Services": ["research_category-dro"],
"Identifiers.org": ["research_category-dro"],
"ADAM Space": ["research_category-dro"],
"SecureWatch": ["research_category-dro"],
"Cos4Bio": ["research_category-dro"],
"re3data - registry of research data repositories": ["research_category-dro"],
"Data discovery and access portal": ["research_category-dro"],
"forschungsdaten.info": ["research_category-mrd"],
"Ethnic and Migrant Minorities Survey Question Data Bank": ["research_category-dro"],
"EMSO ERIC Data Portal": ["research_category-dro"],
"Neuroinformatics OpenAIRE Community Gateway": ["research_category-dro"],
"OpenAIRE Research Community Dashboard (CONNECT)": ["research_category-dro"],
"SPACE-VIS ADN Service": ["research_category-pa"],
"TOPOS Observatory for Organisations": ["research_category-dro"],
"SeaDataNet Common Data Index (CDI)": ["research_category-dro"],
"PowerFit web portal": ["research_category-ari","research_category-pa"],
"OneDataSim": ["research_category-pa","research_category-pro","research_category-fie"],
"Materials Cloud Archive": ["research_category-dro","research_category-pro"],
"Services for Sensitive Data (TSD)": ["research_category-ari","research_category-pa"],
"DataverseNO": ["research_category-dro"],
"Data Management Expert Guide (DMEG)": ["research_category-mrd"],
"B2ACCESS": None,
"Digital Humanities and Cultural Heritage OpenAIRE Community Gateway": ["research_category-dro","research_category-pro"],
"RD-Connect GPAP": ["research_category-dro","research_category-pa","research_category-ari","research_category-pro"],
"Language Resource Switchboard": ["research_category-pa"],
"PRISM: Peer Review Information Service for Monographs": ["research_category-atm"],
"Data Service Portal Aila": ["research_category-dro"],
"VAMDC Portal": ["research_category-dro"],
"NI4OS-Europe repository service": ["research_category-dro"],
"TOPOS Observatory for Individuals": ["research_category-dro"],
"Jelastic Platform-as-a-Service": ["research_category-acr"],
"OpenAIRE Content Provider Dashboard": None,
"ElixirFM": ["research_category-pa"],
"ELSST – European Language Social Science Thesaurus": ["research_category-dro"],
"ARGOS": ["research_category-mrd"],
"Argo marine floats data discovery/download web": ["research_category-dro"],
"COLLABWITH MARKETPLACE": None,
"PSI Public Data Repository": ["research_category-dro"],
"Ethnic and Migrant Minorities Survey Registry": ["research_category-dro"],
"Argo marine floats data API": ["research_category-dro"],
"The EHRI Portal": ["research_category-dro"],
"European Social Survey (ESS) as a service": ["research_category-dro"],
"Argo marine floats metadata ERDDAP server": ["research_category-dro"],
"Argo marine floats vocabularies from NVS vocabulary server": ["research_category-mrd"],
"OPERAS Metrics service": ["research_category-dro"],
"Argo marine floats SPARQL endpoint": ["research_category-dro"],
"Nivola": ["research_category-acr"],
"FAIRsharing": ["research_category-dro","research_category-atm"],
"PRACE Code Vault": ["research_category-dro","research_category-atm"],
"EDP-Catalogue - Metadata Catalogue for environmental data discoverability": ["research_category-dro","research_category-atm"],
"Remote Monitoring and Smart Sensing": ["research_category-dro","research_category-pa"],
"VISA - Virtual Infrastructure for Scientific Analysis": ["research_category-mrd","research_category-ari"],
"UDPipe: tool for lemmatization, morphological analysis, POS tagging and dependency parsing in multiple languages": ["research_category-pa"],
"Verbal Aggression Analyser (VA Analyser)": ["research_category-pa"],
"ARIA (Access to Research Infrastructure Management)": ["research_category-ari"],
"MetalPDB: a database of metal-binding sites in 3D structures of biological macromolecules": ["research_category-dro"],
"EcoPortal": ["research_category-dro"],
"EISCAT data access portal": ["research_category-dro","research_category-acr"],
"Diamond Remote Desktop": ["research_category-pa"],
"WRiMS Taxon match": ["research_category-pa"],
"SeaDataNet European Directory of Marine Organisations (EDMO)": ["research_category-dro"],
"Recommendation API": None,
"SmartSMEAR": ["research_category-pa","research_category-mrd"],
"EODC JupyterHub for global Copernicus data": ["research_category-dro"],
"EOSC-Performance": ["research_category-acr"],
"Scientific publishing and Open Science Platform": ["research_category-dro","research_category-pro"],
"B2FIND": ["research_category-dro"],
"NI4OS-Europe Login": None,
"OPERAS Research for Society (Hypotheses)": ["research_category-dro"],
"eduTEAMS": None,
"Figshare": ["research_category-dro","research_category-pro"],
"UW-BAT": ["research_category-dro","research_category-pa"],
"Reduce and Visualize Gene Ontology": ["research_category-pa","research_category-dro"],
"de.NBI Cloud: Cloud Computing for Life Sciences": ["research_category-acr","research_category-pa","research_category-mrd"],
"TagMe": ["research_category-pa"],
"VD-Maps": ["research_category-pa"],
"UW-Mos": ["research_category-dro","research_category-pa"],
"PEMA Runner": ["research_category-acr","research_category-pa"],
"ATMO-STRESS": ["research_category-pa"],
"Jupyter Notebook can be used to create and share documents that contain live code, equations, visualizations, and text.": ["research_category-pa"],
"GBIF Spain Regions module": ["research_category-dro"],
"CIMPAL Calculator (Cumulative IMPacts of invasive ALien species calculator)": ["research_category-pa"],
"Open Science Observatory": None,
"OpenEBench": ["research_category-pa"],
"SAPS: Surface Energy Balance Automated Processing Service": ["research_category-dro","research_category-pa"],
"GBIF NIS Verifier": ["research_category-pa"],
"phytoplankton_eovs": ["research_category-pa"],
"Virtual Imaging Platform": ["research_category-pa"],
"SeaDataNet European Directory of the Cruise Summary Reports (CSR)": ["research_category-dro","research_category-pro"],
"OpenAPC": None,
"Chipster": ["research_category-pa"],
"WebODV - Online extraction, analysis and visualization of SeaDataNet and Argo data": ["research_category-pa"],
"Modelling Service for Water Supply Systems": ["research_category-pa"],
"ATMO-4CAST": ["research_category-pa"],
"PDB-Tools web": ["research_category-pa"],
"ENES Data Space": ["research_category-pa"],
"KER - Keyword Extractor": ["research_category-pa"],
"UMSA - Untargeted Mass Spectrometry data Analysis": ["research_category-pa"],
"Visual Media Service Virtual Research Environment": ["research_category-pa"],
"Pl@ntNet Identification Service": ["research_category-pa"],
"MorphoDiTa": ["research_category-pa"],
"ScipionCloud": ["research_category-pa"],
"OpenAIRE Funder Dashboard": None,
"Entity Matching Tool": ["research_category-pa"],
"WoRMS Taxon match": ["research_category-pa"],
"GBIF Spain Spatial Portal": ["research_category-pa"],
"OpenAIRE ScholeXplorer": ["research_category-dro"],
"Extractor Resampler and Masking": ["research_category-pa"],
"Data-driven Classifier": ["research_category-pa"],
"ATMO-FLUD": ["research_category-pa"],
"Multi-Messenger Online Data Analysis (MMODA)": ["research_category-pa"],
"Occurrences DataCube Analyst": ["research_category-pa"],
"Latent Space Explorer": ["research_category-pa","research_category-ari"],
"ARGO monitoring engine": None,
"SpotOn web portal": ["research_category-atm"],
"ENES Climate Analytics Service": ["research_category-pa","research_category-ari"],
"Environmental Data Extractor": ["research_category-pa"],
"Trophic Position Analyzer": ["research_category-pa"],
"Trophic Positions Modeler": ["research_category-pa"],
"Search API": ["research_category-dro"],
"PEMA Sequences Retriever": ["research_category-pa"],
"Enrichment API": ["research_category-pa"],
"Metabarcoding Occurrence Intersector": ["research_category-pa"],
"PhenoMeNal": ["research_category-pa","research_category-ari"],
"LOFAR Science Processing": ["research_category-pa"],
"Alien and Invasive Species Virtual Research Environment": ["research_category-pa"],
"AI4GEO Engine": ["research_category-pa","research_category-ari"],
"EGI Notebook": ["research_category-pa","research_category-ari"],
"UW-MAP": ["research_category-pa","research_category-ari"],
"Metabarcoding Runner": ["research_category-pa"],
"European Galaxy Server": ["research_category-ari"],
"e-IRG Knowledge Base": ["research_category-atm"],
"eduDNS: Dynamic DNS service for Academia": None,
"Polaris OS": ["research_category-mrd","research_category-pro"],
"Zenodo": ["research_category-pro","research_category-dro"],
"Episciences": ["research_category-pro","research_category-dro"],
"SeaDataNet DOI minting service": ["research_category-pro"],
"Dissemin": ["research_category-dro"],
"EHRI Document Blog": ["research_category-dro"],
"OpenAIRE Login": ["research_category-ari"],
"Digital Commons": None,
"SeaDataNet European Directory of Marine Environmental Data (EDMED)": ["research_category-ari"],
"B2HANDLE": ["research_category-mrd","research_category-dro"],
"VAMDC Species Database": ["research_category-mrd","research_category-dro"],
"OpenAIRE Validator": None,
"Research Organization Registry (ROR)": None,
"Dynamic DNS service": ["research_category-acr"],
"Technical support towards OpenAIRE compliance": None,
"Secret management service": ["research_category-acr"],
"SeaDataNet Vocabulary Services - underpinned by the NERC Vocabulary Server (NVS)": ["research_category-ari"],
"EGI Data Transfer": ["research_category-mrd"],
"Virtual Collection Registry": ["research_category-mrd"],
"SeaDataNet European Directory of Marine Environmental Research Projects (EDMERP)": ["research_category-pro","research_category-ari"],
"eTDR - European Trusted Digital Repository": ["research_category-dro","research_category-pa"],
"perfSONAR": None,
"DEMO Data Transfer": ["research_category-mrd"],
"Agora Resource Portfolio Management Tool": ["research_category-dro"],
"DMPonline": ["research_category-mrd"],
"OpenAIRE Mining Service": ["research_category-dro"],
"AMNESIA": ["research_category-pa","research_category-mrd"],
"Virtual Language Observatory": ["research_category-dro "],
"OpenAIRE Broker": None,
"SPACE-ML CAESAR service": ["research_category-pa"],
"Transkribus": ["research_category-pa","research_category-ari"],
"openRDM EU": ["research_category-mrd"],
"SPACE-VIS ViaLactea Service": ["research_category-pa"],
"DataCite DOI registration service": ["research_category-dro"],
"da|ra - DOI Registration Service for social science and economic data": ["research_category-dro"],
"Lagunas de Sierra Nevada / Glacier Lagoons of Sierra Nevada": ["research_category-pa","research_category-ari"],
"MOLGENIS": ["research_category-mrd","research_category-acr"],
"DEEP training facility": ["research_category-mrd","research_category-acr"],
"GBIF Spain Images Portal": ["research_category-mrd","research_category-acr"],
"B2SAFE": ["research_category-mrd","research_category-acr"],
"Open Telekom Cloud": ["research_category-mrd","research_category-acr","research_category-pa"],
"LIBNOVA LABDRIVE: The Ultimate Research Data Management and Digital Preservation Platform": ["research_category-mrd"],
"OpenBio.eu": ["research_category-dro","research_category-ari"],
"VAMDC Query Store": ["research_category-dro"],
"EODC Data Catalogue Service": ["research_category-dro"],
"Data Stewardship Wizard": ["research_category-mrd","research_category-dro"],
"GBIF Spain Occurrence Records": ["research_category-dro"],
"ROHub": ["research_category-mrd","research_category-dro","research_category-pro"],
"ISIDORE": ["research_category-dro"],
"Geohazards Exploitation Platform (GEP)": ["research_category-dro"],
"Biotope GRISS Extractor": ["research_category-dro"],
"ILL Data Portal": ["research_category-dro"],
"Snap4City": ["research_category-dro","research_category-pro"],
"CESSDA Data Catalogue": ["research_category-dro"],
"OpenAIRE Explore Portal": ["research_category-dro"],
"OpenAIRE Graph Access API": ["research_category-mrd","research_category-pa"],
"MOBIS - Mobile observation integration service": None,
"SeaDataNet European Directory of the Initial Ocean-Observing Systems (EDIOS)": ["research_category-dro"],
"CloudFerro Data Collections Catalog": ["research_category-dro","research_category-pa"],
"Open Research Knowledge Graph (ORKG)": ["research_category-dro","research_category-pa"],
"Sentinel Hub": ["research_category-dro","research_category-pa"],
"EnerMaps Data Management Tool": ["research_category-dro","research_category-pa"],
"GEO Discovery and Access Broker": ["research_category-dro"],
"LEMONADE - Live Exploration and Mining Of a Non-trivial Amount of Data from Everywhere": ["research_category-pa"],
"InAcademia": None,
"3DBionotes-WS": ["research_category-pa"],
"The National Open Access Research Data Archive (MIDAS)": ["research_category-pa"],
"OpenBioMaps": ["research_category-mrd","research_category-pa","research_category-acr"],
"Identifiers.org Central Registry": None,
"GÉANT Open": None,
"WiFiMon": None,
"Open Science Helpdesk": None,
"HADDOCK2.4 web portal": ["research_category-pa"],
"AUTHENIX": None,
"RvLab VRE": ["research_category-pa"],
"GÉANT L3VPN": None,
"Trusted Certificate Service": None,
"EGI Check-In": None,
"Oceanographic buoy Vida": ["research_category-dro","research_category-pa"],
"GEANT Sandbox Resource Profile": None,
"Biotope GBIF extractor": ["research_category-dro","research_category-pa"],
"Occurrences DataCube Builder": ["research_category-dro","research_category-pa"],
"Swiss eScience (Grid) Certificates": None,
"Guardomic": None,
"Piloting and co-design of Business Pilots": None,
"GÉANT Lambda": None,
"Argo marine floats metadata API": ["research_category-dro","research_category-ari"],
"GÉANT IP": None,
"GÉANT Plus": None,
"INDIGO Identity and Access Management (IAM)": None,
"eduroam": None,
"AiiDAlab": ["research_category-pa"],
"GÉANT MDVPN": None
}

##################################################### FUNCTIONS ########################################################
def service_migration(directory):
    migrationFolders = ['/service/', '/datasource/']
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                isVersion = False
                with open(directory + migrationFolder + file, 'r') as json_file:
                    json_data = migrate_research_categories(json_file, isVersion)
                    # write to file
                    with open(directory + migrationFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
            if file.endswith('-version'):
                isVersion = True
                versionFiles = os.listdir(directory + migrationFolder + file)
                for versionFile in versionFiles:
                    with open(directory + migrationFolder + file + '/' + versionFile, 'r') as json_file:
                        json_data = migrate_research_categories(json_file, isVersion)
                        # write to file
                        with open(directory + migrationFolder + file + '/' + versionFile, 'w') as json_file:
                            json.dump(json_data, json_file, indent=2)


def migrate_research_categories(json_file, isVersion):
    json_data = json.load(json_file)
    xml = json_data['payload']

    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    tree = root.getroot()

    resource = root.find('{http://einfracentral.eu}service')
    if resource is None:
        resource = root.find('{http://einfracentral.eu}datasource')
    resourceId = resource.find('{http://einfracentral.eu}id').text
    resourceName = resource.find('{http://einfracentral.eu}name').text
    if resourceName in servicesToResearchCategories:
        # migrate research categories
        resourceExtras = root.find('{http://einfracentral.eu}resourceExtras')
        if resourceExtras is not None:
            researchCategories = resourceExtras.find('{http://einfracentral.eu}researchCategories')
            if researchCategories is not None:
                resourceExtras.remove(researchCategories)
            newResearchCategories = ET.Element("tns:researchCategories")
            if servicesToResearchCategories[resourceName] is not None:
                for item in servicesToResearchCategories[resourceName]:
                    newResearchCategory = ET.Element("tns:researchCategory")
                    newResearchCategory.text = item
                    newResearchCategories.append(newResearchCategory)
                resourceExtras.append(newResearchCategories)
            # if not isVersion:
                # print("Migrated researchCategories of Resource: [", resourceId, "]-[", resourceName, "]")
        else:
            newResourceExtras = ET.Element("tns:resourceExtras")
            newResearchCategories = ET.Element("tns:researchCategories")
            if servicesToResearchCategories[resourceName] is not None:
                for item in servicesToResearchCategories[resourceName]:
                    newResearchCategory = ET.Element("tns:researchCategory")
                    newResearchCategory.text = item
                    newResearchCategories.append(newResearchCategory)
                newResourceExtras.append(newResearchCategories)
                tree.append(newResourceExtras)
            # if not isVersion:
                # print("Migrated researchCategories of Resource: [", resourceId, "]-[", resourceName, "]")
    else:
        if not isVersion:
            metadata = root.find('{http://einfracentral.eu}metadata')
            if metadata is not None:
                published = metadata.find('{http://einfracentral.eu}published')
                if published is not None:
                    if published.text == 'false':
                        print("Resource: [", resourceId, "]-[", resourceName, "] not found in the list")

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
service_migration(args.path)
######################################################## RUN ###########################################################