#!/usr/bin/python3
"""
    Exports data in JSON
"""
import json
import requests
from sys import argv

if __name__ == '__main__':

    users = requests.get("https://jsonplaceholder.typicode.com/users")

    users = users.json()

    data = {}
    for user in users:
        list = []
        todos = requests.get(f"https://jsonplaceholder.typicode.com/\
            todos?userId={user['id']}")
        todos = todos.json()
        for todo in todos:
            dictionary = {}

            dictionary["username"] = user["username"]
            dictionary["task"] = todo["title"]
            dictionary["completed"] = todo["completed"]

            list.append(dictionary)
        data[f"{user['id']}"] = list

    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data))
