from tkinter import *
from interface_add_new_task import open_window_task
from interface_delete_task import *
from upload_tasks import upload
from interface_delete_task import delete_task
from interface_print_task import interface_print_tasks
from save_tasks_path import save_to_path
from interface_mode_tasks import edit_task, open_window_task_to_edit
from tkinter import filedialog, Text
import os

root = Tk()
root.title('lista mailingowa')
root.geometry("550x700")

json_data_1 = upload()

Question_Label = Label(root, text="Co chciałbyś zrobić?")
Question_Label.grid(row=0, column=0, padx=140, pady=10, columnspan=2)

Add_new_task_1_button = Button(root, text="Dodaj nowe zadanie", command=lambda: open_window_task(json_data_1))
Add_new_task_1_button.grid(row=1, column=0, padx=140, pady=10, columnspan=2)

Delete_task_Label = Label(root, text="Które zadanie usunąć?")
Delete_task_Label.grid(row=2,column=0, pady=10)
Delete_task_entry = Entry(root, width=30)
Delete_task_entry.insert(0, "2")
Delete_task_entry.grid(row=2, column=1, pady=10)



Print_task_button = Button(root, text="Wydrukuj zadania", command=lambda: interface_print_tasks(json_data_1, root))
Print_task_button.grid(row=4, column=0, padx=140, pady=10, columnspan=2)

delete_task_button = Button(root, text="Usuń zadanie", command=lambda: delete_task(int(Delete_task_entry.get()), json_data_1))
delete_task_button.grid(row=3, column=0, padx=140, pady=10, columnspan=2)


path = Entry(root, width=50)
path.insert(0, "Podaj ścieżkę")
path.grid(row=7, column=0, padx=140, pady=10, columnspan=2)

filename = Entry(root, width=50)
filename.insert(0, "Podaj nazwę pliku")
filename.grid(row=8, column=0, padx=140, pady=10, columnspan=2)

save_to_path_button = Button(root, text="Zapisz zadanie pod zadaną ścieżkę", command=lambda: save_to_path(path.get(), filename.get(), json_data_1))
save_to_path_button.grid(row=6, column=0, padx=140, pady=10, columnspan=2)

save_button = Button(root, text="Zapisz zadanie", command=lambda: save(json_data_1))
save_button.grid(row=9, column=0, padx=140, pady=10, columnspan=2)


mode_entry = Entry(root, width=50)
mode_entry.insert(0, "Podaj id do zmodyfikowania")
mode_entry.grid(row=11, column=0, padx=140, pady=10, columnspan=2)

mode_button = Button(root, text="zmodyfikuj zadanie", command=lambda: open_window_task_to_edit(json_data_1, int(mode_entry.get())))
mode_button.grid(row=10, column=0, padx=140, pady=10, columnspan=2)


root.mainloop()