#!/usr/bin/python3
"""Accessing a RESTAPI for todo lists of employees using requests
   and exporting data as a json file
"""

import requests
from sys import argv, exit
import json


def main():
    response_user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
    response_todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos")
    USERNAME = response_user.json()["username"]
    USER_ID = argv[1]
    USER_DICT = {}
    USER_DICT[USER_ID] = []
    for task in response_todos.json():
        USER_DICT[USER_ID].append(
            {"task": task["title"],
             "completed": task["completed"], "username": USERNAME})
    with open(f"{USER_ID}.json", "w") as out:
        json.dump(USER_DICT, out)


if __name__ == "__main__":
    main()
