# Basic Task Tracker


The user should be able to:

- [X] Add, Update, and Delete tasks

Adding a task: `py .\task-cli.py add "Buy groceries"`


**Requirements**:
- [X] Mark a task as in progress or done

- [X] List all tasks

- [X] List all tasks that are done

- [X] List all tasks that are not done

- [X] List all tasks that are in progress

### Use example
```shell
py .\task-cli.py add "Buy groceries"
py .\task-cli.py update 1 "Buy groceries and cook dinner"
py .\task-cli.py delete 1

py .\task-cli.py add "Do stuff"
py .\task-cli.py update 2 "Do stuff and idk do more stuff..."
py .\task-cli.py mark-in-progress 2
py .\task-cli.py list in-progress

py .\task-cli.py mark-done 2
py .\task-cli.py list done

py .\task-cli.py add "Do stuff 2"
py .\task-cli.py add "Do stuff 3"
py .\task-cli.py add "Do stuff 4"
py .\task-cli.py list

```