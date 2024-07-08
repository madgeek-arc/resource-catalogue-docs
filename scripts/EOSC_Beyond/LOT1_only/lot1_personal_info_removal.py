# Removes personal information from Catalogues/Providers and their resources that did not consent
# Removes published resources.

# Bundle:
#	metadata:
#		registerBy/At
#		modifiedBy/At
#		terms
#	loggingInfo:
#		userEmail
#		userFullName
#	latestAuditInfo
#	latestOnboardingInfo
#	latestUpdateInfo
#
# Catalogue:
#	location(streetNameAndNumber)?
#	mainContact
#	publicContacts
#	users
#
# Provider:
#	location?
#	mainContact
#	publicContacts
#	users
#
# Service:
#	mainContact
#	publicContacts
#	helpdeskEmail
#	securityContactEmail
#
# TrainingResource:
#	contact
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
    migrationFolders = ['/catalogue/', '/provider/', '/service/', '/training_resource/']
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
    resource = payload_data.get(internalItem)

    # TODO: Decide upon which fields to be removed and how (deletion OR null values)

    if resourceType == 'catalogue' or resourceType == 'provider':
        remove_unconsented_main_contact(resource)
        remove_unconsented_public_contacts(resource)
        remove_unconsented_users(resource)

    if resourceType == 'service':
        remove_unconsented_main_contact(resource)
        remove_unconsented_public_contacts(resource)

    if resourceType == 'training_resource':
        remove_unconsented_main_contact(resource)


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


def remove_unconsented_main_contact(resource):
    mainContact = resource.get('mainContact')
    contact_field = 'mainContact'
    if mainContact is None:
        mainContact = resource.get('contact')
        contact_field = 'contact'
    if mainContact:
        mainContactEmail = mainContact.get('email')
        if mainContactEmail and mainContactEmail not in emails_consented:
            del resource[contact_field]


def remove_unconsented_public_contacts(resource):
    publicContacts = resource.get('publicContacts')
    if publicContacts:
        contacts_to_delete = []
        for publicContact in publicContacts:
            if publicContact:
                publicContactEmail = publicContact.get('email')
                if publicContactEmail and publicContactEmail not in emails_consented:
                    contacts_to_delete.append(publicContact)
        for publicContact in contacts_to_delete:
            publicContacts.remove(publicContact)


def remove_unconsented_users(resource):
    users = resource.get('users')
    if users:
        users_to_delete = []
        for user in users:
            if user:
                userEmail = user.get('email')
                if userEmail and userEmail not in emails_consented:
                    users_to_delete.append(user)
        for user in users_to_delete:
            users.remove(user)
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
folder_selection(args.path)
######################################################## RUN ###########################################################
