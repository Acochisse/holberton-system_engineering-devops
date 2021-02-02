#!/usr/bin/python3
"""gather data from given API"""
import requests
from sys import argv
import csv


users_data = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}'.
    format(argv[1])).json()

todo_list = requests.get(
    'https://jsonplaceholder.typicode.com/todos?userId={}'.
    format(argv[1])).json()

completed_tasks = 0
total_tasks = 0

emp_name = users_data['name']

with open('{}.csv'.format(argv[1]), mode='w') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    for key in todo_list:
        writer.writerow([
            key.get('userId'),
            users_data.get('username'),
            key.get('completed'),
            key.get('title')
        ])
