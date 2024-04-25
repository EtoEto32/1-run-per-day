set_01 = {"鳩","雀","オウム","フクロウ","ペンギン"}
set_02 = {"鳩","雀","カラス","フラミンゴ","ペンギン"}

print(f"和集合 {set_01.union(set_02)}")

print(f"差集合 {set_01.difference(set_02)}")

print(f"積集合 {set_01.intersection(set_02)}")

print(f"排他的論理和 {set_01.symmetric_difference(set_02)}")

"""
setは順番が担保されない。


"""