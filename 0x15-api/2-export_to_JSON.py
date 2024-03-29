#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
and export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    session_Req = requests.Session()

    id_E = argv[1]
    id_URL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id_E)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(id_E)

    employee = session_Req.get(id_URL)
    employeeName = session_Req.get(nameURL)

    json_req = employee.json()
    usr = employeeName.json()['username']

    totalTasks = []
    updateUser = {}

    for all_Emp in json_req:
        totalTasks.append(
            {
                "task": all_Emp.get('title'),
                "completed": all_Emp.get('completed'),
                "username": usr,
            })
    updateUser[id_E] = totalTasks

    file_Json = id_E + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)
