#!/usr/bin/python3
"""
Fetches data from a REST API and exports it to JSON format.
Usage: python3 script.py [USER_ID]
"""

import json
import requests
from sys import argv

def export_tasks_to_json(user_id=""):
    """
    Fetches tasks data from a REST API and exports it to JSON format.

    Args:
        user_id (str): Optional user ID to fetch tasks for a specific user.

    Returns:
        None
    """
    url_users = "https://jsonplaceholder.typicode.com/users"
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}" if user_id else "https://jsonplaceholder.typicode.com/todos"

    try:
        response_users = requests.get(url_users)
        response_todos = requests.get(url_todos)

        if response_users.status_code != 200 or response_todos.status_code != 200:
            print("Error fetching data.")
            return

        users_data = response_users.json()
        todos_data = response_todos.json()

        user_tasks = {}
        for user in users_data:
            user_id = str(user["id"])
            username = user["username"]
            user_tasks[user_id] = []

            for todo in todos_data:
                if str(todo["userId"]) == user_id:
                    task_info = {
                        "username": username,
                        "task": todo["title"],
                        "completed": todo["completed"]
                    }
                    user_tasks[user_id].append(task_info)

        with open("todo_all_employees.json", "w") as file:
            json.dump(user_tasks, file)

        print("Data exported to todo_all_employees.json successfully.")

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    user_id = argv[1] if len(argv) == 2 else ""
    export_tasks_to_json(user_id)

