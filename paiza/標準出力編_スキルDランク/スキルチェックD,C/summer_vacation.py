N = int(input())
table = list(range(1, 32))

s_1, s_2 = map(int, input().split())
# 最初のメンバー
d_start = s_1
d_end = s_2

# 残りのメンバーの休み期間を取得し、共通する期間を更新
for i in range(N - 1):
    s_1, s_2 = map(int, input().split())
    d_start = max(d_start, s_1)
    d_end = min(d_end, s_2)
# どんどん縮めていく感じ

# 共通する期間があるかどうかを判定
if d_start <= d_end:
    print("OK")
else:
    print("NG")
