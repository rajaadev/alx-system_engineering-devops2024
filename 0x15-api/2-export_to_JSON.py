#!/usr/bin/python3

import json
import requests
import sys

def main():
    """Main function to gather TODO list data for an employee and export to JSON."""
    # Check if an employee ID is provided
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        return

    employee_id = int(sys.argv[1])

    # API URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Get user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("username")  # Get the username

    # Get TODO data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Prepare the output data
    output_data = {employee_id: []}

    for todo in todos_data:
        task_info = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": employee_name
        }
        output_data[employee_id].append(task_info)

    # Define the JSON file name
    json_file_name = f"{employee_id}.json"

    # Write data to JSON file
    with open(json_file_name, mode='w') as json_file:
        json.dump(output_data, json_file)

if __name__ == "__main__":
    main()
