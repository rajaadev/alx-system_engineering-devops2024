#!/usr/bin/python3
"""Script that uses a REST API to export employee TODO list data to JSON."""

import json
import requests
import sys


def export_to_json(employee_id):
    """Fetch employee TODO list data and export it to a JSON file."""
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

    username = user_data.get('username')

    # Prepare data for JSON export
    tasks_list = [
        {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        for task in todos_data
    ]

    # Define JSON file name
    json_file_name = f"{employee_id}.json"

    # Write data to JSON file
    with open(json_file_name, 'w', encoding='utf-8') as file:
        json.dump({str(employee_id): tasks_list}, file, indent=4)

    print(f"Data has been exported to {json_file_name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    export_to_json(employee_id)
