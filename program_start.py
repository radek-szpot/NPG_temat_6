#!/usr/bin/python
# -*- coding: utf-8 -*-
def start():
    print("Napisz liczbe od 1 do 2 by wybrac dana akcje: \n 1.Dodanie nowego zadania \n 2.Wypisanie zadan")
    action = int(input())
    next_action(action)

def next_action(action=0):
    if action == 1:
        # add_new_task()
        exit()
    elif action == 2:
        print("Ile zadan ma zostac wypisane?")
        task_amount = int(input())
        # write_tasks(task_amount)
    else:
        print("Prosze podac liczbe od 1 do 2")
        action = int(input())
        next_action(action)