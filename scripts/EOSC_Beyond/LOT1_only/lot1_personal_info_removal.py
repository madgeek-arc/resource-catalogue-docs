# Removes personal information from Catalogues/Providers and their resources that did not consent
# Removes published resources.

# Bundle:
#	metadata:
#		registerBy -> system for all
#		modifiedBy -> system for all
#		terms -> nullify
#	loggingInfo: -> delete
#		userEmail
#		userFullName
#	latestAuditInfo -> delete
#	latestOnboardingInfo -> delete
#	latestUpdateInfo -> delete
#
# Catalogue/Provider:
#	mainContact -> anonymize everything for emails not consent
#	users -> anonymize everything for emails not consent
#
# Service:
#	mainContact -> anonymize everything for emails not consent
#	securityContactEmail -> anonymize emails not consent
#
# TrainingResource:
#	contact -> anonymize everything for emails not consent
######################################################## IMPORTS #######################################################
import json
import os
import argparse
######################################################## IMPORTS #######################################################


####################################################### LOAD FILES #####################################################
root_path = os.path.dirname(os.path.abspath(__file__))
emails_consented_path = os.path.join(root_path, 'extra_files', 'emails_consented.json')
with open(emails_consented_path, 'r') as file:
    emails_consented = json.load(file)
####################################################### LOAD FILES #####################################################


##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    migrationFolders = ['/catalogue/', '/configuration_template/', '/configuration_template_instance/', '/datasource/',
                        '/interoperability_record/', '/monitoring/', '/provider/', '/resource_interoperability_record/',
                        '/service/', '/training_resource/']
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                with open(directory + migrationFolder + file, 'r') as json_file:
                    json_data = migrate(json_file, migrationFolder.replace("/", ""))
                    # write to file
                    with open(directory + migrationFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)


def migrate(json_file, resourceType):
    internalItem = determine_internal_item(resourceType)
    json_data = json.load(json_file)
    payload_str = json_data['payload']
    payload_data = json.loads(payload_str)

    # Bundle
    metadata = payload_data.get('metadata')
    if metadata:
        registeredBy = metadata.get('registeredBy')
        if registeredBy:
            metadata['registeredBy'] = 'system'
        modifiedBy = metadata.get('modifiedBy')
        if modifiedBy:
            metadata['modifiedBy'] = 'system'
        terms = metadata.get('terms')
        if terms:
            metadata['terms'] = None
    loggingInfo = payload_data.get('loggingInfo')
    if loggingInfo:
        del payload_data['loggingInfo']
    latestAuditInfo = payload_data.get('latestAuditInfo')
    if latestAuditInfo:
        del payload_data['latestAuditInfo']
    latestOnboardingInfo = payload_data.get('latestOnboardingInfo')
    if latestOnboardingInfo:
        del payload_data['latestOnboardingInfo']
    latestUpdateInfo = payload_data.get('latestUpdateInfo')
    if latestUpdateInfo:
        del payload_data['latestUpdateInfo']

    # Internal
    resource = payload_data.get(internalItem)
    if resourceType == 'catalogue' or resourceType == 'provider':
        anonymize_unconsented_main_contact(resource)
        anonymize_unconsented_users(resource)

    if resourceType == 'service':
        anonymize_unconsented_main_contact(resource)
        securityContactEmail = resource.get('securityContactEmail')
        if securityContactEmail:
            resource['securityContactEmail'] = 'redacted@example.com'

    if resourceType == 'training_resource':
        anonymize_unconsented_main_contact(resource)

    # update payload
    json_data['payload'] = json.dumps(payload_data)
    return json_data


def determine_internal_item(resourceType):
    if resourceType == 'configuration_template':
        internalItem = 'configurationTemplate'
    elif resourceType == 'configuration_template_instance':
        internalItem = 'configurationTemplateInstance'
    elif resourceType == 'training_resource':
        internalItem = 'trainingResource'
    elif resourceType == 'interoperability_record':
        internalItem = 'interoperabilityRecord'
    elif resourceType == 'resource_interoperability_record':
        internalItem = 'resourceInteroperabilityRecord'
    else:
        internalItem = resourceType
    return internalItem


def anonymize_unconsented_main_contact(resource):
    mainContact = resource.get('mainContact')
    if mainContact is None:  # training resources
        mainContact = resource.get('contact')
    if mainContact:
        mainContactEmail = mainContact.get('email')
        if mainContactEmail and mainContactEmail not in emails_consented:
            mainContactFirstName = mainContact.get('firstName')
            if mainContactFirstName:
                mainContact['firstName'] = 'name'
            mainContactLastName = mainContact.get('lastName')
            if mainContactLastName:
                mainContact['lastName'] = 'surname'
            mainContact['email'] = 'redacted@example.com'
            mainContactPhone = mainContact.get('phone')
            if mainContactPhone:
                del mainContact['phone']

def anonymize_unconsented_users(resource):
    users = resource.get('users')
    if users:
        for user in users:
            if user:
                userEmail = user.get('email')
                if userEmail and userEmail not in emails_consented:
                    userId = user.get('id')
                    if userId:
                        user['id'] = 'id'
                    userName = user.get('name')
                    if userName:
                        user['name'] = 'name'
                    userSurname = user.get('surname')
                    if userSurname:
                        user['surname'] = 'surname'
                    user['email'] = 'redacted@example.com'
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
folder_selection(args.path)
######################################################## RUN ###########################################################
