#funkcjinalnosc 5- usuwanie zadan
#To jest tylko zarys, pozniej jeszcze doczytam jak to z tym modulem json
#nie wiem czy w koncu mam to pisac tak jak dla slownika czy jak dla zwyklej listy

from Tasks import Tasks

def delete_tasks (ListOfTasks):
    print (ListOfTasks)
    print ("Type Task name to delete:")
    x = input ()
    #sprawdzic czy nazwa zadania znajduje sie w slowniku
    if x in ListOfTasks:
        del ListOfTasks[x]
    else: print("Error!")
    print ("Task has been deleted")
    print (ListOfTasks)