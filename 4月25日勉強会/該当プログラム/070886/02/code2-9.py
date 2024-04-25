class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'


import copy

pt_a = Point(10,12)
pt_b = copy.copy(pt_a)
pt_b.x = 20
print(pt_a)
print(pt_b)
print(id(pt_a))
print(id(pt_b))