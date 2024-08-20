#!/usr/bin/python3
"""Script that uses a REST API to gather information about an employee's TODO
list progress."""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and display employee TODO list progress based on their ID."""
    # URLs for user and TODO data
    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    url_todos = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    )

    # Fetching user data
    user_response = requests.get(url_user)
    if user_response.status_code != 200:
        print("Error: User not found")
        return

    user_data = user_response.json()

    # Fetching TODO list data
    todos_response = requests.get(url_todos)
    todos_data = todos_response.json()

    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]

    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/"
          f"{total_tasks}):")

    # Print titles of completed tasks
    for task in done_tasks:
        print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
