# # Create a dump containing only the resources LOT1 needs (consent = true)
# # SOS: do not include published (public = true) resources
#
# ######################################################## IMPORTS #######################################################
# import json
# import os
# import shutil
# import argparse
# ######################################################## IMPORTS #######################################################
#
# #TODO: LOAD FILE WITH NAMES/EMAILS
# ##################################################### FUNCTIONS ########################################################
# def folder_selection(directory):
#     migrationFolders = ['/catalogue/', '/provider/']
#     for migrationFolder in migrationFolders:
#         for file in os.listdir(directory + migrationFolder):
#             if file.endswith('.json'):
#                 isVersion = False
#                 with open(directory + migrationFolder + file, 'r') as json_file:
#                     find_consent_resources(json_file, isVersion, migrationFolder.replace("/", ""))
#
#
# def find_consent_resources(json_file, isVersion, resourceType):
#     json_data = json.load(json_file)
#     payload_str = json_data['payload']
#     payload_data = json.loads(payload_str)
#     resource = payload_data.get(resourceType)
#
#     if resourceType == 'catalogue':
#         name = resource.get('name')
#         if name in provider_names:
#             transfer_contact_info_list = TransferContactInformation()
#             # for emails in list
#                 transfer_contact_info_instance = ContactInfoTransfer(email=None, acceptedTransfer=True)
#                 transfer_contact_info_list.add_contact(transfer_contact_info_instance)
#             payload_data['transferContactInformation'] = transfer_contact_info_list.to_dict()
#     if resourceType == 'provider':
#         name = resource.get('name')
#         if name in provider_names:
#             transfer_contact_info_list = TransferContactInformation()
#             # for emails in list
#                 transfer_contact_info_instance = ContactInfoTransfer(email=None, acceptedTransfer=True)
#                 transfer_contact_info_list.add_contact(transfer_contact_info_instance)
#         payload_data['transferContactInformation'] = transfer_contact_info_list.to_dict()
#
#     # update payload
#     json_data['payload'] = json.dumps(payload_data)
#     if isVersion:
#         json_data['resource']['payload'] = json.dumps(payload_data)
#
#     return json_data
#
#
# class ContactInfoTransfer:
#     def __init__(self, email, acceptedTransfer):
#         self.email = email
#         self.acceptedTransfer = acceptedTransfer
#
#     def to_dict(self):
#         return {
#             'email': self.email,
#             'acceptedTransfer': self.acceptedTransfer
#         }
#
#
# class TransferContactInformation:
#     def __init__(self, transfer_contact_information=None):
#         if transfer_contact_information is None:
#             transfer_contact_information = []
#         self.transfer_contact_information = transfer_contact_information
#
#     def to_dict(self):
#         return {
#             'transferContactInformation': [contact.to_dict() for contact in self.transfer_contact_information]
#         }
#
#     def add_contact(self, contact):
#         self.transfer_contact_information.append(contact)
# ##################################################### FUNCTIONS ########################################################
#
#
# ######################################################## RUN ###########################################################
# parser = argparse.ArgumentParser()
# parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
# args = parser.parse_args()
# folder_selection(args.path)
# ######################################################## RUN ###########################################################