#!/usr/bin/python3
"""gather data from given API"""
import requests
import json


users_data = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}'.json())

dictionary = {}

for key in users_data:
    new_todo = []
    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.
        format(key.get('id'))).json()

    for subkey in todo_list:
        todo = {}
        todo['task'] = subkey.get('title')
        todo['completed'] = subkey.get('completed')
        todo['username'] = subkey.get('username')
        new_todo.append(todo)
    dictionary[key.get('id')] = new_todo

with open('todo_all_employees.json', mode='w') as jsonfile:
    json.dump(dictionary, jsonfile)
