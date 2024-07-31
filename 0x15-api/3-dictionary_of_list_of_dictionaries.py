import json
import requests

def fetch_todo_data():
    # Fetch users and todos from the JSONPlaceholder API
    users_response = requests.get("https://jsonplaceholder.typicode.com/users")
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")

    if users_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data from the API.")
        return {}

    users = users_response.json()
    todos = todos_response.json()

    # Create a dictionary to hold the tasks for each user
    tasks_by_user = {}

    # Populate the dictionary with tasks for each user
    for user in users:
        user_id = str(user['id'])
        username = user['username']
        
        # Initialize the list for this user
        tasks_by_user[user_id] = []
        
        # Filter todos for this user
        for todo in todos:
            if todo['userId'] == user['id']:
                task_info = {
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                tasks_by_user[user_id].append(task_info)

    return tasks_by_user

def save_to_json(data):
    # Write the data to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)

def main():
    # Fetch the data and save it to a JSON file
    todo_data = fetch_todo_data()
    save_to_json(todo_data)

if __name__ == "__main__":
    main()
