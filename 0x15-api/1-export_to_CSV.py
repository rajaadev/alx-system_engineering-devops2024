#!/usr/bin/python3

import csv
import requests
import sys

def main():
    """Main function to gather TODO list data for an employee and export to CSV."""
    # Check if an employee ID is provided
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        return

    employee_id = int(sys.argv[1])

    # API URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Get user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("username")  # Change to get the username

    # Get TODO data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Define the CSV file name
    csv_file_name = f"{employee_id}.csv"

    # Write data to CSV
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            # Write each task with the required format
            csv_writer.writerow([employee_id, employee_name, todo.get("completed"), todo.get("title")])

if __name__ == "__main__":
    main()
