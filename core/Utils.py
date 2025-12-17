import datetime
import json

CONFIG_FILENAME = "config.json"
LATEST_ID_JSON_KEYWORD = "latest_id"

DATETIME_FORMAT = "%a %d %b %Y, %I:%M:%S%p"

def getNowAsStr():
    return datetimeToStr(datetime.datetime.now())

def datetimeToStr(datetimeObj: datetime.datetime, format:str = DATETIME_FORMAT):
    return datetimeObj.strftime(format)

def strToDatetime(datetimeStr: str, format: str = DATETIME_FORMAT):
    return datetime.datetime.strptime(datetimeStr, format)


def updateJsonFileLatestId(jsonFileName, newId):
    with open(jsonFileName, "r") as jsonFile:
        jsonObject = json.load(jsonFile)

    jsonObject[LATEST_ID_JSON_KEYWORD] = newId

    with open(jsonFileName, "w") as jsonFile:
        json.dump(jsonObject, jsonFile)


def getNextId(jsonFileName: str =CONFIG_FILENAME) -> int:
    latest_id = getLatestIdFromJsonFile(jsonFileName)
    updateJsonFileLatestId(jsonFileName, latest_id + 1)
    return latest_id

def getLatestIdFromJsonFile(jsonFileName):
    try:
        with open(jsonFileName, "r") as jsonFile:
            jsonObject = json.load(jsonFile)
            return jsonObject[LATEST_ID_JSON_KEYWORD]

    except FileNotFoundError:
        raise FileNotFoundError("JSON config file was not found, create a \"config.json\" in root dir!")

