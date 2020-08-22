#!/usr/bin/python
# -*- coding: utf-8 -*-

#from add_new_task import add_new_task      <- nazwy robocze; dodane zeby nie zapomniec o imporcie
#from print_tasks import print_tasks

def start():
    print("Napisz liczbe od 1 do 2 by wybrac dana akcje: \n 1.Dodanie nowego zadania \n 2.Wypisanie zadan")
    action = int(input())
    next_action(action)

def next_action(listOfTasks, action=0):  #dodałem drugi arguement czyli liste zadań która będzie listą dwuwymiarową
        #pierwszy wymiar w liście będzie miał za zadanie określić wagę/priorytet zadania, drugi zaś będzie przechowywał zadania

    if action == 1:
        # add_new_task() TODO:PAWEL
        exit()
    elif action == 2:
        print("Ile zadan ma zostac wypisane?")
        task_amount = int(input())
        # print_tasks(task_amount) TODO:BASIA
    else:
        print("Prosze podac liczbe od 1 do 2")
        action = int(input())
        next_action(action)