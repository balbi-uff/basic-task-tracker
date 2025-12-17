import json
from core.TaskStatus import TaskStatus

CONFIG_FILENAME = "config.json"
LATEST_ID_JSON_KEYWORD = "latest_id"

def getLatestIdFromJsonFile(jsonFileName):
    try:
        with open(jsonFileName, "r") as jsonFile:
            jsonObject = json.load(jsonFile)
            return jsonObject[LATEST_ID_JSON_KEYWORD]

    except FileNotFoundError:
        raise FileNotFoundError("JSON config file was not found, create a \"config.json\" in root dir!")

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

class Task:
    status: str
    _id: str

    def __init__(self, name, status: TaskStatus, description):
        self.name = name
        self._id = str(getNextId())
        self.status = str(status)
        self.description = description
    
    def toDict(self):
        return {
            "name" : self.name,
            "id" : self._id,
            "status" : self.status,
            "description": self.description,
        }

    def __str__(self):
        return f"Task:: id={self._id} | status={self.status} | name={self.name} | description={self.description}... "


    def getName(self):
        return self.name

    def getStatus(self):
        return self.status

    def getDescription(self):
        return self.description

    def setVar(self, var, atr_name):
        if var:
            setattr(self, atr_name, var)
        return self

    def withId(self, _id):
        self._id = _id
        return self

    def getId(self):
        return self._id

    def setName(self, name):
        return self.setVar(name, "name")

    def setStatus(self, status):
        return self.setVar(str(status), "status")

    def setDescription(self, description):
        return self.setVar(description, "description")
