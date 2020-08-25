#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
glowna czesc wykonawcza aplikacji
'''
from add_new_task import add_new_task
from upload_tasks import upload
from save_tasks import save
# from edit_Tasks import edit
# from delete_Tasks import delete_tasks
# from print_tasks import print_tasks

def start():
    json_data = upload()
    next_action(json_data)

def next_action(json_data):
    print("\n","Napisz liczbe od 1 do 3 by wybrac dana akcje: \n",
        " 1.Dodanie nowego zadania \n",
        " 2.Wypisanie zadan \n",
        " 3.Usuwanie lub edytowanie zadan \n",
        " 4.Zapis bazy zadan pod zadana sciezke \n",
        " 5.Zamkniecie programu"
          )
    act = int(input())
    action(act, json_data)


def action(act, json_data):
    if act == 1:
        json_data = add_new_task(json_data)
        save(json_data)
        next_action(json_data)

    elif act == 2:
        print("Ile zadan ma zostac wypisane? By wypisac wszystkie napisz 0")
        task_amount = int(input())
        if task_amount < 0:
            print("*Nie mozna wypisac ujemnej liczby zadan*")
            action(2, json_data)
        else:
            # print_tasks(task_amount, json_data) TODO:BASIA
            next_action(json_data)

    elif act == 3:
        print("Wybierz kojena akcje: \n",
              "  1.Usuwanie zadania \n",
              "  2.Edytowanie zadania \n",
              "  3.Powrot")
        act_ = int(input())
        if act_ == 1:
            # json_data = delete_tasks(json_data) TODO:ANIA
            next_action(json_data)
        elif act_ == 2:
            # json_data = edit_tasks(json_data) TODO:ANIA
            next_action(json_data)
        elif act_ == 3:
            next_action(json_data)
        else:
            print("*Prosze podac liczbe od 1 do 3*")
            action(3, json_data)

    elif act == 4:
        print("Podaj sciezke pod ktora chcesz zapisac baze zadan")
        # TODO:MICHAL
        next_action(json_data)

    elif act == 5:
        save(json_data)
        exit()

    else:
        print("*Prosze podac liczbe od 1 do 3*")
        act = int(input())
        action(act, json_data)