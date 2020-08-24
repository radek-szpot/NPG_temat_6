#!/usr/bin/python
# -*- coding: utf-8 -*-

from add_new_task import add_new_task
#from print_tasks import print_tasks

def start():
    print("Napisz liczbe od 1 do 3 by wybrac dana akcje: \n 1.Dodanie nowego zadania \n 2.Wypisanie zadan \n 3.Zamkniecie programu")
    action = int(input())
    next_action(action)

def next_action(action=0):
    if action == 1:
        add_new_task()
        exit()
    elif action == 2:
        print("Ile zadan ma zostac wypisane?")
        task_amount = int(input())
        # print_tasks(task_amount) TODO:BASIA
    elif action == 3:
        # zapisz akutalna liste zadan TODO:RADEK
        exit()
    else:
        print("Prosze podac liczbe od 1 do 3")
        action = int(input())
        next_action(action)