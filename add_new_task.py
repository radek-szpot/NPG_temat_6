# to jest pierwsza funkcjonalnosc
import string
from parse_input_for_int import parse_input_for_int


def add_new_task(json_data):
    print("Podaj nazwę zadania")
    name_ = input()  # najpierw uzytkownik wypisuje potrzebne do konstruktora atrybuty klasy task
    print("Nadaj priorytet zadaniu: \n",
          "  1.Mało ważne zadanie \n",
          "  2.Ważne zadanie \n",
          "  3.Bardzo ważne zadanie")
    importance_ = parse_input_for_int(1, 3)
    print("Give desciptrion")
    description_ = input()

    tidy_id = 0
    ordered_data = {}
    # Ordering list of json data
    for json_dictionary in json_data:
        json_dictionary_id_ = json_dictionary['id']
        ordered_data[json_dictionary_id_] = json_dictionary
    ordered_data_sorted = sorted(ordered_data)
    sorted_list = [ordered_data[i] for i in ordered_data_sorted]

    # Prescribing id
    for json_dictionary in sorted_list:
        sorted_list[tidy_id]["id"] = tidy_id + 1
        tidy_id += 1

    json_data = sorted_list
    id_ = json_data[-1]["id"] + 1

    task = {"id": id_, "name": name_, "importance": importance_,
            "description": description_}  # jedno zadanie jest słownikiem a nie klasą
    json_data.append(task)

    return json_data