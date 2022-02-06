print('Реализовать следуюшие классы и продемострировать их работоспособность: area & perimeter должны быть акссесорами (@property)')
from abc import ABC, abstractmethod
from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
p1=Point(1,2)
p2=Point(3,4)

print(f'Point 1: {p1.x},{p1.y}')
print(f'Point 2: {p2.x},{p2.y}')

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1 or Point()
        self.p2 = p2 or Point()

    def length(self):
        return round(sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2), 2)

ln1=Line(p1,p2)
ln2=Line(p2,p1)
print(f'Line 1: {ln1.length()}')
print(f'Line 2: {ln2.length()}')

class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape, Line):
    @property
    def area(self):
        return round(self.length() ** 2, 2)

    @property
    def perimeter(self):
        return round(4 * self.length(), 2)

sqr=Square(p1,p2)
print(f'Square perimeter: {sqr.perimeter}')
print(f'Square area: {sqr.area}')

class Rect(Shape):
    def __init__(self, r1, r2):
        self.r1 = r1 or Line()
        self.r2 = r2 or Line()
    @property
    def area(self):
        return round(self.r1.length() * self.r2.length(), 2)

    @property
    def perimeter(self):
        return round((self.r1.length() + self.r2.length()) * 2, 2)

rct=Rect(ln1,ln2)
print(f'Rect perimeter:{rct.perimeter}')
print(f'Rect area:{rct.area}')

class Cube(Square):
    def volume(self):
        return round(self.length() ** 3, 2)
cb=Cube(p1,p2)
print(f'Cube Volume: {cb.volume()}')

print("Bye")
input("жмякни Интер для выхода")