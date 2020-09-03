"""
Module which allows user to edit tasks
"""

from print_tasks import print_tasks_not_sorted

from parse_input_for_int import parse_input_for_int


def edit_tasks(list_of_tasks):
    print_tasks_not_sorted(list_of_tasks, len(list_of_tasks))
    print("Podaj numer zadania, które chcesz edytować")
    user_edit_choice = parse_input_for_int(1, len(list_of_tasks))

    print("Podaj nową nazwę zadania:")
    list_of_tasks[user_edit_choice - 1]["name"] = input()
    print("Podaj nowy opis zadania:")
    list_of_tasks[user_edit_choice - 1]["description"] = input()
    print("Podaj nowy priorytet zadania (liczba 1, 2 lub 3):")
    list_of_tasks[user_edit_choice - 1]["importance"] = parse_input_for_int(1, 3)

    print_tasks_not_sorted(list_of_tasks, len(list_of_tasks))
    return list_of_tasks
