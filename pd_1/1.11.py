"""
Napisz funkcję, która sprawdzi, czy napis jest pangramem.
"""


def panagram(a: str) -> bool:
    alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
    h = 0
    for i in alfabet:
        if i in a.lower():
            h += 1
            if h == 32: return True
    return False


assert panagram("Pchnąć w tę łódź jeża lub ośm skrzyń fig") == True
assert panagram("abc") == False
