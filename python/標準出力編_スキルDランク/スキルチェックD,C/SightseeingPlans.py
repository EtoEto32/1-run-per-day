N = int(input())
required_time = []  # 観光スポットごとの滞在時間
sightseeing_spot = []  # 観光スポットを廻る順番
totaltime = 0

for _ in range(N):
    required_time.append(int(input()))

traveltimes = [
    list(map(int, input().split())) for l in range(N)
]  # 行数を繰り返すイメージ
K = int(input())
for _ in range(K):
    sightseeing_spot.append(int(input()))
"""
3
2
1
4
0 3 2
3 0 8
2 8 0
4
1
2
3
1
"""
# 最初の観光スポットの滞在時間を加算
totaltime += required_time[sightseeing_spot[0] - 1]

# 観光スポット間の移動と滞在時間を加算
for i in range(len(sightseeing_spot) - 1):
    s, g = sightseeing_spot[i], sightseeing_spot[i + 1]
    # 移動の時間を足す
    totaltime += traveltimes[s - 1][g - 1]
    # 次の観光スポットの滞在時間を足す
    totaltime += required_time[g - 1]

print(totaltime)

#補足　インデックス番号を0ベースにする受け取り方法
"""
このプログラムの場合
sightseeing_spot.append(int(input()) - 1)
"""
