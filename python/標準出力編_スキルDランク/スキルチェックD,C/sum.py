a, b = input().split()
# aとbの長さを揃える
max_len = max(len(a), len(b))
a = a.zfill(max_len)
b = b.zfill(max_len)
print(a)
print(b)

result = ""
# 各桁を足し算し、繰り上がりを無視
for a, b in zip(a, b):  # zip関数を使えばrange()のようにint型もイテレーターに...
    temp = int(a) + int(b)
    result += str(temp % 10)#繰り上がり除去　1の位だけを綺麗に取り出す事が出来る。
print(result)
