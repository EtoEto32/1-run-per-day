N = int(input())
Nums = []
for _ in range(N):
    Nums.append(int(input()))
maxdietdays = 0
maxlazydays = 0
Increase = 0
Decrease = 0
for i in range(1, N):
    if Nums[i] < Nums[i - 1]:
        Increase += 1
        Decrease = 0  # 一回太ったらリセット
    else:
        Decrease += 1
        Increase = 0  # 一回痩せたらリセット
    maxdietdays = max(
        maxdietdays, Increase
    )  # 最大の増加日を指定　第一引数と第二引数の大きな方を更新する。
    maxlazydays = max(
        maxlazydays, Decrease
    )  # 最大の減少日を指定　第一引数と第二引数の小さな方を更新する。
print(maxdietdays, maxlazydays)
