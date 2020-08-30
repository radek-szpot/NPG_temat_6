#funkcjinalnosc 5- usuwanie zadan

from print_tasks import print_tasks


def delete_tasks(list_of_tasks):
    print_tasks(list_of_tasks)
    print("Type task id in order to delete it")
    n = parse_input_fot_int(min, max)
    a = 0
    for i in list_of_tasks:
        if i["id"] == n:
            del (list_of_tasks[a])
        a += 1

    print("Task has been deleted")
    print_tasks(list_of_tasks)
    #Starałam sie to zmienic tak zeby sie odwolywalo do funkcji wypisujacej zadania, mam nadzieje ze jest ok..
    return (list_of_tasks)
