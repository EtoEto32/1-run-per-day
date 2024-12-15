# 考えたけどこれ間違い
import math

B = int(input())
found = False

# 上限を設定
max_A = int(math.log(B, 2)) + 1  # Bを2進数で表現したときのビット数で計算出来る
for A in range(1, max_A + 1):
    val = A
    for _ in range(1, A - 1):
        val *= A
        if val > B:
            break
    if val == B:
        print(A)
        found = True
        break
if not (found):
    print(-1)

# 改善点
# math.logを用いて計算範囲を制限
"""
math.log(B,2) 2を何乗したらBになるかという値。これを上限とすることで、Aの探索範囲を大幅に減らす。
"""
# 累乗計算の最適化
"""
Aを段階的に掛け合わせて途中でBを超えたら処理を終了する。
"""
