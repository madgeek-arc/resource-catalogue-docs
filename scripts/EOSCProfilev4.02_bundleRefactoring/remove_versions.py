######################################################## IMPORTS #######################################################
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup as bs
import argparse
import shutil
######################################################## IMPORTS #######################################################

######################################################## GLOBAL ########################################################
serviceRelatedFolders = ['/pending_service/', '/infra_service/']
######################################################## GLOBAL ########################################################

##################################################### FUNCTIONS ########################################################
def versions_deletion(directory):
    versionFoldersIDs = []
    oldLoggingInfos = {}
    latestServices =[]
    count = 0
    for serviceRelatedFolder in serviceRelatedFolders:
        for file in os.listdir(directory + serviceRelatedFolder):
            if file.endswith('.json'):
                with open(directory + serviceRelatedFolder + file, 'r') as json_file:
                    coreId, serviceId, loggingInfoList = find_all_versions(json_file)
                    if coreId is not None and serviceId is not None and loggingInfoList is not None:
                        save_loggingInfo_from_oldest_versions(oldLoggingInfos, serviceId, loggingInfoList)
                        # keep the IDs so to delete the corresponding version folders
                        fileID = os.path.splitext(file)[0]
                        versionFoldersIDs.append(fileID+'-version')
                        # delete the old .json
                        os.remove(directory + serviceRelatedFolder + file)
                        count = count + 1
                    if coreId == 'latest':
                        latestServices.append(serviceId)
    print("Total .json (old versions) deleted:", count)
    version_folders_deletion(directory, versionFoldersIDs)
    update_latest_services_loggingInfo(directory, latestServices, oldLoggingInfos)


def find_all_versions(json_file):
    json_data = json.load(json_file)
    xml = json_data['payload']
    ET.register_namespace("tns", "http://einfracentral.eu")
    root = ET.ElementTree(ET.fromstring(xml))
    service = root.find('{http://einfracentral.eu}service')
    loggingInfoList = []
    for loggingInfo in root.findall('{http://einfracentral.eu}loggingInfo'):
        if loggingInfo is not None:
            loggingInfoObject = LoggingInfo()
            loggingInfoDate = loggingInfo.find('{http://einfracentral.eu}date')
            if loggingInfoDate is not None:
                loggingInfoObject.date = loggingInfoDate.text
            loggingInfoUserEmail = loggingInfo.find('{http://einfracentral.eu}userEmail')
            if loggingInfoUserEmail is not None:
                loggingInfoObject.userEmail = loggingInfoUserEmail.text
            loggingInfoUserFullName = loggingInfo.find('{http://einfracentral.eu}userFullName')
            if loggingInfoUserFullName is not None:
                loggingInfoObject.userFullName = loggingInfoUserFullName.text
            loggingInfoUserRole = loggingInfo.find('{http://einfracentral.eu}userRole')
            if loggingInfoUserRole is not None:
                loggingInfoObject.userRole = loggingInfoUserRole.text
            loggingInfoType = loggingInfo.find('{http://einfracentral.eu}type')
            if loggingInfoType is not None:
                loggingInfoObject.type = loggingInfoType.text
            loggingInfoComment = loggingInfo.find('{http://einfracentral.eu}comment')
            if loggingInfoComment is not None:
                loggingInfoObject.comment = loggingInfoComment.text
            loggingInfoActionType = loggingInfo.find('{http://einfracentral.eu}actionType')
            if loggingInfoActionType is not None:
                loggingInfoObject.actionType = loggingInfoActionType.text
            loggingInfoList.append(loggingInfoObject)
    latest = root.find('{http://einfracentral.eu}latest')
    if latest is not None:
        service_id = service.find('{http://einfracentral.eu}id')
        if latest.text == 'false':
            if service_id is not None and loggingInfoList is not None:
                return json_data.get("id"), service_id.text, loggingInfoList
        else:
            return 'latest', service_id.text, None

    return None, None, None

def version_folders_deletion(directory, versionFoldersIDs):
    count = 0
    for serviceRelatedFolder in serviceRelatedFolders:
        for file in os.listdir(directory + serviceRelatedFolder):
            if file.endswith('-version'):
                if file in versionFoldersIDs:
                    shutil.rmtree(directory + serviceRelatedFolder + file)
                    count = count + 1
    print("Total .version (old version folders) deleted:", count)

def save_loggingInfo_from_oldest_versions(oldLoggingInfos, serviceId, loggingInfoList):
    # SAVE AS A STRING
    # oldLoggingInfos[serviceId] = json.dumps(loggingInfoList[0].asdict())
    # for loggingInfo in loggingInfoList[1:]:
    #     oldLoggingInfos[serviceId] = oldLoggingInfos[serviceId] + ',' + json.dumps(loggingInfo.asdict())
    # return oldLoggingInfos

    # SAVE AS A DICT<STRING,LOGGINGINFO.OBJECT>
    list = []
    for loggingInfo in loggingInfoList:
        list.append(loggingInfo.asdict())
    oldLoggingInfos[serviceId] = list
    return oldLoggingInfos

def update_latest_services_loggingInfo(directory, latestServices, oldLoggingInfos):
    for serviceRelatedFolder in serviceRelatedFolders:
        for file in os.listdir(directory + serviceRelatedFolder):
            if file.endswith('.json'):
                with open(directory + serviceRelatedFolder + file, 'r') as json_file:
                    json_data = json.load(json_file)
                    xml = json_data['payload']
                    ET.register_namespace("tns", "http://einfracentral.eu")
                    root = ET.ElementTree(ET.fromstring(xml))
                    tree = root.getroot()
                    service = root.find('{http://einfracentral.eu}service')
                    serviceId = service.find('{http://einfracentral.eu}id').text
                    if serviceId in latestServices:
                        for oldLoggingInfo in oldLoggingInfos:
                            if (oldLoggingInfo == serviceId):
                                for item in oldLoggingInfos[serviceId]:
                                    loggingInfo = ET.Element("tns:loggingInfo")

                                    loggingInfoDate = ET.Element("tns:date")
                                    loggingInfoDate.text = item['date']
                                    loggingInfo.append(loggingInfoDate)
                                    loggingInfoUserEmail = ET.Element("tns:userEmail")
                                    loggingInfoUserEmail.text = item['userEmail']
                                    loggingInfo.append(loggingInfoUserEmail)
                                    loggingInfoUserFullName = ET.Element("tns:userFullName")
                                    loggingInfoUserFullName.text = item['userFullName']
                                    loggingInfo.append(loggingInfoUserFullName)
                                    loggingInfoUserRole = ET.Element("tns:userRole")
                                    loggingInfoUserRole.text = item['userRole']
                                    loggingInfo.append(loggingInfoUserRole)
                                    loggingInfoType = ET.Element("tns:type")
                                    loggingInfoType.text = item['type']
                                    loggingInfo.append(loggingInfoType)
                                    loggingInfoComment = ET.Element("tns:comment")
                                    loggingInfoComment.text = item['comment']
                                    loggingInfo.append(loggingInfoComment)
                                    loggingInfoActionType = ET.Element("tns:actionType")
                                    loggingInfoActionType.text = item['actionType']
                                    loggingInfo.append(loggingInfoActionType)

                                    tree.append(loggingInfo)

                    # Sort LoggingInfo list
                    allLoggingInfo = root.findall('{http://einfracentral.eu}loggingInfo')
                    tree.extend(sorted(allLoggingInfo, key=lambda x: tree.remove(x) or x.find('{http://einfracentral.eu}date').text))

                    root.write('output.xml')
                    with open("output.xml", "r") as xml_file:
                        content = xml_file.readlines()
                        content = "".join(content)
                        bs_content = bs(content, "xml")
                        json_data['payload'] = str(bs_content)
                    # write to file
                    with open(directory + serviceRelatedFolder + file, 'w') as json_file:
                        json.dump(json_data, json_file, indent=2)
                            

class LoggingInfo:
    date = None
    userEmail = None
    userFullName = None
    userRole = None
    type = None
    comment = None
    actionType = None

    def asdict(self):
        return {'date': self.date, 'userEmail': self.userEmail, 'userFullName': self.userFullName,
                'userRole': self.userRole, 'type': self.type, 'comment': self.comment, 'actionType':  self.actionType}
##################################################### FUNCTIONS ########################################################


######################################################## RUN ###########################################################
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", help="sets the folder path", type=str, required=True)
args = parser.parse_args()
versions_deletion(args.path)
######################################################## RUN ###########################################################