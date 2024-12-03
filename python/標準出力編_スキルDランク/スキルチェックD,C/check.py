import itertools

N, M = map(int, input().split())  # 標準入力からN,Mを取得
A = []  # 指定された順番に並べるべき寿司
for i in range(M):
    A.append(int(input()))

B = []  # 流れてきた寿司
for j in range(M):
    B.append(int(input()))
count = 0
for i in itertools.permutations(B, len(B)):
    i = list(i)
    if count != 1:
        for j in i:
            if j not in A:
                print("No")
                count += 1
                break
    else:
        break
else:
    print("Yes")
# 計算オーバー
