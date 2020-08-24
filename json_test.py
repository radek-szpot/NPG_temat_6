#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Esencja naszego przyszlego programu
'''
import json

#przykładowa funckcja dodająca zadanie
def add_task(id, name, desc):
    return {'id': id, 'nazwa': name, 'opis': desc}


lista_todos = []    #lista zadań dodająca słowniki(za pomocą funkcji dodajacej zadania) jako kolejne elementy
#przykładowe zadania
lista_todos.append(add_task(1, 'nazwa1', 'opis1'))
lista_todos.append(add_task(99, 'nazwa2', 'opis2'))
lista_todos.append(add_task(3, 'nazwa3', 'opis3'))
lista_todos.append(add_task(4, 'nazwa4', 'opis4'))


#zastosowanie json'a
#'myfile.json' to plik do którego zapisujemy/ odczytujemy
#mode w/r (write/read) czyli decydujemy czy zapisujemy czy czytamy

with open('myfile.json', mode="w") as f:
    f.write(json.dumps(lista_todos))
#polecam otworzyć 'myfile.json' aby zobaczyć jak to się zapisuje


with open('myfile.json') as f:
    raw_data = f.read() #raw data jest zamienione na zawartość pliku .json jako string
    print(raw_data + "\n")
json_data = json.loads(raw_data)
print(json_data[1]) #to jest lista
print(raw_data[:3]) #to jest string
print("\n")


#dodanie id jako słownika tak żeby można się bylo odwolywac do zadan po to aby je edytowac usuwac itd
ordered_data = {}
for iterat in json_data:
    ordered_data[iterat['id']] = iterat

print(ordered_data[99])
print(ordered_data)