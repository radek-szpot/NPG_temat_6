"""
Module which allows user to edit tasks
"""

from print_tasks import print_tasks_not_sorted


def edit_tasks(list_of_tasks):
    print_tasks_not_sorted(list_of_tasks, len(list_of_tasks))
    print("Type task id in order to edit it")
    n = int(input())
    d = 0
    for i in list_of_tasks:
        if i["id"] == n:
            # a - name
            # b - importance
            # c - descripton
            a = list_of_tasks[d]["name"]
            b = list_of_tasks[d]["importance"]
            c = list_of_tasks[d]["description"]
            print("Current data: \nname: %s, \nimportance: %s, \ndescription: %s",
                  list_of_tasks[d]["name"], list_of_tasks[d]["importance"], list_of_tasks[d]["description"])
            # Nie wiem czy to juz nie jest troche za duzo kombinowania ale tak chyba lepiej wygladac
            a = input("Type in new name")
            b = input("Type in new importance")
            c = input("Type in new description")
            list_of_tasks[d]["name"] = a
            list_of_tasks[d]["importance"] = b
            list_of_tasks[d]["description"] = c
            print("Data has been changed for task id: %d", n)
    d += 1

    print_tasks_not_sorted(list_of_tasks, len(list_of_tasks))
    return list_of_tasks
