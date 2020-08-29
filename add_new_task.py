#to jest pierwsza funkcjonalnosc
import string


def add_new_task (ListOfTasks):

    print("Give task name")
    name_ = input()          #najpierw uzytkownik wypisuje potrzebne do konstruktora atrybuty klasy task
    print("Give priority of you Task, 1 - 3 (most important)")
    importance_ = int(input())
    print("Give desciptrion")
    description_ = input()

    id_ = ListOfTasks[-1]["id"] + 1

    task = {"id": id_, "name": name_, "importance": importance_, "description": description_} #jedno zadanie jest słownikiem a nie klasą
    ListOfTasks.append(task)

    return ListOfTasks





