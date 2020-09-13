"""
Module which allows user to add new tasks
"""

from parse_input_for_int import parse_input_for_int
from order_id import order_id

def add_new_task(list_of_tasks):
    list_of_tasks = order_id(list_of_tasks) #uporzadkowuje id aby bylo poprawne
    print("Podaj nazwę zadania")
    name_ = input()  # najpierw uzytkownik wypisuje potrzebne do konstruktora atrybuty klasy task
    print("Nadaj priorytet zadaniu: \n",
          "  1.Mało ważne zadanie \n",
          "  2.Ważne zadanie \n",
          "  3.Bardzo ważne zadanie")
    importance_ = parse_input_for_int(1, 3)
    print("Podaj opis")
    description_ = input()

    id_ = list_of_tasks[-1]["id"] + 1

    task = {"id": id_, "name": name_, "importance": importance_,
            "description": description_}  # jedno zadanie jest słownikiem a nie klasą
    list_of_tasks.append(task)

    return list_of_tasks