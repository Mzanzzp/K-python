"""
Napisz funkcję, która zwróci z napisu środkowy znak lub pusty napis, jeśli nie ma środkowego
znaku:
assert "b" == mid("abc")
assert "" == mid("abbc")
"""


def mid(a: str):
    if len(a) % 2 == 0:
        return ""
    else:
        b = len(a) // 2
        return a[(len(a) - b) - 1]


# a = str(input())
# print(mid(a))

assert "b" == mid("abc")
assert "" == mid("abbc")
