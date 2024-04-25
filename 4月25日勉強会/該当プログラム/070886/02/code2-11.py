class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'


import copy

pt_a = Point(10,12)
pt_b = Point(20,24)
lst_a = [pt_a,pt_b]
lst_b = copy.deepcopy(lst_a)

print(f"lst_aのオブジェクトIDは{id(lst_a)}")
print(f"lst_bのオブジェクトIDは{id(lst_b)}")

for pt in lst_a:
    print(f"lst_a内のPointクラスのオブジェクトのIDは{id(pt)}")

for pt in lst_b:
    print(f"lst_b内のPointクラスのオブジェクトのIDは{id(pt)}")