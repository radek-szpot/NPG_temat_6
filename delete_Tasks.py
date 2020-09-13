"""
Module which allows user to delete tasks
"""

from print_tasks import print_tasks_not_sorted
from parse_input_for_int import parse_input_for_int


def delete_tasks(list_of_tasks):
    print_tasks_not_sorted(list_of_tasks, len(list_of_tasks))
    print("Podaj id zadania, które chcesz usunąć")
    n = parse_input_for_int(1, len(list_of_tasks))
    a = 0
    for i in list_of_tasks:
        if i["id"] == n:
            del (list_of_tasks[a])
        a += 1

    print("Zadanie o podanym id zostało usunięte")
    print_tasks_not_sorted(list_of_tasks, len(list_of_tasks))
    return list_of_tasks
