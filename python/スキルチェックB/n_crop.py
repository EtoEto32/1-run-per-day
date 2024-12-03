N, M = map(int, input().split())  # 作業回数N,作物の種類数M
H, W = map(int, input().split())  # 畑の行数H,列数W

# 畑の初期化
field = [["." for _ in range(W)] for _ in range(H)]
# 収穫した量
count = [0] * M

# 納期ごとの作業
for _ in range(N):
    a, b, c, d, e = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    e -= 1  # 0ベースに
    # 収穫
    for i in range(a, b + 1):
        for j in range(c, d + 1):
            if field[i][j] != ".":
                count[int(field[i][j]) - 1] += 1
    # 植える
    for i in range(a, b + 1):
        for j in range(c, d + 1):
            field[i][j] = str(e + 1)  # 実際の数字に変換
# 収穫量
for c in count:
    print(c)
# 最終的な畑の状態,行ごとに
for row in field:
    print("".join(row))
