"""
Module which allows user to print tasks
"""
from parse_input_for_int import parse_input_for_int
import colours


def print_tasks(list_of_tasks):
    print("Czy wyświetlić zadania posortowane?\n",
          "0. Nie\n",
          "1. Tak")
    whether_sort = parse_input_for_int(0, 1)
    if whether_sort == 0:
        print('Ile zadań chcesz wypisać? Jeżeli chcesz wypisać wszystkie napisz "0"')
        task_amount = parse_input_for_int(0, len(list_of_tasks))
        if task_amount == 0:
            task_amount = len(list_of_tasks)
        print_tasks_not_sorted(list_of_tasks, task_amount)
    elif whether_sort == 1:
        print_tasks_sorted(list_of_tasks)


def print_tasks_sorted(list_of_tasks):
    # Print sorted
    print("Jak chcesz posortować zadania?\n",
          "1. Według daty dodania\n",
          "2. Według priorytetu")
    sorting_type = parse_input_for_int(1, 2)

    # Sorting chronologicaly
    if sorting_type == 1:
        ordered_data = {}
        for i in list_of_tasks:
            ordered_data[i['id']] = i
        ordered_data_sorted = sorted(ordered_data)
        sorted_list = [ordered_data[i] for i in ordered_data_sorted]
        for i in sorted_list:
            print(i['name'], end='')
            print(' -', i['description'])
        print("\n", "Żeby kontynuować wciśnij enter")
        input()

    # Sorting by priority
    elif sorting_type == 2:
        for i in list_of_tasks:
            if i['importance'] == 1:
                colours.prGreen(i['name'])
                print(' -', i['description'])
            else:
                continue
        for i in list_of_tasks:
            if i['importance'] == 2:
                colours.prYellow(i['name'])
                print(' -', i['description'])
            else:
                continue
        for i in list_of_tasks:
            if i['importance'] == 3:
                colours.prRed(i['name'])
                print(' -', i['description'])
        print("\n", "Żeby kontynuować wciśnij enter")
        input()
        return


def print_tasks_not_sorted(list_of_tasks, task_amount):
    break_when_n = 1
    for i in list_of_tasks:
        if i['importance'] == 1:
            print(i['id'], ".", end='')
            colours.prGreen(i['name'])
            print(' -', i['description'])
            if break_when_n == task_amount:
                print("\n", "Żeby kontynuować wciśnij enter")
                input()
                return
            break_when_n += 1
        elif i['importance'] == 2:
            print(i['id'], ".", end='')
            colours.prYellow(i['name'])
            print(' -', i['description'])
            if break_when_n == task_amount:
                print("\n", "Żeby kontynuować wciśnij enter")
                input()
                return
            break_when_n += 1
        elif i['importance'] == 3:
            print(i['id'], ".", end='')
            colours.prRed(i['name'])
            print(' -', i['description'])
            if break_when_n == task_amount:
                print("\n", "Żeby kontynuować wciśnij enter")
                input()
                return
            break_when_n += 1
    print("\n", "Żeby kontynuować wciśnij enter")
    input()
    return
