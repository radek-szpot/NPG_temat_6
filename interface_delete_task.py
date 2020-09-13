from tkinter import *
from save_tasks import save
import json

def delete_task(id, json_data):

    a = 0
    for dic in json_data:
        if dic["id"] == int(id):
            del (json_data[a])
        a += 1

    tidy_id = 0
    ordered_data = {}  # słownik klucz: id, wartość słownik z odpowiednim id
    # Ordering list of json data
    for json_dictionary in json_data:
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

    save(json_data)


