#!/usr/bin/python3

"""
This script fetches information about a specific employee's TODO list progress
from a REST API and exports it to a CSV file.
"""

import csv
import requests
import sys

def fetch_todo_list_progress(employee_id):
    """
    Fetches and exports the TODO list progress of a specific employee to a CSV file.

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
    employee_username = user_data.get('username')

    csv_file_name = f'{employee_id}.csv'
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for task in todos_data:
            task_completed_status = 'True' if task.get('completed') else 'False'
            csv_writer.writerow([employee_id, employee_username, task_completed_status, task.get('title')])

    print(f'Data exported to {csv_file_name} successfully.')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_list_progress(employee_id)
