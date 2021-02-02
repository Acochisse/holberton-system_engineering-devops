#!/usr/bin/python3
"""gather data from given API"""
import requests
from sys import argv
import json


users_data = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}'.
    format(argv[1])).json()

todo_list = requests.get(
    'https://jsonplaceholder.typicode.com/todos?userId={}'.
    format(argv[1])).json()

completed_tasks = 0
total_tasks = 0

emp_name = users_data['name']

todos = []

for key in todo_list:
    new = {}
    new['task'] = key.get('title')
    new['completed'] = key.get('completed')
    new['username'] = key.get('username')
    todos.append(new)

dictionary = {argv[1]: todos}

with open('{}.json'.format(argv[1]), mode='w') as jsonfile:
    json.dump(dictionary, jsonfile)
