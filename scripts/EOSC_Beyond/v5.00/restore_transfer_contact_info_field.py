######################################################## IMPORTS #######################################################
import json
import os
import argparse
######################################################## IMPORTS #######################################################

# Manually add transferContactInfo for
# Institute for Information Science and Technologies \"Alessandro Faedo\" - ISTI
# 985d0029-54b3-444b-9037-7b841bee49f2, 7f759133-d5ba-4b10-b6e8-6fdb132ac99a

####################################################### LOAD FILES #####################################################
root_path = os.path.dirname(os.path.abspath(__file__))  # This gives the directory of the current script
catalogue_names_to_consent_path = os.path.join(root_path, 'extra_files', 'catalogue_names_to_emails_consent.json')
with open(catalogue_names_to_consent_path, 'r') as file:
    catalogue_names_to_consent = json.load(file)

provider_names_to_consent_path = os.path.join(root_path, 'extra_files', 'provider_names_to_emails_consent.json')
with open(provider_names_to_consent_path, 'r') as file:
    provider_names_to_consent = json.load(file)
####################################################### LOAD FILES #####################################################


##################################################### FUNCTIONS ########################################################
catalogueFound = 0
providerFound = 0

def folder_selection(directory):
    migrationFolders = ['/catalogue/', '/provider/']
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                with open(directory + migrationFolder + file, 'r') as json_file:
                    json_data = find_consent_resources(json_file, migrationFolder.replace("/", ""))
                    # write to file
                    with open(directory + migrationFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)


def find_consent_resources(json_file, resourceType):
    global catalogueFound, providerFound

    json_data = json.load(json_file)
    payload_str = json_data['payload']
    payload_data = json.loads(payload_str)
    resource = payload_data.get(resourceType)

    if resourceType == 'catalogue':
        name = resource.get('name')
        if name in catalogue_names_to_consent:
            catalogueFound += 1
            transfer_contact_info_list = TransferContactInformation()
            emails = catalogue_names_to_consent[name]
            if isinstance(emails, str):
                emails = [emails]
            for email in emails:
                transfer_contact_info_instance = ContactInfoTransfer(email=email, acceptedTransfer=True)
                transfer_contact_info_list.add_contact(transfer_contact_info_instance)
            payload_data['transferContactInformation'] = transfer_contact_info_list.to_dict()
    if resourceType == 'provider':
        catalogueId = resource['catalogueId']
        name = resource.get('name')
        if name in provider_names_to_consent:
            if name == 'Vilnius University' and catalogueId != 'eosc':  # EOSC-NORDIC same name, not consent
                return  # FIXME: returns and then saves null json. Test if it is fixed.
            providerFound += 1
            transfer_contact_info_list = TransferContactInformation()
            emails = provider_names_to_consent[name]
            if isinstance(emails, str):
                emails = [emails]
            for email in emails:
                transfer_contact_info_instance = ContactInfoTransfer(email=email, acceptedTransfer=True)
                transfer_contact_info_list.add_contact(transfer_contact_info_instance)
            payload_data['transferContactInformation'] = transfer_contact_info_list.to_dict()

        # update payload
        json_data['payload'] = json.dumps(payload_data)

    return json_data


class ContactInfoTransfer:
    def __init__(self, email, acceptedTransfer):
        self.email = email
        self.acceptedTransfer = acceptedTransfer

    def to_dict(self):
        return {
            'email': self.email,
            'acceptedTransfer': self.acceptedTransfer
        }


class TransferContactInformation:
    def __init__(self, transfer_contact_information=None):
        if transfer_contact_information is None:
            transfer_contact_information = []
        self.transfer_contact_information = transfer_contact_information

    def to_dict(self):
        return [contact.to_dict() for contact in self.transfer_contact_information]

    def add_contact(self, contact):
        self.transfer_contact_information.append(contact)
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
folder_selection(args.path)
# enable with published = false to get 5/175
# print(f"Catalogues found: {catalogueFound}")
# print(f"Providers found: {providerFound}")
######################################################## RUN ###########################################################