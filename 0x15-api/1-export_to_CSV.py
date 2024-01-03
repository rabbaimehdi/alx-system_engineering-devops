#!/usr/bin/python3
"""Accessing a RESTAPI for todo lists of employees using requests
   and exporting data as a csv file
"""

import requests
from sys import argv, exit


def main():
    response_user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
    response_todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos")
    USERNAME = response_user.json()["name"]
    with open(f"{argv[1]}.csv", "w") as out:
        for task in response_todos.json():
            out.write(
                '"{}","{}","{}","{}"\n'.format(
                    argv[1],
                    USERNAME,
                    task['completed'],
                    task['title']))


if __name__ == "__main__":
    main()
