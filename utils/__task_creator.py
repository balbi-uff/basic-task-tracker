import os
import random

task_names = [f"Task {i}" for i in range(1, 11)]
task_descriptions = [f"Description for task {i}" for i in range(1, 21)]

for name, description in zip(task_names, task_descriptions):
    os.system(f'py .\\task-cli.py add "{name}" "{description}"')