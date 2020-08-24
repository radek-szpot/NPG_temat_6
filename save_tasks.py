#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
modul zapisujacy dane do pliku database.json
'''
import json

def save(json_data):
    with open('database.json', mode="w") as f:
        f.write(json.dumps(json_data))

def save_to_location(json_data):
    exit()