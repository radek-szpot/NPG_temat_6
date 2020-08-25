#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
modul ladujacy zadania z pliku database.json
'''
import json
import colours

def upload():
    with open('database.json') as f:
        raw_data = f.read()
        json_data = json.loads(raw_data)
        print("Aktualna lista zadan:")
    for i in json_data:
        if i['importance'] == 1:
            colours.prGreen(i['name'])
            print(' -', i['description'])
        elif i['importance'] == 2:
            colours.prYellow(i['name'])
            print(' -', i['description'])
        elif i['importance'] == 3:
            colours.prRed(i['name'])
            print(' -', i['description'])
    return json_data