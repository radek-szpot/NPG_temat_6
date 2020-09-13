from tkinter import *
import json
from save_tasks import save

def open_window_task_to_edit(json_data, id):
    window_task_root_for_edit = Tk()
    window_task_root_for_edit.title("edytuj zadanie")
    window_task_root_for_edit.geometry("300x300")

    #creating entry box

    name = Entry(window_task_root_for_edit, width=30)
    name.grid(row=0, column=1)
    description = Entry(window_task_root_for_edit, width=30)
    description.grid(row=1, column=1)
    importance = Entry(window_task_root_for_edit, width=30)
    importance.grid(row=2, column=1)

    #creating labels
    name_label = Label(window_task_root_for_edit, text="name")
    name_label.grid(row=0, column=0, pady=30)
    description_label = Label(window_task_root_for_edit, text="description")
    description_label.grid(row=1, column=0, pady=30)
    importance_label = Label(window_task_root_for_edit, text="importance")
    importance_label.grid(row=2, column=0, pady=30)

    confirm_button = Button(window_task_root_for_edit, text="confirm", command=lambda : edit_task(json_data,
                                                                                            name.get(),
                                                                                            description.get(),
                                                                                            importance.get(),
                                                                                            id))
    confirm_button.grid(row=3, column=0, columnspan=2)

def edit_task(json_data, name, description, importance, id):
    for dict in json_data:
        if dict["id"] == id:
            dict["name"] = name
            dict["description"] = description
            dict["importance"] = importance

    save(json_data)