#to jest pierwsza funkcjonalnosc
import string


def add_new_task (ListOfTasks):

    print("Give task name")
    name_ = input()          #najpierw uzytkownik wypisuje potrzebne do konstruktora atrybuty klasy task
    print("Give priority of you Task, 1 - 3 (most important)")
    importance_ = int(input())
    print("Give desciptrion")
    description_ = input()
    print("Give id")
    id_ = input()

    task = {'id': id_, 'name' : name_, 'importance' : importance_, "description" : description_} #jedno zadanie jest słownikiem a nie klasą

    if task['importance'] == 3:
        ListOfTasks[2].append(task)
    elif task['importance'] == 2:
        ListOfTasks[1].append(task)
    elif task['importance'] == 1:
        ListOfTasks[1].append(task)
    else:
        print("Wrong priority number")





