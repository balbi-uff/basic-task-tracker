from enum import StrEnum


class TaskStatus(StrEnum):
    UNDEFINED = "undefined"
    IN_PROGRESS = "in-progress"
    TODO = "todo"
    DONE = "done"