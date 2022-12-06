######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
######################################################## IMPORTS #######################################################

servicesToHorizontalServices = {
"WorkflowHub": None,
"AMBER-based Portal Server for NMR structures (AMPS-NMR)": None,
"Plant Classification": None,
"OCRE Cloud Services by Amazon Web Services ": "true",
"EGI Online Storage": "true",
"EDC EOxHub Workspace": "true",
"ePouta Virtual Private Cloud": "true",
"100 Percent IT Trusted Cloud": "true",
"PAN gitlab": None,
"ARIS": "true",
"European Cloud Hosting": "true",
"Open Knowledge Maps": "true",
"INFN-Cloud Object Storage Service for DICE": "true",
"MetaCentrum Cloud": "true",
"SurveyCodings.org": None,
"cPouta Community Cloud": "true",
"CSIC Cloud": "true",
"EGI DataHub": "true",
"ARIS - Archival service": "true",
"Embassy Cloud": None,
"UT Rocket": "true",
"CyVerse UK": "true",
"Arkivum Digital Archiving and Preservation Solution": "true",
"Open Energy Platform": None,
"EGI Workload Manager": "true",
"robotbenchmark": "true",
"fedcloudclient: EGI FedCloud client": "true",
"GPU Grant Program for scientific research projects and prospective startups": "true",
"IFCA-CSIC Cloud Infrastructure": "true",
"CSCS Object Storage": "true",
"Infrastructure Manager (IM)": "true",
"PROMINENCE": "true",
"SWITCHengines": "true",
"Laniakea@ReCaS": None,
"STFC Rucio Data Management Service": "true",
"Nuvla.io B2B SaaS edge-to-cloud management platform and marketplace of business applications": "true",
"EGI Cloud Container Compute": "true",
"FinisTerrae": "true",
"SCIGNE Cloud Compute": "true",
"Clouds Service": "true",
"CloudFerro Infrastructure": "true",
"EGI Cloud Compute": None,
"Rahti Container Cloud": "true",
"EGI High-Throughput Compute": "true",
"CLOUDIFIN": "true",
"PSI Remote Desktop Service": None,
"PaaS Orchestrator ": "true",
"CESNET DataCare - Object Based Storage": "true",
"EGI Training Infrastructure": "true",
"B2DROP": "true",
"symbIoTe": "true",
"Dynamic On Demand Analysis Service (DODAS Portal)": "true",
"RPrototypingLab Virtual Research Environment": None,
"LINDAT/CLARIAH-CZ Repository": None,
"B2SHARE": "true",
"RSU Dataverse": "true",
"Elastic Cloud Compute Cluster (EC3)": "true",
"Distributed Deep Learning by Horovod": None,
"PRACE Massive Open Online Courses (MOOC)": "true",
"PaN-Training e-Learning Platform": None,
"E-Learning Platform of GBIF Spain": None,
"eduMEET - Webbased videoconferencing platform": "true",
"INFRAFRONTIER Training in mouse functional genomics": None,
"Open Science MOOC": "true",
"PRACE Seasonal Schools and International Summer School": "true",
"UBORA e-platform": None,
"EGI ISO 27001 Training": "true",
"EGI FitSM Training": "true",
"PRACE Training Portal": "true",
"Digital production for conferences, workshops, roundtables and other academic and professional events": "true",
"PRACE Training Centres": "true",
"TRANSITS Training": "true",
"DARIAH-Campus": None,
"Open Science Training": "true",
"PRACE Advanced Training Centres": "true",
"WORSICA - Water Monitoring Sentinel Cloud Platform": None,
"SSH Open Marketplace": None,
"Cloudferro Data related Services - EO Finder": None,
"ADAM Platform": None,
"STFC CVMFS Content Distribution Service": "true",
"eduVPN": "true",
"FANTEN\t (Finding Anisotropy TENsor)\t  ": None,
"NOMAD repository": None,
"European Marine Science OpenAIRE Community Gateway": "true",
"The European Synchrotron Radiation Facility Data Portal": None,
"SIMBAD": None,
"GoTriple Discovery platform": None,
"Early Holocaust Testimony": None,
"Machine Translation": None,
"Climadjust": None,
"Greek Sustainable Development Solutions Network (SDSN) OpenAIRE Community Gateway": "true",
"The Tromsø Repository of Language and Linguistics (TROLLing)": None,
"BDRC - Barcelona Dust Regional Center": None,
"INODE Open Data Dialog": "true",
"GBIF Spain Species Portal": None,
"OpenCitations": "true",
"Software Heritage archive": "true",
"GBIF Spain Collections Registry": None,
"NiMMBus: Geospatial User Feedback": None,
"Cloudferro Data related Services - EO browser": None,
"eduGAIN": "true",
"Diplomatic Reports": None,
"Europeana APIs": None,
"Argo marine floats dashboard, fleet monitoring": None,
"Argo marine floats OpenSearch API": None,
"BeGrenzte Flucht": None,
"GBIF Species Occurrence Data": None,
"O3as: ozone assessment": None,
"Web Panel Sample Service (WPSS) for the European Social Survey (ESS ERIC)": None,
"DisVis web portal": None,
"OpenAIRE Usage Counts": "true",
"IRP2": None,
"Kuha2 metadata server": None,
"PaNOSC Software Catalogue": None,
"Multilingual Corpus of Survey Questionnaires ": None,
"GBIF Portugal Occurrence Records": None,
"Thoth": "true",
"NameTag": None,
"Bielefeld Academic Search Engine (BASE)": "true",
"Identifiers.org Resolution Services": None,
"Identifiers.org": "true",
"ADAM Space": None,
"SecureWatch": None,
"Cos4Bio": None,
"re3data - registry of research data repositories": "true",
"Data discovery and access portal": None,
"forschungsdaten.info": "true",
"Ethnic and Migrant Minorities Survey Question Data Bank": None,
"EMSO ERIC Data Portal": None,
"Neuroinformatics OpenAIRE Community Gateway": "true",
"OpenAIRE Research Community Dashboard (CONNECT)": "true",
"SPACE-VIS ADN Service": None,
"TOPOS Observatory for Organisations": "true",
"SeaDataNet Common Data Index (CDI) user interface": None,
"PowerFit web portal": None,
"OneDataSim": None,
"Materials Cloud Archive": None,
"Services for Sensitive Data (TSD)": None,
"DataverseNO": "true",
"Data Management Expert Guide (DMEG)": None,
"B2ACCESS": "true",
"Digital Humanities and Cultural Heritage OpenAIRE Community Gateway": None,
"RD-Connect GPAP": None,
"Language Resource Switchboard": None,
"PRISM: Peer Review Information Service for Monographs": None,
"Data Service Portal Aila": None,
"VAMDC Portal": None,
"NI4OS-Europe repository service": "true",
"TOPOS Observatory for Individuals": None,
"Jelastic Platform-as-a-Service": "true",
"OpenAIRE Content Provider Dashboard": "true",
"ElixirFM": None,
"ELSST – European Language Social Science Thesaurus": None,
"ARGOS": "true",
"Argo marine floats data discovery/download web": None,
"COLLABWITH MARKETPLACE": "true",
"PSI Public Data Repository": None,
"Ethnic and Migrant Minorities Survey Registry": None,
"Argo marine floats data API": None,
"The EHRI Portal": None,
"European Social Survey (ESS) as a service": None,
"Argo marine floats metadata ERDDAP server": None,
"Argo marine floats vocabularies from NVS vocabulary server": None,
"OPERAS Metrics service": None,
"Argo marine floats SPARQL endpoint": None,
"Nivola": "true",
"FAIRsharing": "true",
"PRACE Code Vault": "true",
"EDP-Catalogue - Metadata Catalogue for environmental data discoverability": None,
"Remote Monitoring and Smart Sensing": None,
"VISA - Virtual Infrastructure for Scientific Analysis": None,
"UDPipe: tool for lemmatization, morphological analysis, POS tagging and dependency parsing in multiple languages": None,
"Verbal Aggression Analyser (VA Analyser)": None,
"ARIA (Access to Research Infrastructure Management)": None,
"MetalPDB: a database of metal-binding sites in 3D structures of biological macromolecules": None,
"EcoPortal": None,
"EISCAT data access portal": None,
"Diamond Remote Desktop": None,
"WRiMS Taxon match": None,
"SeaDataNet European Directory of Marine Organisations (EDMO)": None,
"Recommendation API": None,
"SmartSMEAR": None,
"EODC JupyterHub for global Copernicus data": None,
"EOSC-Performance": "true",
" Scientific publishing and Open Science Platform": "true",
"B2FIND": "true",
"NI4OS-Europe Login": "true",
"OPERAS Research for Society (Hypotheses)": None,
"eduTEAMS": "true",
"Figshare": "true",
"UW-BAT": None,
"Reduce and Visualize Gene Ontology": None,
"de.NBI Cloud: Cloud Computing for Life Sciences": None,
"TagMe": None,
"VD-Maps": "true",
"UW-Mos": None,
"PEMA Runner": None,
"ATMO-STRESS": None,
"Jupyter Notebook can be used to create and share documents that contain live code, equations, visualizations, and text.": None,
"GBIF Spain Regions module": None,
"CIMPAL Calculator (Cumulative IMPacts of invasive ALien species calculator)": None,
"Open Science Observatory": "true",
"OpenEBench": None,
"SAPS: Surface Energy Balance Automated Processing Service": None,
"GBIF NIS Verifier": None,
"Phytoplankton EOVs": None,
"Virtual Imaging Platform": None,
"SeaDataNet European Directory of the Cruise Summary Reports (CSR)": None,
"OpenAPC": "true",
"Chipster": "true",
"WebODV - Online extraction, analysis and visualization of SeaDataNet and Argo data": None,
"Modelling Service for Water Supply Systems": None,
"ATMO-4CAST": None,
"PDB-Tools web": None,
"ENES Data Space": None,
"KER - Keyword Extractor": None,
"UMSA - Untargeted Mass Spectrometry data Analysis": None,
"Visual Media Service Virtual Research Environment": "true",
"Pl@ntNet Identification Service": None,
"MorphoDiTa": None,
"ScipionCloud": None,
"OpenAIRE Funder Dashboard": "true",
"Entity Matching Tool": None,
"WoRMS Taxon match": None,
"GBIF Spain Spatial Portal": None,
"OpenAIRE ScholeXplorer": "true",
"Extractor Resampler and Masking": None,
"Data-driven Classifier": None,
"ATMO-FLUD": None,
"Multi-Messenger Online Data Analysis (MMODA)": None,
"Occurrences DataCube Analyst": None,
"Latent Space Explorer": "true",
"ARGO monitoring engine": "true",
"SpotOn web portal": None,
"ENES Climate Analytics Service": None,
"Environmental Data Extractor": None,
"Trophic Position Analyzer": None,
"Trophic Positions Modeler": None,
"Search API": None,
"PEMA Sequences Retriever": None,
"Enrichment API": None,
"Metabarcoding Occurrence Intersector": None,
"PhenoMeNal": None,
"LOFAR Science Processing": None,
"Alien and Invasive Species Virtual Research Environment": None,
"AI4GEO Engine": None,
"EGI Notebook": "true",
"UW-MAP": None,
"Metabarcoding Runner": None,
"European Galaxy Server": None,
"e-IRG Knowledge Base": "true",
"eduDNS: Dynamic DNS service for Academia": "true",
"Polaris OS": "true",
"Zenodo": "true",
"Episciences": "true",
"SeaDataNet DOI minting service": None,
"Dissemin": "true",
"EHRI Document Blog": None,
"OpenAIRE Login": "true",
"Digital Commons": "true",
"SeaDataNet European Directory of Marine Environmental Data (EDMED)": None,
"B2HANDLE": "true",
"VAMDC Species Database": None,
"OpenAIRE Validator": "true",
"Research Organization Registry (ROR)": "true",
"Dynamic DNS service": "true",
"Technical support towards OpenAIRE compliance": "true",
"Secret management service": "true",
"SeaDataNet Vocabulary Services - underpinned by the NERC Vocabulary Server (NVS)": None,
"EGI Data Transfer": "true",
"Virtual Collection Registry": None,
"SeaDataNet European Directory of Marine Environmental Research Projects (EDMERP)": None,
"eTDR - European Trusted Digital Repository": "true",
"perfSONAR": "true",
"DEMO Data Transfer": "true",
"Agora Resource Portfolio Management Tool": "true",
"DMPonline": "true",
"OpenAIRE Mining Service": "true",
"AMNESIA": "true",
"Virtual Language Observatory": None,
"OpenAIRE Broker": "true",
"SPACE-ML CAESAR service": None,
"Transkribus": None,
"openRDM EU": "true",
"SPACE-VIS ViaLactea Service": None,
"DataCite DOI registration service": "true",
"da|ra - DOI Registration Service for social science and economic data": None,
"Lagunas de Sierra Nevada / Glacier Lagoons of Sierra Nevada": None,
"MOLGENIS": None,
"DEEP training facility": "true",
"GBIF Spain Images Portal": None,
"B2SAFE": "true",
"Open Telekom Cloud": "true",
"LIBNOVA LABDRIVE: The Ultimate Research Data Management and Digital Preservation Platform": "true",
"OpenBio.eu": None,
"VAMDC Query Store": "true",
"EODC Data Catalogue Service": None,
"Data Stewardship Wizard": "true",
"GBIF Spain Occurrence Records": None,
"ROHub": None,
"ISIDORE": None,
"Geohazards Exploitation Platform (GEP)": None,
"Biotope GRISS Extractor": None,
"ILL Data Portal": None,
"Snap4City": None,
"CESSDA Data Catalogue": None,
"OpenAIRE Explore Portal": "true",
"OpenAIRE Graph Access API": "true",
"MOBIS - Mobile observation integration service": None,
"SeaDataNet European Directory of the Initial Ocean-Observing Systems (EDIOS)": None,
"CloudFerro Data Collections Catalog": None,
"Open Research Knowledge Graph (ORKG)": "true",
"Sentinel Hub": None,
"EnerMaps Data Management Tool": "true",
"GEO Discovery and Access Broker": None,
"LEMONADE - Live Exploration and Mining Of a Non-trivial Amount of Data from Everywhere": None,
"InAcademia": "true",
"3DBionotes-WS": None,
"The National Open Access Research Data Archive (MIDAS)": None,
"OpenBioMaps": None,
"Identifiers.org Central Registry": "true",
"GÉANT Open": "true",
"WiFiMon": "true",
"Open Science Helpdesk": "true",
"HADDOCK2.4 web portal": None,
"AUTHENIX": "true",
"RvLab VRE": None,
"GÉANT L3VPN": "true",
"Trusted Certificate Service": "true",
"EGI Check-In": "true",
"Oceanographic buoy Vida": None,
"GEANT Sandbox Resource Profile": "true",
"Biotope GBIF extractor": None,
"Occurrences DataCube Builder ": None,
"Swiss eScience (Grid) Certificates": "true",
"Guardomic": "true",
"Piloting and co-design of Business Pilots": "true",
"GÉANT Lambda": "true",
"Argo marine floats metadata API": None,
"GÉANT IP": "true",
"GÉANT Plus": "true",
"INDIGO Identity and Access Management (IAM) ": "true",
"eduroam": "true",
"AiiDAlab": "true",
"GÉANT MDVPN": "true"
}

horizontalServicesRelatedTags = {
"WorkflowHub": None,
"AMBER-based Portal Server for NMR structures (AMPS-NMR)": None,
"Plant Classification": None,
"OCRE Cloud Services by Amazon Web Services ": "e-INFRA GEANT",
"EGI Online Storage": "e-INFRA EGI",
"EDC EOxHub Workspace": "e-INFRA",
"ePouta Virtual Private Cloud": "e-INFRA EUDAT",
"100 Percent IT Trusted Cloud": "e-INFRA EGI",
"PAN gitlab": None,
"ARIS": "e-INFRA GEANT",
"European Cloud Hosting": "e-INFRA",
"Open Knowledge Maps": "e-INFRA (Libraries)",
"INFN-Cloud Object Storage Service for DICE": "e-INFRA EUDAT",
"MetaCentrum Cloud": "e-INFRA",
"SurveyCodings.org": None,
"cPouta Community Cloud": "e-INFRA EUDAT",
"CSIC Cloud": "e-INFRA EUDAT",
"EGI DataHub": "e-INFRA EGI",
"ARIS - Archival service": "e-INFRA EUDAT",
"Embassy Cloud": None,
"UT Rocket": "e-INFRA GEANT",
"CyVerse UK": "e-INFRA",
"Arkivum Digital Archiving and Preservation Solution": "e-INFRA Commercial",
"Open Energy Platform": None,
"EGI Workload Manager": "e-INFRA EGI",
"robotbenchmark": "e-INFRA",
"fedcloudclient: EGI FedCloud client": "e-INFRA EGI",
"GPU Grant Program for scientific research projects and prospective startups": "e-INFRA Commercial",
"IFCA-CSIC Cloud Infrastructure": "e-INFRA",
"CSCS Object Storage": "e-INFRA",
"Infrastructure Manager (IM)": "e-INFRA",
"PROMINENCE": "e-INFRA",
"SWITCHengines": "e-INFRA non-commercial",
"Laniakea@ReCaS": None,
"STFC Rucio Data Management Service": "e-INFRA non-commercial",
"Nuvla.io B2B SaaS edge-to-cloud management platform and marketplace of business applications": "e-INFRA Commercial",
"EGI Cloud Container Compute": "e-INFRA EGI",
"FinisTerrae": "e-INFRA non-commercial",
"SCIGNE Cloud Compute": "e-INFRA non-commercial",
"Clouds Service": "e-INFRA GEANT",
"CloudFerro Infrastructure": "e-INFRA non-commercial",
"EGI Cloud Compute": None,
"Rahti Container Cloud": "e-INFRA non-commercial",
"EGI High-Throughput Compute": "e-INFRA EGI",
"CLOUDIFIN": "e-INFRA non-commercial",
"PSI Remote Desktop Service": None,
"PaaS Orchestrator ": "e-INFRA non-commercial",
"CESNET DataCare - Object Based Storage": "e-INFRA non-commercial",
"EGI Training Infrastructure": "e-INFRA EGI",
"B2DROP": "e-INFRA EUDAT",
"symbIoTe": "e-INFRA non-commercial",
"Dynamic On Demand Analysis Service (DODAS Portal)": "e-INFRA non-commercial",
"RPrototypingLab Virtual Research Environment": None,
"LINDAT/CLARIAH-CZ Repository": None,
"B2SHARE": "e-INFRA EUDAT",
"RSU Dataverse": "e-INFRA non-commercial",
"Elastic Cloud Compute Cluster (EC3)": "e-INFRA EGI",
"Distributed Deep Learning by Horovod": None,
"PRACE Massive Open Online Courses (MOOC)": "e-INFRA PRACE",
"PaN-Training e-Learning Platform": None,
"E-Learning Platform of GBIF Spain": None,
"eduMEET - Webbased videoconferencing platform": "e-INFRA GEANT",
"INFRAFRONTIER Training in mouse functional genomics": None,
"Open Science MOOC": "e-INFRA non-commercial",
"PRACE Seasonal Schools and International Summer School": "e-INFRA PRACE",
"UBORA e-platform": None,
"EGI ISO 27001 Training": "e-INFRA EGI",
"EGI FitSM Training": "e-INFRA EGI",
"PRACE Training Portal": "e-INFRA PRACE",
"Digital production for conferences, workshops, roundtables and other academic and professional events": "e-INFRA non-commercial",
"PRACE Training Centres": "e-INFRA PRACE",
"TRANSITS Training": "e-INFRA GEANT",
"DARIAH-Campus": None,
"Open Science Training": "e-INFRA OpenAIRE",
"PRACE Advanced Training Centres": "e-INFRA PRACE",
"WORSICA - Water Monitoring Sentinel Cloud Platform": None,
"SSH Open Marketplace": None,
"Cloudferro Data related Services - EO Finder": None,
"ADAM Platform": None,
"STFC CVMFS Content Distribution Service": "e-INFRA non-commercial",
"eduVPN": "e-INFRA non-commercial",
"FANTEN\t (Finding Anisotropy TENsor)\t  ": None,
"NOMAD repository": None,
"European Marine Science OpenAIRE Community Gateway": "e-INFRA OpenAIRE",
"The European Synchrotron Radiation Facility Data Portal": None,
"SIMBAD": None,
"GoTriple Discovery platform": None,
"Early Holocaust Testimony": None,
"Machine Translation": None,
"Climadjust": None,
"Greek Sustainable Development Solutions Network (SDSN) OpenAIRE Community Gateway": "e-INFRA OpenAIRE",
"The Tromsø Repository of Language and Linguistics (TROLLing)": None,
"BDRC - Barcelona Dust Regional Center": None,
"INODE Open Data Dialog": "e-INFRA non-commercial",
"GBIF Spain Species Portal": None,
"OpenCitations": "e-INFRA non-commercial",
"Software Heritage archive": "e-INFRA non-commercial",
"GBIF Spain Collections Registry": None,
"NiMMBus: Geospatial User Feedback": None,
"Cloudferro Data related Services - EO browser": None,
"eduGAIN": "e-INFRA GEANT",
"Diplomatic Reports": None,
"Europeana APIs": None,
"Argo marine floats dashboard, fleet monitoring": None,
"Argo marine floats OpenSearch API": None,
"BeGrenzte Flucht": None,
"GBIF Species Occurrence Data": None,
"O3as: ozone assessment": None,
"Web Panel Sample Service (WPSS) for the European Social Survey (ESS ERIC)": None,
"DisVis web portal": None,
"OpenAIRE Usage Counts": "e-INFRA OpenAIRE",
"IRP2": None,
"Kuha2 metadata server": None,
"PaNOSC Software Catalogue": None,
"Multilingual Corpus of Survey Questionnaires ": None,
"GBIF Portugal Occurrence Records": None,
"Thoth": "e-INFRA non-commercial",
"NameTag": None,
"Bielefeld Academic Search Engine (BASE)": "e-INFRA non-commercial",
"Identifiers.org Resolution Services": None,
"Identifiers.org": "e-INFRA non-commercial",
"ADAM Space": None,
"SecureWatch": None,
"Cos4Bio": None,
"re3data - registry of research data repositories": "e-INFRA non-commercial",
"Data discovery and access portal": None,
"forschungsdaten.info": "e-INFRA non-commercial",
"Ethnic and Migrant Minorities Survey Question Data Bank": None,
"EMSO ERIC Data Portal": None,
"Neuroinformatics OpenAIRE Community Gateway": "e-INFRA OpenAIRE",
"OpenAIRE Research Community Dashboard (CONNECT)": "e-INFRA OpenAIRE",
"SPACE-VIS ADN Service": None,
"TOPOS Observatory for Organisations": "e-INFRA OpenAIRE",
"SeaDataNet Common Data Index (CDI) user interface": None,
"PowerFit web portal": None,
"OneDataSim": None,
"Materials Cloud Archive": None,
"Services for Sensitive Data (TSD)": None,
"DataverseNO": "e-INFRA non-commercial",
"Data Management Expert Guide (DMEG)": None,
"B2ACCESS": "e-INFRA EUDAT",
"Digital Humanities and Cultural Heritage OpenAIRE Community Gateway": None,
"RD-Connect GPAP": None,
"Language Resource Switchboard": None,
"PRISM: Peer Review Information Service for Monographs": None,
"Data Service Portal Aila": None,
"VAMDC Portal": None,
"NI4OS-Europe repository service": "e-INFRA non-commercial",
"TOPOS Observatory for Individuals": None,
"Jelastic Platform-as-a-Service": "e-INFRA commercial",
"OpenAIRE Content Provider Dashboard": "e-INFRA OpenAIRE",
"ElixirFM": None,
"ELSST – European Language Social Science Thesaurus": None,
"ARGOS": "e-INFRA OpenAIRE",
"Argo marine floats data discovery/download web": None,
"COLLABWITH MARKETPLACE": "e-INFRA commercial",
"PSI Public Data Repository": None,
"Ethnic and Migrant Minorities Survey Registry": None,
"Argo marine floats data API": None,
"The EHRI Portal": None,
"European Social Survey (ESS) as a service": None,
"Argo marine floats metadata ERDDAP server": None,
"Argo marine floats vocabularies from NVS vocabulary server": None,
"OPERAS Metrics service": None,
"Argo marine floats SPARQL endpoint": None,
"Nivola": "e-INFRA non-commercial",
"FAIRsharing": "e-INFRA non-commercial",
"PRACE Code Vault": "e-INFRA PRACE",
"EDP-Catalogue - Metadata Catalogue for environmental data discoverability": None,
"Remote Monitoring and Smart Sensing": None,
"VISA - Virtual Infrastructure for Scientific Analysis": None,
"UDPipe: tool for lemmatization, morphological analysis, POS tagging and dependency parsing in multiple languages": None,
"Verbal Aggression Analyser (VA Analyser)": None,
"ARIA (Access to Research Infrastructure Management)": None,
"MetalPDB: a database of metal-binding sites in 3D structures of biological macromolecules": None,
"EcoPortal": None,
"EISCAT data access portal": None,
"Diamond Remote Desktop": None,
"WRiMS Taxon match": None,
"SeaDataNet European Directory of Marine Organisations (EDMO)": None,
"Recommendation API": None,
"SmartSMEAR": None,
"EODC JupyterHub for global Copernicus data": None,
"EOSC-Performance": "e-INFRA non-commercial",
" Scientific publishing and Open Science Platform": "e-INFRA non-commercial",
"B2FIND": "e-INFRA EUDAT",
"NI4OS-Europe Login": "e-INFRA non-commercial",
"OPERAS Research for Society (Hypotheses)": None,
"eduTEAMS": "e-INFRA GEANT",
"Figshare": "e-INFRA commercial",
"UW-BAT": None,
"Reduce and Visualize Gene Ontology": None,
"de.NBI Cloud: Cloud Computing for Life Sciences": None,
"TagMe": None,
"VD-Maps": "e-INFRA non-commercial",
"UW-Mos": None,
"PEMA Runner": None,
"ATMO-STRESS": None,
"Jupyter Notebook can be used to create and share documents that contain live code, equations, visualizations, and text.": None,
"GBIF Spain Regions module": None,
"CIMPAL Calculator (Cumulative IMPacts of invasive ALien species calculator)": None,
"Open Science Observatory": "e-INFRA OpenAIRE",
"OpenEBench": None,
"SAPS: Surface Energy Balance Automated Processing Service": None,
"GBIF NIS Verifier": None,
"Phytoplankton EOVs": None,
"Virtual Imaging Platform": None,
"SeaDataNet European Directory of the Cruise Summary Reports (CSR)": None,
"OpenAPC": "e-INFRA non-commercial",
"Chipster": "e-INFRA non-commercial",
"WebODV - Online extraction, analysis and visualization of SeaDataNet and Argo data": None,
"Modelling Service for Water Supply Systems": None,
"ATMO-4CAST": None,
"PDB-Tools web": None,
"ENES Data Space": None,
"KER - Keyword Extractor": None,
"UMSA - Untargeted Mass Spectrometry data Analysis": None,
"Visual Media Service Virtual Research Environment": "e-INFRA non-commercial",
"Pl@ntNet Identification Service": None,
"MorphoDiTa": None,
"ScipionCloud": None,
"OpenAIRE Funder Dashboard": "e-INFRA OpenAIRE",
"Entity Matching Tool": None,
"WoRMS Taxon match": None,
"GBIF Spain Spatial Portal": None,
"OpenAIRE ScholeXplorer": "e-INFRA OpenAIRE",
"Extractor Resampler and Masking": None,
"Data-driven Classifier": None,
"ATMO-FLUD": None,
"Multi-Messenger Online Data Analysis (MMODA)": None,
"Occurrences DataCube Analyst": None,
"Latent Space Explorer": "e-INFRA non-commercial",
"ARGO monitoring engine": "e-INFRA non-commercial",
"SpotOn web portal": None,
"ENES Climate Analytics Service": None,
"Environmental Data Extractor": None,
"Trophic Position Analyzer": None,
"Trophic Positions Modeler": None,
"Search API": None,
"PEMA Sequences Retriever": None,
"Enrichment API": None,
"Metabarcoding Occurrence Intersector": None,
"PhenoMeNal": None,
"LOFAR Science Processing": None,
"Alien and Invasive Species Virtual Research Environment": None,
"AI4GEO Engine": None,
"EGI Notebook": "e-INFRA EGI",
"UW-MAP": None,
"Metabarcoding Runner": None,
"European Galaxy Server": None,
"e-IRG Knowledge Base": "e-INFRA non-commercial",
"eduDNS: Dynamic DNS service for Academia": "e-INFRA GEANT",
"Polaris OS": "e-INFRA commercial",
"Zenodo": "e-INFRA non-commercial",
"Episciences": "e-INFRA non-commercial",
"SeaDataNet DOI minting service": None,
"Dissemin": "e-INFRA non-commercial",
"EHRI Document Blog": None,
"OpenAIRE Login": "e-INFRA OpenAIRE",
"Digital Commons": "e-INFRA commercial",
"SeaDataNet European Directory of Marine Environmental Data (EDMED)": None,
"B2HANDLE": "e-INFRA EUDAT",
"VAMDC Species Database": None,
"OpenAIRE Validator": "e-INFRA OpenAIRE",
"Research Organization Registry (ROR)": "e-INFRA non-commercial",
"Dynamic DNS service": "e-INFRA EGI",
"Technical support towards OpenAIRE compliance": "e-INFRA OpenAIRE",
"Secret management service": "e-INFRA EGI",
"SeaDataNet Vocabulary Services - underpinned by the NERC Vocabulary Server (NVS)": None,
"EGI Data Transfer": "e-INFRA EGI",
"Virtual Collection Registry": None,
"SeaDataNet European Directory of Marine Environmental Research Projects (EDMERP)": None,
"eTDR - European Trusted Digital Repository": "e-INFRA EUDAT",
"perfSONAR": "e-INFRA GEANT",
"DEMO Data Transfer": "e-INFRA EGI",
"Agora Resource Portfolio Management Tool": "e-INFRA non-commercial",
"DMPonline": "e-INFRA non-commercial",
"OpenAIRE Mining Service": "e-INFRA OpenAIRE",
"AMNESIA": "e-INFRA OpenAIRE",
"Virtual Language Observatory": None,
"OpenAIRE Broker": "e-INFRA OpenAIRE",
"SPACE-ML CAESAR service": None,
"Transkribus": None,
"openRDM EU": "e-INFRA non-commercial",
"SPACE-VIS ViaLactea Service": None,
"DataCite DOI registration service": "e-INFRA non-commercial",
"da|ra - DOI Registration Service for social science and economic data": None,
"Lagunas de Sierra Nevada / Glacier Lagoons of Sierra Nevada": None,
"MOLGENIS": None,
"DEEP training facility": "e-INFRA non-commercial",
"GBIF Spain Images Portal": None,
"B2SAFE": "e-INFRA EUDAT",
"Open Telekom Cloud": "e-INFRA commercial",
"LIBNOVA LABDRIVE: The Ultimate Research Data Management and Digital Preservation Platform": "e-INFRA commercial",
"OpenBio.eu": None,
"VAMDC Query Store": "e-INFRA non-commercial",
"EODC Data Catalogue Service": None,
"Data Stewardship Wizard": "e-INFRA non-commercial",
"GBIF Spain Occurrence Records": None,
"ROHub": None,
"ISIDORE": None,
"Geohazards Exploitation Platform (GEP)": None,
"Biotope GRISS Extractor": None,
"ILL Data Portal": None,
"Snap4City": None,
"CESSDA Data Catalogue": None,
"OpenAIRE Explore Portal": "e-INFRA OpenAIRE",
"OpenAIRE Graph Access API": "e-INFRA OpenAIRE",
"MOBIS - Mobile observation integration service": None,
"SeaDataNet European Directory of the Initial Ocean-Observing Systems (EDIOS)": None,
"CloudFerro Data Collections Catalog": None,
"Open Research Knowledge Graph (ORKG)": "e-INFRA OpenAIRE",
"Sentinel Hub": None,
"EnerMaps Data Management Tool": "e-INFRA OpenAIRE",
"GEO Discovery and Access Broker": None,
"LEMONADE - Live Exploration and Mining Of a Non-trivial Amount of Data from Everywhere": None,
"InAcademia": "e-INFRA GEANT",
"3DBionotes-WS": None,
"The National Open Access Research Data Archive (MIDAS)": None,
"OpenBioMaps": None,
"Identifiers.org Central Registry": "e-INFRA non-commercial",
"GÉANT Open": "e-INFRA GEANT",
"WiFiMon": "e-INFRA GEANT",
"Open Science Helpdesk": "e-INFRA OpenAIRE",
"HADDOCK2.4 web portal": None,
"AUTHENIX": "e-INFRA non-commercial",
"RvLab VRE": None,
"GÉANT L3VPN": "e-INFRA GEANT",
"Trusted Certificate Service": "e-INFRA GEANT",
"EGI Check-In": "e-INFRA EGI",
"Oceanographic buoy Vida": None,
"GEANT Sandbox Resource Profile": "e-INFRA GEANT",
"Biotope GBIF extractor": None,
"Occurrences DataCube Builder ": None,
"Swiss eScience (Grid) Certificates": "e-INFRA non-commercial",
"Guardomic": "e-INFRA non-commercial",
"Piloting and co-design of Business Pilots": "e-INFRA non-commercial",
"GÉANT Lambda": "e-INFRA GEANT",
"Argo marine floats metadata API": None,
"GÉANT IP": "e-INFRA GEANT",
"GÉANT Plus": "e-INFRA GEANT",
"INDIGO Identity and Access Management (IAM) ": "e-INFRA non-commercial",
"eduroam": "e-INFRA GEANT",
"AiiDAlab": "e-INFRA non-commercial",
"GÉANT MDVPN": "e-INFRA GEANT"
}

##################################################### FUNCTIONS ########################################################
def service_migration(directory):
    migrationFolders = ['/service/', '/datasource/']
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                isVersion = False
                with open(directory + migrationFolder + file, 'r') as json_file:
                    json_data = migrate_horizontal_service(json_file, isVersion)
                    # write to file
                    with open(directory + migrationFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
            if file.endswith('-version'):
                isVersion = True
                versionFiles = os.listdir(directory + migrationFolder + file)
                for versionFile in versionFiles:
                    with open(directory + migrationFolder + file + '/' + versionFile, 'r') as json_file:
                        json_data = migrate_horizontal_service(json_file, isVersion)
                        # write to file
                        with open(directory + migrationFolder + file + '/' + versionFile, 'w') as json_file:
                            json.dump(json_data, json_file, indent=2)


def migrate_horizontal_service(json_file, isVersion):
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
    if resourceName in servicesToHorizontalServices:
        # migrate horizontal service
        if servicesToHorizontalServices[resourceName] is not None:
            resourceExtras = root.find('{http://einfracentral.eu}resourceExtras')
            if resourceExtras is not None:
                horizontalService = resourceExtras.find('{http://einfracentral.eu}horizontalService')
                if horizontalService is not None:
                        horizontalService.text = servicesToHorizontalServices[resourceName]
                else:
                    newHorizontalService = ET.Element("tns:horizontalService")
                    newHorizontalService.text = servicesToHorizontalServices[resourceName]
                    resourceExtras.append(newHorizontalService)
                # if not isVersion:
                    # print("Migrated researchCategories of Resource: [", resourceId, "]-[", resourceName, "]")
            else:
                newResourceExtras = ET.Element("tns:resourceExtras")
                newHorizontalService = ET.Element("tns:horizontalService")
                newHorizontalService.text = servicesToHorizontalServices[resourceName]
                newResourceExtras.append(newHorizontalService)
                tree.append(newResourceExtras)
                # if not isVersion:
                    # print("Migrated researchCategories of Resource: [", resourceId, "]-[", resourceName, "]")

        # migrate tags
        if horizontalServicesRelatedTags[resourceName] is not None:
            tags = resource.find('{http://einfracentral.eu}tags')
            if tags is not None:
                found = False
                for tag in tags:
                    if tag.text == horizontalServicesRelatedTags[resourceName]:
                        found = True
                if not found:
                    newTag = ET.Element("tns:tag")
                    newTag.text = horizontalServicesRelatedTags[resourceName]
                    tags.append(newTag)
                # if not isVersion:
                    # print("Migrated researchCategories of Resource: [", resourceId, "]-[", resourceName, "]")
            else:
                newTags = ET.Element("tns:tags")
                newTag = ET.Element("tns:tag")
                newTag.text = horizontalServicesRelatedTags[resourceName]
                newTags.append(newTag)
                resource.append(newTags)
                # if not isVersion:
                    # print("Migrated researchCategories of Resource: [", resourceId, "]-[", resourceName, "]")

    # else:
    #     if not isVersion:
    #         metadata = root.find('{http://einfracentral.eu}metadata')
    #         if metadata is not None:
    #             published = metadata.find('{http://einfracentral.eu}published')
    #             if published is not None:
    #                 if published.text == 'false':
    #                     print("Resource: [", resourceId, "]-[", resourceName, "] not found in the list")

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