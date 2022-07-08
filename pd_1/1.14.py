"""
Napisz funkcję, która przyjmie napis i zwróci mapowanie słów na ich częstotliwość wystąpienia w
tekście. Mapowanie powinno być zawarte w słowniku lub obiekcie do niego podobnym
Powinno to działać mniej więcej tak:
count_words("kobyła ma mały bok bok")
{'kobyła': 1, 'ma': 1, 'mały': 1, 'bok': 2}
Wielkość liter nie powinna mieć wpływu na wynik:
count_words("kobyła ma mały bok Bok")
{'kobyła': 1, 'ma': 1, 'mały': 1, 'bok': 2}
Nie powinny mieć też wpływu na to różne znaki interpunkcyjne, oraz znaki takie jak ’ i - umieszczone
poza słowami
count_words("kobyła, ma mały bok! Bok!")
{'kobyła': 1, 'ma': 1, 'mały': 1, 'bok': 2}
count_words("C'est la vie, -- c'est la vie! closed-door")
{"c'est": 2, "la": 2, "vie": 2, "closed-door": 1}

Mogą tu być przydatne wyrażenia regularne. Być może też w collections znajdziesz coś pomoc-
nego
"""


def count_words(a: str):
    count = {}
    a = a.lower()
    a = a.split(" ")
    for i in a:
        i = i.replace(".", "")
        i = i.replace(",", "")
        i = i.replace("--", "")
        i = i.replace("!", "")
        i = i.replace("?", "")
        if i == "":
            continue
        count.setdefault(i, 0)
        count[i] += 1
    print(count)
    return count


# a = input()
# count_words(a)

assert count_words("kobyła, ma mały bok! Bok!") == {'kobyła': 1, 'ma': 1, 'mały': 1, 'bok': 2}
assert count_words("C'est la vie, -- c'est la vie! closed-door") == {"c'est": 2, "la": 2, "vie": 2, "closed-door": 1}
