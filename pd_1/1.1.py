# Napisz funkcję format_number, która przyjmie nieujemne liczby i zwróci napis, w którym liczba
# będzie sformatowana tak, by tysiące były rozdzielane przecinkiem

def format_number(a: int) -> str:
    if (a >= 0):
        return "{:,d}".format(a)
    else:
        print("podano liczbe ujemna")


a = int(input())
print(format_number(a))

assert "100,000" == format_number(100000)
assert "100,000,000,000,000,000,000,000" == format_number(100000000000000000000000)
