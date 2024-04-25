# pt = (10,20)
# print(pt[0])
# print(pt[1])


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# pt = Point(10,12)　インスタンス作成時に引数も渡す
# print(pt.x)
# print(pt.y)

"""
いちいちクラスを作るのは面倒である。
"""

import collections

Point = collections.namedtuple("Point", "x y")
# 第一引数：タプル自体の名前　第二引数：参照

p1 = Point(10, 20)
print(p1)
print(p1.x)
print(p1.y)

p1 = p1._replace(x=100)
# 新しいタプルを生成したわけではない。
# 別のタプルをメモリ上に置いているだけである。
print(p1)

"""
タプルの要素に名前を付けることが
できたら便利じゃないか
定義した時から値が変らない
"""
