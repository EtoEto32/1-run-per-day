N, X, Y = map(int, input().split())
totalprice = 0
item_count = 0
free_count = 0
temp = []

for _ in range(N):
    temp.append(int(input()))
temp = sorted(temp)

for i in range(1, N + 1):  # 無料になるものを消す
    if i == X:
        for j in range(Y):
            temp.pop(0)
for j in temp:
    totalprice += j
print(totalprice)
