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
from save_tasks_path import save_to_path
from parse_input_for_int import parse_input_for_int


class Program:
    def __init__(self):
        self.json_data = upload()

    def start(self):
        self.next_action()

    def next_action(self):
        print("\n", "Napisz liczbę od 1 do 5 by wybrać dana akcję: \n",
              " 1.Dodanie nowego zadania \n",
              " 2.Wypisanie zadań \n",
              " 3.Usuwanie lub edytowanie zadań \n",
              " 4.Zapis bazy zadań pod zadaną ścieżkę \n",
              " 5.Zamknięcie programu"
              )
        chosen_action = parse_input_for_int(1, 5)
        self.action(chosen_action)

    def action(self, chosen_action):
        # Add new task
        if chosen_action == 1:
            self.json_data = add_new_task(self.json_data)
            save(self.json_data)
            self.next_action()

        # Print tasks
        elif chosen_action == 2:
            print("Ile zadań ma zostać wypisane? By wypisać wszystkie napisz 0")
            task_amount = parse_input_for_int(0, None)
            # print_tasks(task_amount, self.json_data) TODO:BASIA
            self.next_action()

        # Edit/delete task
        elif chosen_action == 3:
            print("Wybierz kojena akcje: \n",
                  "  1.Usuwanie zadania \n",
                  "  2.Edytowanie zadania \n",
                  "  3.Powrót")
            chosen_option = parse_input_for_int(1, 3)
            if chosen_option == 1:
                # self.json_data = delete_tasks(self.json_data) TODO:ANIA
                save(self.json_data)
                self.next_action()
            elif chosen_option == 2:
                # self.json_data = edit_tasks(self.json_data) TODO:ANIA
                save(self.json_data)
                self.next_action()
            elif chosen_option == 3:
                self.next_action()

        # Save to path
        elif chosen_action == 4:
            print("Podaj ściezkę pod którą chcesz zapisać bazę zadań")
            path = str(input())
            print("Jak chcesz nazwać plik?")
            file_name = str(input())
            save_to_path(path, file_name, self.json_data)
            if True:
                print("Udało się zapisać!")
            self.next_action()

        # Save and exit
        elif chosen_action == 5:
            save(self.json_data)
            exit()
