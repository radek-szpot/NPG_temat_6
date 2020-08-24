#druga funkcjonalność - print zadań

import string
from Task import Task

def print_tasks (ListOfTasks):
    print("Ile zadan ma zostac wypisane?")
    task_amount = int(input())
    for x in range(task_amount):
        print(x)
#trochę nie wiem jak zabrać się do odwoływania do listy zadań
#jeszcze dodać posortowanie
