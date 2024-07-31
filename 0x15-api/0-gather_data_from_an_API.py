#!/usr/bin/python3

import requests
import sys

def main():
    # Check if the employee ID is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        return

    employee_id = int(sys.argv[1])

    # Define the API URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Get user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get todo data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate completed tasks
    completed_tasks = [todo.get("title") for todo in todos_data if todo.get("completed")]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    # Display the results
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    main()

