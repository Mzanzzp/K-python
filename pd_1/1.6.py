"""
Napisz funkcję spłaszczającą zagnieżdzone listy:
assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
assert flatten([[1, 2], [3, 4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]
"""


# def flatten(a: list) -> list:
#     return sum(a, [])
# dziala nie dokonca


def flatten(a: list) -> list:
    new = []
    for i in a:
        for j in i:
            new.append(j)
    return new


# dziala nie dokonca

g = [[1, 2], [3, 4, [5, 6]]]
print(flatten(g))
