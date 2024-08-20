#!/usr/bin/python3
import json
import requests

# Fetch users and todos from API
users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

users_response = requests.get(users_url)
todos_response = requests.get(todos_url)

users = users_response.json()
todos = todos_response.json()

# Create a dictionary with user IDs as keys
tasks_by_user = {}
for user in users:
    tasks_by_user[user['id']] = []

# Populate the dictionary with tasks
for todo in todos:
    user_id = todo['userId']
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        task_entry = {
            "username": user['username'],
            "task": todo['title'],
            "completed": todo['completed']
        }
        tasks_by_user[user_id].append(task_entry)

# Write the dictionary to a JSON file
with open('todo_all_employees.json', 'w') as f:
    json.dump(tasks_by_user, f)
