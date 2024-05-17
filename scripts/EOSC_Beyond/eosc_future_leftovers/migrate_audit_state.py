######################################################## IMPORTS #######################################################
import json
import os
import argparse
######################################################## IMPORTS #######################################################

##################################################### FUNCTIONS ########################################################
def folder_selection(directory):
    migrationFolders = ['/catalogue/', '/provider/', '/service/', '/training_resource/', '/interoperability_record/']
    for migrationFolder in migrationFolders:
        for file in os.listdir(directory + migrationFolder):
            if file.endswith('.json'):
                isVersion = False
                with open(directory + migrationFolder + file, 'r') as json_file:
                    json_data = migrate(json_file, isVersion)
                    # write to file
                    with open(directory + migrationFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
            if file.endswith('-version'):
                isVersion = True
                versionFiles = os.listdir(directory + migrationFolder + file)
                for versionFile in versionFiles:
                    with open(directory + migrationFolder + file + '/' + versionFile, 'r') as json_file:
                        json_data = migrate(json_file, isVersion)
                        # write to file
                        with open(directory + migrationFolder + file + '/' + versionFile, 'w') as json_file:
                            json.dump(json_data, json_file, indent=2)

def migrate(json_file, isVersion):
    json_data = json.load(json_file)
    payload_str = json_data['payload']
    payload_data = json.loads(payload_str)

    # migrate audit state
    auditState = payload_data.get('auditState')
    if auditState is None:
        # if audit functionality restart on Beyond / LOT1
        # newAuditState = 'Not audited'

        # if audit functionality resumes from EOSC Future
        loggingInfo = payload_data.get('loggingInfo', [])
        newAuditState = get_latest_audit_state(loggingInfo)
        payload_data['auditState'] = newAuditState

        # update payload
        json_data['payload'] = json.dumps(payload_data)
        if isVersion:
            json_data['resource']['payload'] = json.dumps(payload_data)

    return json_data


def get_latest_audit_state(loggingInfo):
    sortedLoggingInfo = sorted(loggingInfo, key=lambda x: x['date'])
    for loggingInfo in sortedLoggingInfo:
        if loggingInfo is not None:
            loggingInfoType = loggingInfo['type']
            if loggingInfoType is not None:
                if loggingInfoType == "audit":
                    loggingInfoActionType = loggingInfo['actionType']
                    if loggingInfoActionType is not None:
                        if loggingInfoActionType == "valid":
                            return "Valid"
                        else:
                            return "Invalid and not updated"
    return "Not audited"

##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
folder_selection(args.path)
######################################################## RUN ###########################################################