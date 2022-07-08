"""
Napisz dekorator, który będzie printował w konsoli czas wykonania dekorowanej funkcji.
Możesz skorzystać z moduły time do mierzenia czasu.
"""
from time import time

def dekorator(funkcja):

    def czas(*a, **b):  #*args, **kwargs
        start = time()
        x = funkcja(*a, **b)
        koniec = time()
        print(f"{funkcja.__name__} zostaław wykonana w {(koniec - start):.5f} sekund")
        return x
    return czas


@dekorator
def napis():
    print("napis")

@dekorator
def doskonala(a: int) ->bool:
    dzielniki = 0
    for i in range(a):
        if i == 0:
            continue
        if a%i==0:
            dzielniki += i
    if dzielniki == a: return True
    else: return False

@dekorator
def dlugo():
    print(10000000000000000000000000000000000000**10000)
napis()
print(doskonala(6))
print(doskonala(555))
dlugo()



