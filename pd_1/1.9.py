"""
Napisz funkcję, która sprawdzi czy podany napis jest palindromem
"""


def palindrom(a: str) -> bool:
    new = ""
    for i in a.lower():
        if i.isalnum():
            new += i
    if new == new[::-1]:
        return True
    else:
        return False


assert palindrom("Kobyła ma mały bok!") == True
assert palindrom("nie www") == False
