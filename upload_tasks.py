#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
The module loads tasks from database.json file
'''
import json
import colours

def upload():
    with open('database.json') as f:
        raw_data = f.read()
        list_of_tasks = json.loads(raw_data)
        print("Aktualna lista zadan:")
    for i in list_of_tasks:
        if i['importance'] == 1:
            colours.prGreen(i['name'])
            print(' -', i['description'])
        elif i['importance'] == 2:
            colours.prYellow(i['name'])
            print(' -', i['description'])
        elif i['importance'] == 3:
            colours.prRed(i['name'])
            print(' -', i['description'])
    return list_of_tasks
