#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import Saving_files

def add_task(id, name, desc):
    return {'id': id, 'nazwa': name, 'opis': desc}

lista_todos = []
lista_todos.append(add_task(60, 'nazwa1', 'olpis1'))
lista_todos.append(add_task(99, 'nazwa2', 'olpis3'))
lista_todos.append(add_task(2, 'nazwa3', 'olpis4'))
lista_todos.append(add_task(3, 'nazwa4', 'olpis5'))

with open('myfile.json', mode="w") as f:
    f.write(json.dumps(lista_todos))

with open('myfile.json') as f:
    raw_data = f.read()

json_data = json.loads(raw_data)

ordered_data = {}
for iterat in json_data:
    ordered_data[iterat['id']] = iterat

print(ordered_data)