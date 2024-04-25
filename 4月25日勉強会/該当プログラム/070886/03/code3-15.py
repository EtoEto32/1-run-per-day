from collections import Counter

group1 = ["鳩","雀","オウム","フクロウ","ペンギン","鳩","オウム","雀"
          ,"カモメ","カラス","雀","鳩"] #12

group2 = ["鳩","雀","オウム","フクロウ","ペンギン","キジ","カモメ"
          ,"雀", "カラス", "鳩", "カラス", "雀", "カラス"] #13

c1 = Counter(group1)
c2 = Counter(group2)

print(c1["鳩"])
print(sum(c1.values()))

c1.update(c2)
print(sum(c1.values()))

print(c1.most_common(3))

c1.subtract(c2)
print(c1.most_common(3))

print(c1 & c2)