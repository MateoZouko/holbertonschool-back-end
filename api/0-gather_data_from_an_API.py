#!/usr/bin/python3
"""
Summary : Api requesting employee information
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    """ Module for Asking apis info"""
    employee_id = argv[1]
    urlToDo = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    urlUsers = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(urlToDo)
    responseuser = requests.get(urlUsers)
    sum = 0

    if response.status_code >= 400 and responseuser.status_code >= 400:
        print("Error fetching data")
        exit()
    if response.status_code >= 400 and responseuser.status_code >= 400:
        print("Error fetching data")
        exit()
    employee = response.json()
    employeeinfo = responseuser.json()
    name = employeeinfo['name']
    for task in employee:
        if task['completed'] is True:
            sum += 1
    print(f"Employee {name} is done with tasks({sum}/{len(employee)}):")
    for task in employee:
        if task['completed'] is True:
            print(f"\t {task['title']}")
