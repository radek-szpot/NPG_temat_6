#funkcjonalnosc 5- edytowanie zadan
#nie działa do końca tak jakbym chciała ale to jeszcze do tego wroce
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