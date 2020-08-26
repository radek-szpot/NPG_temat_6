#funkcjinalnosc 5- usuwanie zadan
#Jakby bylo cos zle albo kod inaczej powinnam byla napisac to niech mnie ktos powiadomi
#Pomogl mi brat i twierdzi ze to nie do konca tak powinno byc ale dziala

from Task import Task

def delete_tasks (ListOfTasks):

    print (ListOfTasks)
    print("Type task id in order to delete it")
    n = int(input())
    a = 0
    for i in ListOfTasks:
        if i["id"] == n:
            del (ListOfTasks[a])
        a += 1

    print ("Task has been deleted")
    print (ListOfTasks)