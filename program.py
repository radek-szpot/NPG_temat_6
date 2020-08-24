#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
glowna czesc wykonawcza aplikacji
'''
from add_new_task import add_new_task
from upload_tasks import upload
from save_tasks import save
#from print_tasks import print_tasks

def start():
    json_data = upload()
    print("Napisz liczbe od 1 do 3 by wybrac dana akcje: \n 1.Dodanie nowego zadania \n 2.Wypisanie zadan \n 3.Zamkniecie programu")
    action = int(input())
    next_action(action, json_data)

def next_action(action, json_data):
    #INFO DO PAWMANA - chcialbym zebys przekazywal nowa liste powiekszona o kolejne "zadanie" do json_data tak aby mozna bylo z nowych danych korzystac
    if action == 1:
        json_data = add_new_task(json_data)
        save(json_data)

    elif action == 2:
        print("Ile zadan ma zostac wypisane? By wypisac wszystkie napisz 0")
        task_amount = int(input())
        if task_amount < 0:
            print("Nie mozna wypisac ujemnej liczby zadan")
            next_action(2, json_data)
        else:
            # print_tasks(task_amount, json_data) TODO:BASIA
            exit()

    elif action == 3:
        save(json_data)
        exit()

    else:
        print("Prosze podac liczbe od 1 do 3")
        action = int(input())
        next_action(action)