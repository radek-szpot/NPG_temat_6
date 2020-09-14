from tkinter import *
from upload_tasks import upload
import json
from save_tasks import save

def open_window_task(list_of_tasks):
    window_task_root = Tk()
    window_task_root.title("dodaj zadanie")
    window_task_root.geometry("300x300")

    #creating entry box

    name = Entry(window_task_root, width=30)
    name.grid(row=0, column=1)
    description = Entry(window_task_root, width=30)
    description.grid(row=1, column=1)
    importance = Entry(window_task_root, width=30)
    importance.grid(row=2, column=1)

    #creating labels
    name_label = Label(window_task_root, text="name")
    name_label.grid(row=0, column=0, pady=30)
    description_label = Label(window_task_root, text="description")
    description_label.grid(row=1, column=0, pady=30)
    importance_label = Label(window_task_root, text="importance")
    importance_label.grid(row=2, column=0, pady=30)

    confirm_button = Button(window_task_root, text="confirm", command=lambda : add_new_task_interface(list_of_tasks,
                                                                                            name.get(),
                                                                                            description.get(),
                                                                                            importance.get()))
    confirm_button.grid(row=3, column=0, columnspan=2)




def add_new_task_interface(list_of_tasks, name, description, importance):

    tidy_id = 0
    ordered_data = {}  # słownik klucz: id, wartość słownik z odpowiednim id
    # Ordering list of json data
    for json_dictionary in list_of_tasks:
        json_dictionary_id_ = json_dictionary['id']
        ordered_data[
            json_dictionary_id_] = json_dictionary  # stworzenie słownika za pomocą pętli, id cały czas mogą być nieposortowane
    ordered_data_sorted = sorted(ordered_data)  # id stają się posortowane,
    sorted_list = [ordered_data[id] for id in
                   ordered_data_sorted]  # wykorzystanie list comprehension i uzyskanie listy posortowanych słowników wzlędem wcześniej posortowanych id_

    # Prescribing id
    for json_dictionary in sorted_list:
        sorted_list[tidy_id][
            "id"] = tidy_id + 1  # musimy przepisać id w celu uniknięcia błedu braku jednego id_ np: 1 2 3 5 6 7
        tidy_id += 1


    id_ = list_of_tasks[-1]["id"] + 1

    task = {"id": id_, "name": name, "description": description, "importance": int(importance)}
    list_of_tasks.append(task)

    with open('database.json', mode="w") as f:
        f.write(json.dumps(list_of_tasks))

    with open('database.json') as f:
        raw_data = json.load(f)
    with open('database.json', mode="w") as f:
        json.dump(raw_data, f, indent=4)


