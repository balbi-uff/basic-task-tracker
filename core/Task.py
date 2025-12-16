from uuid import uuid4
from core.TaskStatus import TaskStatus


class Task:
    status: str

    def __init__(self, name, status: TaskStatus, description, marked):
        self.name = name
        self.id = str(uuid4().hex)[:4] # essa limitação de :4 é somente para testes
        self.status = str(status)
        self.description = description
        self.marked = marked
    
    def toDict(self):
        return {
            "name" : self.name,
            "id" : self.id,
            "status" : self.status,
            "description": self.description,
            "marked": self.marked
        }

    def __str__(self):
        return f"Task:: id={self.id} | status={self.status} | marked={self.marked} | name={self.name} | description={self.description}... "

    def getMarkedStatus(self):
        return self.marked

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
        self.id = _id
        return self

    def getId(self):
        return self.id

    def setName(self, name):
        return self.setVar(name, "name")

    def setStatus(self, status):
        return self.setVar(str(status), "status")

    def setDescription(self, description):
        return self.setVar(description, "description")

    def setMarked(self, marked_status):
        return self.setVar(marked_status, "marked")

