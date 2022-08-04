"""
Okrąg powinien mieć promień (radius), średnicę (diameter) i pole powierzchni (area) oraz przy-
jemną reprezentację napisową
"""
import math


class Circle:

    def __init__(self, radius=1):
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value < 0: raise ValueError("liczba ujemna")
        self.__radius = value

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @property
    def area(self):
        return self.radius ** 2 * math.pi

    @area.setter
    def area(self, value):
        self.radius = math.pi * value ** 0.5

    def __str__(self):
        return f"Circle\n======\nradius: \t{self.radius}\ndiameter: \t{self.diameter}\narea: \t{self.area}"

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return False

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.radius >= other.radius
        return False

    def __add__(self, other):
        return Circle(self.area + other.area)

class Square:
    def __init__(self, side=1):
        self.side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        if value < 0: raise ValueError("liczba ujemna")
        self.__side = value

    @property
    def area(self):
        return self.side ** 2

    @area.setter
    def area(self, value):
        self.radius = value ** 0.5


a = Circle(1)
b = Circle()
assert (a == b) == True
assert (a > b) == False
assert (a >= b) == True

# a = Circle()
# b = Circle(5)
# g = a + b
# print(g)
# print(g.area)
