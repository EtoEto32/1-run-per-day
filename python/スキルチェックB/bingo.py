N, M = map(int, input().split())  # Nはビンゴの行列数
# リスト内包表記
bingo = [list(map(int, input().split())) for i in range(N)]
# bingo初期テーブル
table = []
for i in range(N):
    row = []  # １行ごとに追加
    for i in range(N):
        row.append(False)
    table.append(row)

check = list(map(int, input().split()))

# 当選番号による穴埋めコードを書く
for row in range(len(bingo)):  # 行
    for column in range(len(bingo[row])):  # 列
        if bingo[row][column] in check or bingo[row][column] == 0:
            table[row][column] = True


# 当選チェックのコードを書く
winning = 0
count = 0
# 縦のチェック
for i in range(N):
    count = 0
    for j in range(N):
        if table[i][j]:
            count += 1
    if count == N:  # 1行ずつ出力させない為
        winning += 1
# 縦のチェック
for i in range(N):
    count = 0
    for j in range(N):
        if table[j][i]:
            count += 1
    if count == N:  # 1行ずつ出力させない為
        winning += 1
# 斜めのチェック（左上から右下）
count = 0
for i in range(N):
    if table[i][i]:
        count += 1
if count == N:
    winning += 1

# 斜めのチェック（右上から左下)
count = 0
for i in range(N):
    if table[i][N - 1 - i]:  # 上手い感じにデクリメント
        count += 1
if count == N:
    winning += 1


print(winning)
