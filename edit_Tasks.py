#funkcjonalnosc 5- edytowanie zadan
#zmieniłam kod tak zeby mozna było zmienic wszystko i to juz powinno dzialac
from print_tasks import print_tasks


def edit_tasks(list_of_tasks):
    print("Type task id")
    n = int(input())
    d = 0
    for i in list_of_tasks:
        if i["id"] == n:
            name = list_of_tasks[d]["name"]
            importance = list_of_tasks[d]["importance"]
            description = list_of_tasks[d]["description"]
            print("Current name: %s",  list_of_tasks[d]["name"] )
            name = input("Type in new name")
            print("Current name : %s", list_of_tasks[d]["importance"])
            importance = input("Type in new importance")
            print("Current name : %s", list_of_tasks[d]["description"])
            description = input("Type in new description")
            list_of_tasks[d]["name"] = name
            list_of_tasks[d]["importance"] = importance
            list_of_tasks[d]["description"] = description
    d += 1

    print_tasks(list_of_tasks)
    return(list_of_tasks)
