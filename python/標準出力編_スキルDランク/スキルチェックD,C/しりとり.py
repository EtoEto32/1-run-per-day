N = int(input())
temp = []
for _ in range(N):
    s = input()
    temp.append(s)

for i in range(N - 1):
    if temp[i][-1] == temp[i + 1][0]:  # 現在の要素と次の要素の確認
        pass
    else:
        print(temp[i][-1], temp[i + 1][0])
        break  # ここがifのイメージ
else:  # ループが最後まで回ったら（途中でbreakされなかったら）
    print("Yes")
