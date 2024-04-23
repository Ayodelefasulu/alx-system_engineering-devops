#!/usr/bin/python3

"""
This script fetches information about a specific employee's TODO list progress
from a REST API and exports it to a JSON file in the specified format.
"""

import json
import requests
import sys

def fetch_todo_list_progress(employee_id):
    """
    Fetches and exports the TODO list progress of a specific employee to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
    """
    base_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'{base_url}/todos'
    user_response = requests.get(base_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error fetching data. Please check the employee ID.")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_username = user_data.get('username')

    json_data = {str(employee_id): []}
    for task in todos_data:
        task_completed_status = task.get('completed')
        task_title = task.get('title')
        json_data[str(employee_id)].append({
            'task': task_title,
            'completed': task_completed_status,
            'username': employee_username
        })

    json_file_name = f'{employee_id}.json'
    with open(json_file_name, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f'Data exported to {json_file_name} successfully.')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list_progress(employee_id)

