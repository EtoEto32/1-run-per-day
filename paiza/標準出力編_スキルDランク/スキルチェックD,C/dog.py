# 標準入力から値を取得
p1, p2 = map(int, input().split())
p3, p4 = map(int, input().split())
e1, e2, e3, e4 = map(int, input().split())
f1, f2 = map(int, input().split())

# 1回戦の結果を格納する辞書を作成
first_round = {1: e1, 2: e2, 3: e3, 4: e4}

# 1回戦の勝者を決定
winners = []
if first_round[p1] < first_round[p2]:
    winners.append(p1)
else:
    winners.append(p2)

if first_round[p3] < first_round[p4]:
    winners.append(p3)
else:
    winners.append(p4)

# 2回戦の結果を格納する辞書を作成
second_round = {}
winners.sort()
second_round[winners[0]] = f1
second_round[winners[1]] = f2

# 優勝者と準優勝者を決定
winner = min(second_round, key=second_round.get)
del second_round[winner]
runner_up = min(second_round, key=second_round.get)

# 結果を出力
print(winner)
print(runner_up)
