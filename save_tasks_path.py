#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

def save_to_path(path, fileName, json_data):
    filePathName = path + fileName + '.json'
    with open(filePathName, 'w') as f:
        f.write(json.dumps(json_data, indent=4))


#tak to ma mniej więcej wygladac???