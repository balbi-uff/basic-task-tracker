import argparse

from core.Task import Task
from core.TaskHandler import TaskHandler
from core.TaskStatus import TaskStatus

epilog = """
The user should be able to:

\tAdd, Update, and Delete tasks

\tMark a task as in progress or done

\tList all tasks

\tList all tasks that are done

\tList all tasks that are not done

\tList all tasks that are in progress
"""

parser = argparse.ArgumentParser(
                prog='Task CLI',
                description='Organize tasks',
                epilog=epilog)

parser.add_argument("args", nargs="*")

args = parser.parse_args().args
taskHandler = TaskHandler()


if __name__ == '__main__':
    if args[0] == "add":
        try:
            description = args[2]
        except IndexError:
            description = ""

        newTask = Task(args[1], TaskStatus.TODO, description=description)
        taskHandler.save_task(newTask)
        print(f"Task added successfully (ID: {newTask.getId()})")

    elif args[0] == "list":
        try:
            if args[1]:
                taskHandler.print_tasks_by_status(status=args[1])
        except IndexError:
            taskHandler.print_tasks_by_status()

    elif args[0] == "delete":
        try:
            taskHandler.deleteTaskById(args[1])
            print(f"Task deleted! (ID: {args[1]}) ")
        except KeyError:
            print(f"Task with (ID: {args[1]}) does not exist!")

    try:
        if args[0] == "mark-in-progress":
            taskHandler.mark_task_as_in_progress(args[1])

        elif args[0] == "update":
            taskHandler.update_task_by_id(args[1], name=args[2], description=None)

        elif args[0] == "mark-done":
            taskHandler.mark_task_as_done(args[1])

    except KeyError as e:
        print(e)


