#funkcjinalnosc 5- usuwanie zadan
#To jest tylko zarys, pozniej jeszcze doczytam jak to z tym modulem json

from Tasks import Tasks

def delete_tasks (ListOfTasks):
    print (ListOfTasks)
    print ("Type Task number to delete:")
    x = int (input ())
    del ListOfTasks[x]
    print ("Task has been deleted")
    print (ListOfTasks)