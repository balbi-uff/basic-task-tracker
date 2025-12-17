import json

from core.Task import Task
from core.TaskStatus import TaskStatus

TASKS_FILENAME = "current_tasks.json"


def createTasksFile(task_file):
    import os
    if not task_file in os.listdir("."):
        with open(task_file, "w") as file:
            file.write("{}")


class TaskHandler:
    task_file = None
    current_tasks = None

    def __init__(self, tasks_filename=TASKS_FILENAME):
        self.task_file = tasks_filename
        createTasksFile(self.task_file)

    def get_current_tasks(self):
        if not self.current_tasks:
            with open(self.task_file, 'r') as file:
                self.current_tasks = json.load(file)
        return self.current_tasks

    def get_all_tasks(self) -> list[Task]:
        processedTasks = []

        tasks = self.get_current_tasks()

        for task in tasks.values():
            local_task = convertLoadedJsonDictToTask(task["id"], task)
            processedTasks.append(local_task)

        return processedTasks

    def save_tasks_dict_in_json_file(self):
        with open(self.task_file, 'w') as json_file:
            json.dump(self.current_tasks, json_file, indent=4)


    def save_task(self, task: Task):
        self.current_tasks = self.get_current_tasks()
        self.current_tasks[task.getId()] = task.toDict()
        self.save_tasks_dict_in_json_file()

    def save_task_as_dict(self, task: dict):
        self.current_tasks[str(task["id"])] = task
        self.save_tasks_dict_in_json_file()

    def mark_task_as_in_progress(self, _id: str):
        self.update_task_by_id(_id, status=TaskStatus.IN_PROGRESS)

    def mark_task_as_done(self, _id: str):
        self.update_task_by_id(_id, status=TaskStatus.DONE)

    def update_task_by_id(self, _id: str, name: str = None, description: str = None, status: TaskStatus = None):
        foundTask: dict = self.get_current_tasks().get(_id)

        if not foundTask:
            raise KeyError("Task was not found!")

        if name:
            foundTask["name"] = name

        if description:
            foundTask["description"] = description

        if status:
            foundTask["status"] = status

        self.save_task_as_dict(foundTask)


    def deleteTaskById(self, _id):
        tasks = self.get_current_tasks()
        del tasks[_id]
        self.save_tasks_dict_in_json_file()

    def save_tasks(self, tasks):
        for task in tasks:
            self.save_task(task)

    def get_task_by_id(self, taskId):
        for t in self.get_all_tasks():
            if t.getId() == taskId:
                return t

    def print_tasks_by_status(self, status: TaskStatus =None):
        """
        If no status is inputed, print all tasks
        :param status: TaskStatus
        :return: None
        """

        for task in self.get_all_tasks():
            if task.getStatus() == status or (not status):
                print(task)


def convertLoadedJsonDictToTask(_id, task_dict):
    return Task(task_dict["name"], task_dict["status"], task_dict["description"]).withId(_id)
