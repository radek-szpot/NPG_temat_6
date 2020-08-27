#funkcjinalnosc 5- usuwanie zadan
#Jakby bylo cos zle albo kod inaczej powinnam byla napisac to niech mnie ktos powiadomi

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


#Znalazlam w necie jeszcze takie rozwiazanie tego zadania
#Nie wiem czy tylko to jest poprawne jesli chodzi o prace z json ale zostawie oba rozwiazania w razie czego
#Chodzi tu o to, ze iteruje sie po wszystkich elementach listy ListOfTasks i dany element jest pomijany w nowo stworzonej liście, tak jakby zostal usuniety
#Usuwanie jest zadanie o danym indeksie na liscie, narazie nie wiem jak sie odwolywac do id zadania

def delete_tasks ():
    view_data ()
    new_data = []
    with open (filename, "r") as f:
        tasks = json.load(f)
        data_length = len(tasks) - 1
    print ("Type id number in order to delete task")
    delete_option = input(f"Select a number 0-(data_length)")
    i = 0
    for entry in tasks:
        if i == int(delete_option):
            pass
            i= i+1
        else:
            new_data.append(entry)
            i= i+1
    with open (filename, "w") as f:
        json.dump(new_data, f)