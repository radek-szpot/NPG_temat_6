from tkinter import *
from save_tasks import save
import json


def interface_print_tasks(json_data, root):
    json_data_text =''
    for dict in json_data:
        json_data_text = json_data_text + str(dict) + "\n"
    Printed_tasks_label = Label(root, text=json_data_text)
    Printed_tasks_label.grid(row=5, column=0, columnspan=2)
