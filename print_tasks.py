'''
modul pozwalajacy wypisywac n zadan
'''
import string
from Task import Task

def print_tasks (ListOfTasks):
    print("Ile zadan ma zostac wypisane?")
    task_amount = int(input())
    for x in range(task_amount):
        print(x)
#trochę nie wiem jak zabrać się do odwoływania do listy zadań
    #Najlepiej zobacz sobie upload_tasks.py bo bardzo podobnie + popatrz do program.py co jest przekazywane do funkcji
#jeszcze dodać posortowanie
