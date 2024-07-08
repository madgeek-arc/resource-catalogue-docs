# Create a dump containing only the resources that User Admins have consented for.
# No Public layer, no version folders

######################################################## IMPORTS #######################################################
import json
import os
import shutil
import argparse
######################################################## IMPORTS #######################################################
# To be deleted after running:
# 31a9a29b-d4be-46c2-8002-d9ade13b0372 -> 21.15120/XRKb49 -> Jagiellonian University, Jagiellonian Library (duplicate un-onboarded)
# 657f69a6-8f64-44e7-9933-8c506714893a -> 21.15120/ITqSpd -> EOSC-NORDIC Vilnius University (not consent)


# Provider names who consent
provider_names = ['Predictia Intelligent Data Solutions SL','OpenMinTeD','Biomedical Research Foundation, Academy of Athens',
                  'Serbian Academy of Sciences and Arts','Mandat International','Center for direct scientific communication',
                  'VI-SEEM','University of Belgrade - Faculty of Chemistry',
                  'EMBIMOS (Environmental and Sustainability Participatory Information Systems)',
                  'Institute of Chemistry, Technology and Metallurgy, University of Belgrade',
                  'George Kourousias (abbrev. Elettra Sincrotrone Trieste)','Helmholtz-Zentrum Dresden-Rossendorf e.V.',
                  'Global Biodiversity Information Facility (GBIF)','Instituto Superior de Agronomia da Universidade de Lisboa',
                  'Bijvoet Centre - Utrecht University','European Research Infrastructure for Language Resources and Technology',
                  'Portuguese Node of GBIF','Istituto Nazionale di Astrofisica','MyScienceWork','SWITCH','OpenAIRE',
                  'University of Florence, DISIT lab','PlantNet consortium (hosted by Inria)','DDQ B.V.',
                  'Institute of Informatics - Slovak Academy of Sciences ','FIR e. V. at RWTH Aachen University','EnerMaps',
                  'PROduction et GEstion des DOnnées','Seth Software spółka z ograniczoną odpowiedzialnością','Eurac Research',
                  'Cineca Consorzio Interuniversitario','Instruct-ERIC',
                  'Alfred Wegener Institute for Polar and Marine Research in cooperation with MARUM, Center for Marine Environmental Sciences',
                  'EnhanceR','University of Opole','SeaDataNet','University and State Library of Saxony Anhalt','EOSC DIH - Digital Innovation Hub',
                  're3data - Registry of Research Data Repositories','Arts et Metiers Institute of Technology','UiT The Arctic University of Norway',
                  'Euro-Mediterranean Center on Climate Change','Centre for Data Analysis and Archiving','Poznan Supercomputing and Networking Center',
                  'Earth Observation Data Centre for Water Resources Monitoring','Synchrotron SOLEIL','NORCE Norwegian Research Centre',
                  'DataCite','OPERAS AISBL','Lithuanian Data Archive for Social Sciences and Humanities','Digital Curation Centre',
                  'Institute for Atmospheric and Earth System Research','The Foundation NILU','Leibniz Information Centre for Science and Technology',
                  'National Documentation Centre','INFRAFRONTIER','Open Knowledge Maps - Verein zur Förderung der Sichtbarkeit wissenschaftlichen Wissens',
                  'European Holocaust Research Infrastructure','READ-COOP SCE mit beschränkter Haftung',
                  'Horizon Europe Project Truly Carbon Neutral electricity enhanced Synthesis of Liquefied Natural Gas (LNG) from biomass',
                  'Friedrich-Alexander-University Erlangen-Nürnberg, Chair of Energy Process Engineering','NIOD Institute for War, Genocide and Holocaust Studies',
                  'National Technical University of Athens','ELIXIR United Kingdom','Blue-Cloud - Piloting innovative services for Marine Research &amp; the Blue Economy',
                  'BlueBRIDGE','Earlham Institute','Portuguese National Distributed Computing Infrastructure (INCD)',
                  'IBERGRID - Iberian Distributed Computing Infrastructure','Flemisch Research Information Space','IsoArcH','SoBigData',
                  'D4Science','Institute for Information Science and Technologies \"Alessandro Faedo\" - ISTI','ELIXIR','transcript Independent Academic Publishing ',
                  'Institute of Instrumentation for Molecular Imaging - Grid and High Performance Computing - Universitat Politècnica de València',
                  'Jülich Supercomputing Centre','IDEAconsult','Alma Mater Studiorum - Università di Bologna','Leibniz Institute for Psychology',
                  'Consorci de Serveis Universitaris de Catalunya','Forschungszentrum Jülich','Oxford e-Research Centre, University of Oxford, UK',
                  'Europeana Foundation','Observatoire de Paris','Consortium of European Social Science Data Archives ERIC','University of Oslo',
                  'University of Freiburg','The SCIGNE Platform','UNPARALLEL Innovation, Lda','de.NBI - German Network for Bioinformatics Infrastructure',
                  'Leibniz Institute DSMZ - German Collection of Microorganisms and Cell Cultures','Huma-Num','European Network of Living Labs',
                  'Laboratório de Sistemas Distribuídos - Universidade Federal de Campina Grande','Meteorological Environmental Earth Observation',
                  'Vilnius University','EOX IT Services GmbH','Kaunas University of Technology',
                  'Magnetic Resonance Center of the University of Florence - CERM, Interuniversity consortium CIRMMP',
                  'A Worldwide e-Infrastructure for Structural Biology','Consorzio per il Sistema Informativo','DOAB Foundation',
                  'Finnish Social Science Data Archive','Fundacion Centro Tecnologico de Supercomputacion de Galicia','Institut Laue Langevin',
                  'Barcelona Supercomputing Center - Centro Nacional de Supercomputación','GÉANT Association','GBIF Spain',
                  'EUROPEAN ORGANIZATION FOR NUCLEAR RESEARCH','Universitat Pompeu Fabra','Centerdata','Advanced Metabolomics',
                  'EUDAT','MAX IV Laboratory, Lund University','SURF','Virtual Atomic and Molecular Data Centre','Net7 S.r.l.',
                  'Centre de Recherche en Acquisition et Traitement de l\'Image pour la Santé','Common Workflow Language community','ICTLC S.P.A.',
                  'The Svalbard Integrated Arctic Earth Observing System','Ifremer, the French National Institute for Ocean Science',
                  'Institute of Physics of Cantabria (IFCA)','DARIAH ERIC (Digital Research Infrastructure for the Arts and Humanities)',
                  'UK Research and Innovation - Science and Technology Facilities Council','CSC – IT CENTER FOR SCIENCE','RASDAMAN',
                  'University of Belgrade – Faculty of Philosophy','Consejo Superior de Investigaciones Científicas (CSIC)',
                  'Heidelberg Institute for Theoretical Studies','Materials Cloud','University of Konstanz','Flanders Marine Institute',
                  'Institute for Biocomputation and Physics of Complex Systems - University of Zaragoza','Charles University',
                  'Stefan cel Mare University of Suceava','VITO NV  (Vlaamse Instelling voor Technologisch Onderzoek NV)',
                  'Athena Research and Innovation Center in Information and Communication Technologies','Strasbourg astronomical Data Centre',
                  'Central European Research Infrastructure Consortium','ELIXIR Belgium','University of Zagreb University Computing Centre',
                  'EXOSCALE','Progressive Systems Srl','Turkish Academic Network and Information Center','CERIC-ERIC','EGI Foundation',
                  'National Infrastructures for Research and Technology','DEMO Foundation','Georgian Research and Educational Networking Association',
                  'Arkivum Limited','Horia Hulubei National Institute for R&amp;D in Physics and Nuclear Engineering','VIB',
                  'Krakow University of Economics, Main Library','Consortium FAIRmat','LifeWatch ERIC','University of Padua',
                  'AGH University of Krakow Main Library ','Biodiversity Knowledge Hub','Pedagogical University of Krakow, Main Library',
                  'Gesellschaft für wissenschaftliche Datenverarbeitung mbH Göttingen','University of Belgrade Computer Centre',
                  'Swedish Infrastructure for Ecosystem Science','expert.ai','Italian National Institute of Nuclear Physics',
                  'OLOS Association','KIT - Scientific Computing Center','Karlsruhe Institute of Technology','GFT Italy',
                  'Academic Computer Centre CYFRONET AGH','KIT - Library','Jagiellonian University, Jagiellonian Library',
                  'KU Leuven','Horia Hulubei National Institute for R&D in Physics and Nuclear Engineering','George Kourousias',
                  'Institute for Information Science and Technologies \\\"Alessandro Faedo\\\" - ISTI',
                  'Blue-Cloud - Piloting innovative services for Marine Research & the Blue Economy']

naames = []
provider_ids = []
service_ids = []
training_ids = []
interoperability_ids = []
datasource_ids = []
monitoring_ids = []
resource_interoperability_record_ids = []

provider_core_ids = []
service_core_ids = []
training_core_ids = []
interoperability_core_ids = []
datasource_core_ids = []
monitoring_core_ids = []
resource_interoperability_record_core_ids = []
##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    migrationFolders = ['/provider/', '/service/', '/training_resource/', '/interoperability_record/', '/datasource/',
                        '/monitoring/', '/resource_interoperability_record/']
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                isVersion = False
                with open(directory + migrationFolder + file, 'r') as json_file:
                    find_consent_resources(json_file, isVersion, migrationFolder.replace("/", ""))


def find_consent_resources(json_file, isVersion, resourceType):
    internalItem = determine_internal_item(resourceType)
    json_data = json.load(json_file)
    payload_str = json_data['payload']
    payload_data = json.loads(payload_str)
    core_id = json_data['id']
    metadata = payload_data.get('metadata')
    if metadata is not None:
        published = metadata.get('published')
    resource = payload_data.get(internalItem)
    resourceId = resource.get('id')

    if resourceType == 'provider':
        name = resource.get('name')
        if name in provider_names and not published:
            provider_ids.append(resourceId)
            provider_core_ids.append(core_id)
            naames.append(name)
        # if 'Centre de Recherche en Acquisition et Traitement de' in name and not published:
        #     provider_ids.append(resourceId)
        #     provider_core_ids.append(core_id)

    if resourceType == 'service':
        resourceOrganisation = resource.get('resourceOrganisation')
        if resourceOrganisation in provider_ids:
            service_ids.append(resourceId)
            service_core_ids.append(core_id)

    if resourceType == 'training_resource':
        resourceOrganisation = resource.get('resourceOrganisation')
        if resourceOrganisation in provider_ids:
            training_ids.append(resourceId)
            training_core_ids.append(core_id)

    if resourceType == 'interoperability_record':
        providerId = resource.get('providerId')
        if providerId in provider_ids:
            interoperability_ids.append(resourceId)
            interoperability_core_ids.append(core_id)

    if resourceType == 'datasource':
        serviceId = resource.get('serviceId')
        if serviceId in service_ids:
            datasource_ids.append(resourceId)
            datasource_core_ids.append(core_id)

    if resourceType == 'monitoring':
        serviceId = resource.get('serviceId')
        if serviceId in service_ids or serviceId in training_ids:
            monitoring_ids.append(resourceId)
            monitoring_core_ids.append(core_id)

    if resourceType == 'resource_interoperability_record':
        resourceId = resource.get('resourceId')
        if resourceId in service_ids or resourceId in training_ids:
            resource_interoperability_record_ids.append(resourceId)
            resource_interoperability_record_core_ids.append(core_id)


def determine_internal_item(resourceType):
    if resourceType == 'training_resource':
        internalItem = 'trainingResource'
    elif resourceType == 'interoperability_record':
        internalItem = 'interoperabilityRecord'
    elif resourceType == 'resource_interoperability_record':
        internalItem = 'resourceInteroperabilityRecord'
    else:
        internalItem = resourceType
    return internalItem


def copy_json_files(directory):
    migrationFolders = ['/provider/', '/service/', '/training_resource/', '/interoperability_record/', '/datasource/',
                        '/monitoring/', '/resource_interoperability_record/']
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                # Get the file name without the .json extension
                filename = os.path.splitext(file)[0]

                # Check if the filename exists in your array of filenames
                if filename in provider_core_ids:
                    folder_path = directory + migrationFolder
                    source_file = os.path.join(folder_path, file)
                    destination_file = os.path.join('/home/mike/Downloads/lot1/provider', file)
                    shutil.copyfile(source_file, destination_file)
                if filename in service_core_ids:
                    folder_path = directory + migrationFolder
                    source_file = os.path.join(folder_path, file)
                    destination_file = os.path.join('/home/mike/Downloads/lot1/service', file)
                    shutil.copyfile(source_file, destination_file)
                if filename in training_core_ids:
                    folder_path = directory + migrationFolder
                    source_file = os.path.join(folder_path, file)
                    destination_file = os.path.join('/home/mike/Downloads/lot1/training_resource', file)
                    shutil.copyfile(source_file, destination_file)
                if filename in interoperability_core_ids:
                    folder_path = directory + migrationFolder
                    source_file = os.path.join(folder_path, file)
                    destination_file = os.path.join('/home/mike/Downloads/lot1/interoperability_record', file)
                    shutil.copyfile(source_file, destination_file)
                if filename in datasource_core_ids:
                    folder_path = directory + migrationFolder
                    source_file = os.path.join(folder_path, file)
                    destination_file = os.path.join('/home/mike/Downloads/lot1/datasource', file)
                    shutil.copyfile(source_file, destination_file)
                if filename in monitoring_core_ids:
                    folder_path = directory + migrationFolder
                    source_file = os.path.join(folder_path, file)
                    destination_file = os.path.join('/home/mike/Downloads/lot1/monitoring', file)
                    shutil.copyfile(source_file, destination_file)
                if filename in resource_interoperability_record_core_ids:
                    folder_path = directory + migrationFolder
                    source_file = os.path.join(folder_path, file)
                    destination_file = os.path.join('/home/mike/Downloads/lot1/resource_interoperability_record', file)
                    shutil.copyfile(source_file, destination_file)
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
folder_selection(args.path)
print(naames)
print(provider_core_ids.__len__())
print(provider_ids.__len__())
print(service_core_ids.__len__())
print(service_ids.__len__())
print(training_core_ids.__len__())
print(training_ids.__len__())
print(interoperability_core_ids.__len__())
print(interoperability_ids.__len__())
print(datasource_core_ids.__len__())
print(datasource_ids.__len__())
print(monitoring_core_ids.__len__())
print(monitoring_ids.__len__())
print(resource_interoperability_record_core_ids.__len__())
print(resource_interoperability_record_ids.__len__())
copy_json_files(args.path)
######################################################## RUN ###########################################################
