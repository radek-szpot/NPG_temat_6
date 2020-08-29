import tkinter as tk
from program import start
from add_new_task import add_new_task
from functools import partial
from upload_tasks import upload
from tkinter import filedialog, Text
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

AddNewTask = tk.Button(root, text="Start", padx=10, pady=5, fg="white", bg="#263D42", command=partial(add_new_task, upload()))
AddNewTask.pack()

root.mainloop()