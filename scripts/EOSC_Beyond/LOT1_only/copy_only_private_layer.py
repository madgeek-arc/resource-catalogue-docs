# Create a dump containing all resources
# No Public layer, no version folders

######################################################## IMPORTS #######################################################
import json
import os
import shutil
import argparse
######################################################## IMPORTS #######################################################
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
                with open(directory + migrationFolder + file, 'r') as json_file:
                    find_consent_resources(json_file, migrationFolder.replace("/", ""))


def find_consent_resources(json_file, resourceType):
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
        if not published:
            provider_ids.append(resourceId)
            provider_core_ids.append(core_id)

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
                    destination_file = os.path.join('/tmp/lot1/provider', file)
                    shutil.copyfile(source_file, destination_file)
                if filename in service_core_ids:
                    folder_path = directory + migrationFolder
                    source_file = os.path.join(folder_path, file)
                    destination_file = os.path.join('/tmp/lot1/service', file)
                    shutil.copyfile(source_file, destination_file)
                if filename in training_core_ids:
                    folder_path = directory + migrationFolder
                    source_file = os.path.join(folder_path, file)
                    destination_file = os.path.join('/tmp/lot1/training_resource', file)
                    shutil.copyfile(source_file, destination_file)
                if filename in interoperability_core_ids:
                    folder_path = directory + migrationFolder
                    source_file = os.path.join(folder_path, file)
                    destination_file = os.path.join('/tmp/lot1/interoperability_record', file)
                    shutil.copyfile(source_file, destination_file)
                if filename in datasource_core_ids:
                    folder_path = directory + migrationFolder
                    source_file = os.path.join(folder_path, file)
                    destination_file = os.path.join('/tmp/lot1/datasource', file)
                    shutil.copyfile(source_file, destination_file)
                if filename in monitoring_core_ids:
                    folder_path = directory + migrationFolder
                    source_file = os.path.join(folder_path, file)
                    destination_file = os.path.join('/tmp/lot1/monitoring', file)
                    shutil.copyfile(source_file, destination_file)
                if filename in resource_interoperability_record_core_ids:
                    folder_path = directory + migrationFolder
                    source_file = os.path.join(folder_path, file)
                    destination_file = os.path.join('/tmp/lot1/resource_interoperability_record', file)
                    shutil.copyfile(source_file, destination_file)
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
folder_selection(args.path)
copy_json_files(args.path)
######################################################## RUN ###########################################################
