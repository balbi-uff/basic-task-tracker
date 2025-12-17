from datetime import datetime
import json
from core.TaskStatus import TaskStatus
from core.Utils import datetimeToStr, getNextId, getNowAsStr


class Task:
    status: str
    _id: str


    def __init__(self, name, status: TaskStatus, description):
        self.name = name
        self._id = str(getNextId())
        self.status = str(status)
        self.description = description
        self.creationDate = datetimeToStr(datetime.now())
        self.updateDate = self.creationDate
    
    def toDict(self):
        return {
            "name" : self.name,
            "id" : self._id,
            "status" : self.status,
            "description": self.description,
            "creationDate" : self.creationDate,
            "updateDate" : self.updateDate
        }

    def __str__(self):
        return f"Task:: id={self._id} | status={self.status} | createdAt: {self.creationDate} | updatedAt: {self.updateDate} |name={self.name} | description={self.description}... "


    def getName(self):
        return self.name

    def getStatus(self):
        return self.status

    def getDescription(self):
        return self.description

    def getId(self):
        return self._id

    def setName(self, name):
        return self.setVar(name, "name")

    def setStatus(self, status):
        return self.setVar(str(status), "status")

    def setDescription(self, description):
        return self.setVar(description, "description")

    def setId(self, _id):
        return self.setVar(_id, "_id")

    def setVar(self, var, atr_name):
        if var:
            self.updateDateOfTask()
            setattr(self, atr_name, var)
        return self

    def updateDateOfTask(self):
        self.updateDate = getNowAsStr()

