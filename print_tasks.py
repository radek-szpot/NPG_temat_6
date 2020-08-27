'''
modul pozwalajacy wypisywac n zadan
'''
import string
from Task import Task

def print_tasks (ListOfTasks):
    print("Ile zadan ma zostac wypisane?")
    task_amount = int(input())
    print("Czy zadania mają wyświetlać się posortowane?\n"
          "Jeżeli tak, wpisz 1, jeżeli nie, wpisz 2.")
    sorting = int(input())
    if sorting == 1:
        with open('database.json') as f:
                raw_data = f.read()
                json_data = json.loads(raw_data)
        for i in range(task_amount):
            if i['importance'] == 1:
                colours.prGreen(i['name'])
                print(' -', i['description'])
            else:
                continue
        for i in range(task_amount):
            if i['importance'] == 2:
                colours.prYellow(i['name'])
                print(' -', i['description'])
            else:
                continue
        for i in range(task_amount):
            if i['importance'] == 3:
                colours.prRed(i['name'])
                print(' -', i['description'])
            else:
                continue
    if sorting == 2:
        with open('database.json') as f:
            raw_data = f.read()
            json_data = json.loads(raw_data)
        for i in range(task_amount):
            if i['importance'] == 1:
                colours.prGreen(i['name'])
                print(' -', i['description'])
            elif i['importance'] == 2:
                colours.prYellow(i['name'])
                print(' -', i['description'])
            elif i['importance'] == 3:
                colours.prRed(i['name'])
                print(' -', i['description'])
    else:
        print('Podałeś niepoprawną liczbę')
    return json_data
