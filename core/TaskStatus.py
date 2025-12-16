from enum import Enum

class TaskStatus(Enum):
    UNDEFINED = "UNDEFINED"
    IN_PROGRESS = "IN_PROGRESS"
    TODO = "TODO"
    DONE = "DONE"