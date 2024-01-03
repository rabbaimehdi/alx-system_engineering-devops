#!/usr/bin/python3
"""Accessing a RESTAPI for todo lists of employees using requests
   and exporting data as a csv file
"""

import requests
from sys import argv, exit
import csv


def main():
    response_user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
    response_todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos")
    USERNAME = response_user.json()["name"]
    LIST_TASKS = []
    for task in response_todos.json():
        DATA = {}
        DATA["USER_ID"] = task["userId"]
        DATA["USERNAME"] = USERNAME
        DATA["TASK_COMPLETED_STATUS"] = task["completed"]
        DATA["TASK_TITLE"] = task["title"]
        LIST_TASKS.append(DATA)

    with open(f"{argv[1]}.csv", "w", newline="") as out:
        dict_writer = csv.DictWriter(out, LIST_TASKS[0].keys())
        dict_writer.writeheader()
        dict_writer.writerows(LIST_TASKS)


if __name__ == "__main__":
    main()
