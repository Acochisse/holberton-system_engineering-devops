#!/usr/bin/python3
""" export api data to JSON """
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    users_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.
        format(argv[1])).json()

    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/usersId={}'.
        format(argv[1])).json()

    employee_name = users_data['name']
    completed_tasks = 0
    total_tasks = 0

    todos = []
    for key in todo_list:
        todo = {}
        todo['task'] = key.get('title')
        todo['completed'] = key.get('completed')
        todo['username'] = key.get('username')
        todos.append(todo)


        dictionary = {argv[1]: todos}

        with open('{}.json'.format(argv[1]), mode='w') as jsonfile:
            json.dump(dictionary, jsonfile)
