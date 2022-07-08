"""
Napisz funkcję (lub funkcje), która zwróci maksymalną spośród 3 liczb. W rozwiązaniu skorzystaj
tylko z możliwośći definiowania funkcji i używania w nich operatorów porównania
"""


def max_of_three(a: int, b: int, c: int) -> int:
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c


assert max_of_three(3, 5, 1) == 5
assert max_of_three(1, 3, 99) == 99
assert max_of_three(3563456, 2352, 436) == 3563456
