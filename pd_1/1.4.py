"""
double letters
Stwórz funkcję, która sprawdzi, czy w zadanym tekście dwa identyczne znaki sąsiadują ze sobą
assert double_letters("ala") == False
assert double_letters("Hello") == True
assert double_letters("abc") == False
assert double_letters("nono") == False
"""


def double_letters(a: str) -> bool:
    poprzedni = ""
    for i in a:
        if i == poprzedni:
            return True
        poprzedni = i
    return False


assert double_letters("ala") == False
assert double_letters("Hello") == True
assert double_letters("abc") == False
assert double_letters("nono") == False
