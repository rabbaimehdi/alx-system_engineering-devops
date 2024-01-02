#!/usr/bin/python3
"""Accessing a RESTAPI for todo lists of employees using requests"""

import requests
from sys import argv, exit


def main():
    response_user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
    response_todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos")
    EMPLOYEE_NAME = response_user.json()["name"]
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = len(response_todos.json())
    LIST_OF_COMPLETED_TASK_TITLES = []
    for task in response_todos.json():
        if (task["completed"] is True):
            NUMBER_OF_DONE_TASKS += 1
            LIST_OF_COMPLETED_TASK_TITLES.append(task["title"])

    print(
        f"Employee {EMPLOYEE_NAME} is done with tasks\
({NUMBER_OF_DONE_TASKS} / {TOTAL_NUMBER_OF_TASKS}): ")
    for completed_task_title in LIST_OF_COMPLETED_TASK_TITLES:
        print(f"\t {completed_task_title}")


if __name__ == "__main__":
    main()
