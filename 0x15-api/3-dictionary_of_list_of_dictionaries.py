#!/usr/bin/python3
"""Accessing a RESTAPI for todo lists of employees using requests
   and exporting data as a csv file
"""

import json
import requests
from sys import argv, exit


def main():
    response_users = requests.get("https://jsonplaceholder.typicode.com/users")
    response_todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    users = response_users.json()
    tasks = response_todos.json()
    todos_all_employees_dict = {}

    for user in users:
        todos_all_employees_dict[user["id"]] = []
        for task in tasks:
            if task["userId"] == user["id"]:
                todos_all_employees_dict[user["id"]].append(
                    {"username": user["username"],
                     "task": task["title"], "completed": task["completed"]})

    with open("todo_all_employees.json", "w") as out:
        json.dump(todos_all_employees_dict, out)


if __name__ == "__main__":
    main()
