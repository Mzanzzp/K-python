"""
stwórz funkcję, która sprawdzi, czy dwa teksty są anagramami
assert is_anagram("typhoon", "opython") == True
assert is_anagram("Alice", "Bob") == False
"""


def angram(a: str, b: str) -> bool:
    count_a = {}
    count_b = {}
    for i in a:
        count_a.setdefault(i, 0)
        count_a[i] += 1
    for i in b:
        count_b.setdefault(i, 0)
        count_b[i] += 1
    if count_a == count_b:
        return True
    else:
        return False


# a = input()
# b = input()
# print(angram(a, b))
assert angram("typhoon", "opython") == True
assert angram("Alice", "Bob") == False
