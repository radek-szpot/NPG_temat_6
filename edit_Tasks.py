#funkcjonalnosc 5- edytowanie zadan
#zmienia sie tylko jedna cecha w jednym zadaniu narazie

from Tasks import Tasks

def edit_tasks (ListOfTasks):

    print("Type task id")
    n = int(input())
    d = 0
    for i in ListOfTasks:
        if i["id"] == n:
            print("Type name, describtion or priority that you want to change")
            x = input()
            if x == "name":
                a = input()
                ListOfTasks[d]["name"] = a
            elif x == "describtion":
                b = input()
                ListOfTasks[d]["describtion"] = b
            elif x == "importance":
                c = input()
                ListOfTasks[d]["importance"] = c
        d += 1

    print(ListOfTasks)


#Podobnie jak w poprzednim pliku delete_Tasks.py tez znalazlam inne rozwiazanie i tez zostawie oba rozwiazania narazie
#Działa na podobnej zasadzie co ten program z usuwaniem tylko zastepuje poprzednie informacje nowymi

def edit_tasks ():
    view_data ()
    new_data = []
    with open (filename, "r") as f:
        tasks = json.load(f)
        data_length = len(tasks) - 1
    print ("Type id number in order to delete task")
    edit_option = input(f"Select a number 0-(data_length)")
    i = 0
    for entry in tasks:
        if i == int(edit_option):
            name = entry["name"]
            importance = entry["importance"]
            description = entry["decsription"]
            print("Current name : {name}")
            name = input("Type in new name")
            print("Current name : {importance}")
            importance = input("Type in new importance")
            print("Current name : {description}")
            description = input("Type in new description")
            new_data.append({"name" : name, "importance" : importance, "description" : description})
            i = i+1
        else:
            new_data.append(entry)
            i= i+1
    with open (filename, "w") as f:
        json.dump(new_data, f)