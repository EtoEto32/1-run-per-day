values = input().split()
H = int(values[0])
W = int(values[1])
A = int(values[2])
B = int(values[3])

for i in range(H):
    for j in range(W):
        print("({}, {})".format(A, B), end="")
        if j == W - 1:
            print()
        else:
            print(end=" | ")

    if i < H - 1:
        print("=" * (6 * W + 3 * (W - 1)))
        # 6*Wはタプルの部分の文字数、3*(W-1)は区切り文字の文字数
        # 分けて考えると合計しやすい
