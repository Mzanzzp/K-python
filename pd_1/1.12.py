"""
Napisz funkcję, które sprawdzi, czy zadana liczba jest doskonała
(czy jest równa sumie wszystkich swoich dzielników różnych od tej liczby: np. 6 = 1 + 2 + 3)
"""


def doskonala(a: int) -> bool:
    dzielniki = 0
    for i in range(a):
        if i == 0:
            continue
        if a % i == 0:
            dzielniki += i
    if dzielniki == a:
        return True
    else:
        return False


assert doskonala(6) == True
assert doskonala(42) == False
assert doskonala(28) == True
