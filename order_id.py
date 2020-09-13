"""
Module which orders id in list of tasks
"""


def order_id(list_of_tasks):
    tidy_id = 0  # variable needed to prescript new id
    ordered_data = {}  # dictionary which will include key: id, value:  id dictionary with same id

    # Ordering list of list_of_tasks
    # this step is in case id's were not chronological in the first place
    for json_dictionary in list_of_tasks:
        json_dictionary_id_ = json_dictionary['id']
        ordered_data[
            json_dictionary_id_] = json_dictionary  # creating dictionary with: keys -> id's and values -> dictionaries with same id
    ordered_data_sorted = sorted(ordered_data)  # creating list of sorted id (only id's)
    sorted_list = [ordered_data[id] for id in
                   ordered_data_sorted]  # usage of list comprehension to create list of sorted dictionaries with sorted id's

    # Prescribing id
    # this step is so that there will be no hole in id (e.g. 1 2 3 5 6 7)
    for json_dictionary in sorted_list:
        sorted_list[tidy_id][
            "id"] = tidy_id + 1
        tidy_id += 1

    return sorted_list
