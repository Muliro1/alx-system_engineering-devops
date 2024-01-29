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

    sessionReq = requests.Session()

    id_Emp = argv[1]
    id_URL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format
    (id_Emp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(id_Emp)

    employee = sessionReq.get(id_URL)
    employeeName = sessionReq.get(nameURL)

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
    updateUser[id_Emp] = totalTasks

    file_Json = id_Emp + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)
