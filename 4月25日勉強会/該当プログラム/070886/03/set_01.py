# 順序は保証されない
set_01 = {"A", "B", "C", "D", "E"}
# print(type(set_01))
print(set_01)


# 要素の重複は許されない
set_02 = {"A", "B", "B", "C", "D", "E"}
print(set_02)

# リストから重複を取り除く
birds = ["鳩", "雀", "オウム", "雀", "フクロウ", "オウム", "雀", "ペンギン"]
set_birds = set(birds)
lst_birds = list(set_birds)
print(lst_birds)

"""
オウムと雀が被っている。
しかし、順番が担保されない。
辞書、タプル、セットを相互変換できる。
"""
