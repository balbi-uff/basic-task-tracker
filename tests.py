import os

import pytest

from core.Task import Task
from core.TaskHandler import TaskHandler
from core.TaskStatus import TaskStatus

JSON_TEST_FILENAME = "tasks_test.json"
taskHandler: TaskHandler

def deleteTestFile(filename: str):
    os.remove(filename)

class TestTaskTracker():
    @pytest.fixture()
    def standart_setup_teardown(self):
        global taskHandler

        print("\nRunning test setup.")
        taskHandler = TaskHandler(tasks_filename=JSON_TEST_FILENAME)

        yield taskHandler

        deleteTestFile(JSON_TEST_FILENAME)

    def test_create_task(self, standart_setup_teardown):
        name = "Test task"
        status = TaskStatus.TODO
        description = "Lorem ipsum dolor sit amet"

        newTask = Task(name, status, description)

        taskHandler.save_task(newTask)
        allTasks = taskHandler.get_all_tasks()
        savedTask = allTasks[0]

        assert savedTask.getId() == newTask.getId()
        assert savedTask.getName() == newTask.getName()
        assert savedTask.getStatus() == newTask.getStatus()
        assert savedTask.getDescription() == newTask.getDescription()

    def test_readall_tasks(self, standart_setup_teardown):
        t1 = Task("temptask", "DONE", "lorem ipsum dolor")
        t2 = Task("temptask", "DONE", "lorem ipsum dolor")
        t3 = Task("temptask", "DONE", "lorem ipsum dolor")

        taskHandler.save_tasks([t1, t2, t3])
        assert len(taskHandler.get_all_tasks()) == 3

    def test_update_task(self, standart_setup_teardown):
        name = "Test task"
        status = TaskStatus.TODO
        description = "Lorem ipsum dolor sit amet"

        newTask = Task(name, status, description)

        taskHandler.save_task(newTask)

        allTasks = taskHandler.get_all_tasks()
        savedTask = allTasks[0]

        taskHandler.update_task_by_id(savedTask.getId(),
                                      name="NEWNAME",
                                      status=TaskStatus.IN_PROGRESS,
                                      description="13243546576879")

        allTasks = taskHandler.get_all_tasks()
        savedTask = allTasks[0]

        assert savedTask.getId() == newTask.getId()
        assert savedTask.getName() == "NEWNAME"
        assert savedTask.getStatus() == str(TaskStatus.IN_PROGRESS)
        assert savedTask.getDescription() == "13243546576879"

    def test_delete_task(self, standart_setup_teardown):
        name = "Test task"
        status = TaskStatus.TODO
        description = "Lorem ipsum dolor sit amet"

        newTask = Task(name, status, description)

        taskHandler.save_task(newTask)
        taskHandler.deleteTaskById(newTask.getId())
        allTasks = taskHandler.get_all_tasks()

        assert len(allTasks) == 0

    def test_mark_task_as_done(self, standart_setup_teardown):
        name = "Test task"
        status = TaskStatus.TODO
        description = "Lorem ipsum dolor sit amet"

        newTask = Task(name, status, description)

        taskHandler.save_task(newTask)

        firstLen = len(taskHandler.get_all_tasks())

        taskHandler.mark_task_as_done(newTask.getId())
        assert taskHandler.get_task_by_id(newTask.getId()).getStatus() == TaskStatus.DONE
        assert len(taskHandler.get_all_tasks()) == firstLen

    def test_mark_task_in_progress(self, standart_setup_teardown):
        name = "Test task"
        status = TaskStatus.TODO
        description = "Lorem ipsum dolor sit amet"

        newTask = Task(name, status, description)

        taskHandler.save_task(newTask)
        firstLen = len(taskHandler.get_all_tasks())

        taskHandler.mark_task_as_in_progress(newTask.getId())
        assert taskHandler.get_task_by_id(newTask.getId()).getStatus() == TaskStatus.IN_PROGRESS
        assert len(taskHandler.get_all_tasks()) == firstLen

    def test_show_only_done_status_task(self, standart_setup_teardown):
        ...

    def test_show_only_not_done_status_task(self, standart_setup_teardown):
        ...

    def test_show_only_in_progress_status_task(self, standart_setup_teardown):
        ...