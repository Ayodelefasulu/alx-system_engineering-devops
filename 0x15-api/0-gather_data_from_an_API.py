#!/usr/bin/python3

"""
This script fetches information about a specific employee's TODO list progress
from a REST API and displays it in a specific format.
"""

import requests
import sys

def fetch_todo_list_progress(employee_id):
    """
    Fetches and displays the TODO list progress of a specific employee.

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

    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    completed_tasks = len([task for task in todos_data if task.get('completed')])

    print(f'Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):')
    for task in todos_data:
        if task.get('completed'):
            print(f'\t{task.get("title")}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list_progress(employee_id)
