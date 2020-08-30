'''
modul pozwalajacy wypisywac zadania (opcjonalnie posortowane)
'''
from parse_input_for_int import parse_input_for_int
import colours

def print_tasks(json_data):
    print("Czy wyświetlić zadania posortowane?\n",
    "0. Nie\n",
    "1. Tak")
    whether_sort = parse_input_for_int(0, 1)
    print_tasks_optionally_sorted(json_data, whether_sort)
    
def print_tasks_optionally_sorted(json_data, whether_sort):
    #Print sorted
    if whether_sort == 1:
        print("Jak chcesz posortować zadania?\n",
              "1. Według daty dodania\n",
              "2. Według priorytetu")
        sorting_type = parse_input_for_int(1, 2)
        #Sorting chronologicaly
        if sorting == 1:
            ordered_data = {}
            for i in json_data:
                ordered_data[i['id']] = i
            ordered_data_sorted = sorted(ordered_data)
            sorted_list = [ordered_data[i] for i in ordered_data_sorted]
            for i in sorted_list:
                print(i['name'], end='')
                print(' -', i['description'])
            print("\n", "Żeby powrócić do panelu sterowania wciśnij enter")
            input()
        
        #Sorting by priority
        elif sorting_type == 2:
            for i in json_data:
                if i['importance'] == 1:
                    colours.prGreen(i['name'])
                    print(' -', i['description'])
                else:
                    continue
            for i in json_data:
                if i['importance'] == 2:
                    colours.prYellow(i['name'])
                    print(' -', i['description'])
                else:
                    continue
            for i in json_data:
                if i['importance'] == 3:
                    colours.prRed(i['name'])
                    print(' -', i['description'])
            print("\n", "Żeby powrócić do panelu sterowania wciśnij enter")
            input()

    #Simply print
    print('Ile zadań chcesz wypisać? Jeżeli chcesz wypisać wszystkie napisz "0"')
        task_amount = parse_input_for_int(0, len(json_data))
        if task_amount == 0:
            task_amount = len(json_data)
        break_when_n = 1
        for i in json_data:
            if i['importance'] == 1:
                colours.prGreen(i['name'])
                print(' -', i['description'])
                if break_when_n == task_amount:
                    print("\n", "Żeby powrócić do panelu sterowania wciśnij enter")
                    input()
                    return
                break_when_n += 1
            elif i['importance'] == 2:
                colours.prYellow(i['name'])
                print(' -', i['description'])
                if break_when_n == task_amount:
                    print("\n", "Żeby powrócić do panelu sterowania wciśnij enter")
                    input()
                    return
                break_when_n += 1
            elif i['importance'] == 3:
                colours.prRed(i['name'])
                print(' -', i['description'])
                if break_when_n == task_amount:
                    print("\n", "Żeby powrócić do panelu sterowania wciśnij enter")
                    input()
                    return
                break_when_n += 1
        print("\n", "Żeby powrócić do panelu sterowania wciśnij enter")
        input()
    return
