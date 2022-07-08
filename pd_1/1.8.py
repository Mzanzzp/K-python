"""
Napisz funkcję, która:
1. Jeśli jej argument będzie listą, tuplą bądź zbiorem, zwróci sumę jej elementów
2. Jeśli jej argument będzie słownikiem, zwróci sumę wartości
W obu przypadkach ignoruj napisy - o ile napisy nie reprezentują liczb
"""


def suma(a):
    h = 0
    if type(a) == dict:
        for v in a.values():
            h += int(v)
        return h
    elif type(a) == list or tuple or set:
        for i in a:
            h += int(i)
            print(h)
        return h
    else:
        print("zly typ danych")


a = [1, 2, 4]
b = {"hej": 4, "w": 8}
suma(a)
