#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
modul zapisujacy dane do pliku database.json
'''
import json

def save(json_data):
    with open('database.json', mode="w") as f:
        f.write(json.dumps(json_data))

    with open('database.json') as f:
        raw_data = json.load(f)
    with open('database.json', mode="w") as f:
        json.dump(raw_data, f, indent=4)