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

# Create a dictionary with user IDs as keys and usernames
tasks_by_user = {
    user['id']: {"username": user['username'], "tasks": []}
    for user in users
}

# Populate the dictionary with tasks
for todo in todos:
    user_id = todo['userId']
    task_entry = {
        "task": todo['title'],
        "completed": todo['completed']
    }
    tasks_by_user[user_id]["tasks"].append(task_entry)

# Convert: {user_id: [{"username": ..., "task": ..., "completed": ...}]}
tasks_by_user = {
    user_id: [
        {"username": info["username"], **task}
        for task in info["tasks"]
    ]
    for user_id, info in tasks_by_user.items()
}

# Write the dictionary to a JSON file
with open('todo_all_employees.json', 'w') as f:
    json.dump(tasks_by_user, f)
