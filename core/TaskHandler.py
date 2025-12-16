import json

from core.Task import Task

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

        print("ALL TASKS".center(50, "="))
        for task in tasks.values():
            local_task = convertLoadedJsonDictToTask(task["id"], task)
            print(str(local_task))
            processedTasks.append(local_task)

        return processedTasks


    def save_tasks_dict_in_json_file(self):
        with open(self.task_file, 'w') as json_file:
            json.dump(self.current_tasks, json_file, indent=4)


    def save_task(self, task: Task):
        self.current_tasks = self.get_current_tasks()
        self.current_tasks[task.getId()] = task.toDict()
        self.save_tasks_dict_in_json_file()


    def update_task_in_json_file(self, task: Task):
        found = self.get_current_tasks().get(task.getId())

        if not found:
            print("Task was not found!")
            #raise KeyError("Task was not found!")
            return

        foundTask: Task = convertLoadedJsonDictToTask(task.getId(), found)

        print(f"UPDATING... >> {str(foundTask)}")

        foundTask.setName(task.getName())
        foundTask.setStatus(task.getStatus())
        foundTask.setDescription(task.getDescription())
        foundTask.setMarked(task.getMarkedStatus())

        self.save_task(foundTask)
        print(F"UPDATED >> {str(foundTask)}")

    def deleteTaskById(self, _id):
        tasks = self.get_current_tasks()
        del tasks[_id]
        self.save_tasks_dict_in_json_file()

    def save_tasks(self, tasks):
        for task in tasks:
            self.save_task(task)


def convertLoadedJsonDictToTask(_id, task_dict):
    return Task(task_dict["name"], task_dict["status"], task_dict["description"], task_dict["marked"]).withId(_id)
