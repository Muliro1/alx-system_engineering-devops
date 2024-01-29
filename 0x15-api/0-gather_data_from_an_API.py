#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    id_Emp = argv[1]
    id_URL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id_Emp)
    name_URL = 'https://jsonplaceholder.typicode.com/users/{}'.format(id_Emp)

    employee = sessionReq.get(id_URL)
    employeeName = sessionReq.get(name_URL)

    json_req = employee.json()
    name = employeeName.json()['name']

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, totalTasks, len(json_req)))
    for done_tasks in json_req:
        if done_tasks['completed']:
            print("\t " + done_tasks.get('title'))
