#!/usr/bin/python3
"""Script that uses a REST API to export employee TODO list data to CSV."""

import csv
import requests
import sys


def export_to_csv(employee_id):
    """Fetch employee TODO list data and export it to a CSV file."""
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

    # Define CSV file name
    csv_file_name = f"{employee_id}.csv"

    # Write data to CSV
    with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                username,
                str(task.get('completed')).capitalize(),
                task.get('title')
            ])

    print(f"Data has been exported to {csv_file_name}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    export_to_csv(employee_id)
