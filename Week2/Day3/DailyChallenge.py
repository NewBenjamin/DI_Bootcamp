import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius: {self.radius}, area: {self.area():.2f}"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius
    
c1 = Circle(5)
c2 = Circle(10)
c3 = Circle(3)

print(c1)
print(c2)

print(c1 + c2)
print(c1 > c2)
print(c1 == c3)

circles = [c1, c2, c3]
print(sorted(circles))
