#to jest pierwsza funkcjonalnosc
import string
from Task import Task

def add_new_task (ListOfTasks):
    print("Podaj nazwe zadania")
    name = input()          #najpierw uzytkownik wypisuje potrzebne do konstruktora atrybuty klasy task
    print("Podaj priorytet tego zadania od 1 - 3")
    importance = int(input())
    print("Podaj opis zadania")
    description = input()

    task = Task(name, importance, description)

    if task.get #tutaj użyję gettera klasy task aby poznać jego ważnośc następnie w zależności od get będę dodawał do odpowiedniego stopnia ListOfTask
    ListOfTasks[0].append(task)


