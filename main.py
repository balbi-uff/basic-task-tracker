import argparse

from core.Task import Task
from core.TaskHandler import TaskHandler

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

parser.add_argument("-c", "--create", action="store_true") #create task
parser.add_argument("-r", "--read-all", action="store_true")
parser.add_argument("-u", "--update", action="store_true")
parser.add_argument("-d", "--delete", action="store_true")


# Update args
parser.add_argument("-id", default=None)


# Shared args
parser.add_argument("-m", "--marked", action="store_true")
parser.add_argument("--name", nargs="?", const="Unnamed Task", default=None)
parser.add_argument("--description", nargs="?", const="", default=None)
parser.add_argument("-s", "--status", nargs="?", const="PENDING", default=None)


args = parser.parse_args()
taskHandler = TaskHandler()

if __name__ == '__main__':
    if args.create:
        newTask = Task(args.name, args.status, description=args.description, marked=args.marked)
        print(f"CREATED >> {str(newTask)}")
        taskHandler.save_task(newTask)
        print(f"SAVED >> {str(newTask)}")

    elif args.update:
        updatedTask = Task(args.name, args.status, args.description).withId(args.id)
        taskHandler.update_task_in_json_file(updatedTask)

    elif args.read_all:
        taskHandler.print_all_tasks()

    elif args.delete:
        taskHandler.deleteTaskById(args.id)

