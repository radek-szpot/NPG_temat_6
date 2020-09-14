#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
A module that saves the data under the chosen path
'''
import json


def save_to_path(path, fileName, list_of_tasks):

    if path[-1] != '\\':  
        path += '\\'

    filePathName = path + fileName + '.json'
    with open(filePathName, 'w') as f:
        f.write(json.dumps(list_of_tasks, indent=4))

    return True
