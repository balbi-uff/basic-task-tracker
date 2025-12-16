import os

import pytest

from core.Task import Task
from core.TaskHandler import TaskHandler
from core.TaskStatus import TaskStatus

JSON_TEST_FILENAME = "tasks_test.json"
taskHandler: TaskHandler

def deleteTestFile(filename: str):
    os.remove(filename)


@pytest.fixture()
def standart_setup_teardown():
    global taskHandler

    print("\nRunning test setup.")
    taskHandler = TaskHandler(tasks_filename=JSON_TEST_FILENAME)

    yield taskHandler

    deleteTestFile(JSON_TEST_FILENAME)

def test_create_task(standart_setup_teardown):
    name = "Test task"
    status = TaskStatus.TODO
    description = "Lorem ipsum dolor sit amet"
    marked = True

    newTask = Task(name, status, description, marked)

    taskHandler.save_task(newTask)
    allTasks = taskHandler.get_all_tasks()
    savedTask = allTasks[0]

    assert savedTask.getId() == newTask.getId()
    assert savedTask.getName() == newTask.getName()
    assert savedTask.getStatus() == newTask.getStatus()
    assert savedTask.getDescription() == newTask.getDescription()
    assert savedTask.getMarkedStatus() == newTask.getMarkedStatus()

def test_readall_tasks(standart_setup_teardown):
    t1 = Task("temptask", "DONE", "lorem ipsum dolor", True)
    t2 = Task("temptask", "DONE", "lorem ipsum dolor", False)
    t3 = Task("temptask", "DONE", "lorem ipsum dolor", True)

    taskHandler.save_tasks([t1, t2, t3])
    assert len(taskHandler.get_all_tasks()) == 3


def test_update_task(standart_setup_teardown):
    name = "Test task"
    status = TaskStatus.TODO
    description = "Lorem ipsum dolor sit amet"
    marked = True

    newTask = Task(name, status, description, marked)

    taskHandler.save_task(newTask)

    allTasks = taskHandler.get_all_tasks()
    savedTask = allTasks[0]

    savedTask.setName("NEWNAME")
    savedTask.setStatus(TaskStatus.IN_PROGRESS)
    savedTask.setDescription("13243546576879")

    taskHandler.update_task_in_json_file(savedTask)

    allTasks = taskHandler.get_all_tasks()
    savedTask = allTasks[0]

    assert savedTask.getId() == newTask.getId()
    assert savedTask.getName() == "NEWNAME"
    assert savedTask.getStatus() == str(TaskStatus.IN_PROGRESS)
    assert savedTask.getDescription() == "13243546576879"
    assert savedTask.getMarkedStatus() == True

def test_delete_task(standart_setup_teardown):
    ...

def test_mark_task(standart_setup_teardown):
    ...

def test_show_only_done_status_task(standart_setup_teardown):
    ...

def test_show_only_not_done_status_task(standart_setup_teardown):
    ...

def test_show_only_in_progress_status_task(standart_setup_teardown):
    ...