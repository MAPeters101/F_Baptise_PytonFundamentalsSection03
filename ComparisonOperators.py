a = 10
b = 10
c = 10.0

print(a == b)
print(a == c)
print(a is b)
print(a is c)
print('='*40)
a = 10
b = 10.0

print(a == b)
print(a is b)
print(id(a), id(b))

print(10 != 12)
print(10.5 != 10.5)

print(10 >= 5)
print(10.5 < 100)

a = 1 + 1j
b = 1 + 1j
c = 2 + 2j

print(a == b)
print(a is b, id(a), id(b))  # Was False for him == different locations
#print(a < c)

print(0.1*3 == 0.3)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False


v1 = Vector(1, 1)
v2 = Vector(1, 1)
v3 = Vector(2, 3)
print(id(v1), id(v2), id(v3))
print(v1 is v2)
print(v1 == v2)  # False by default, python uses identity comparison for custom objects


