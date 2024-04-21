N = int(input())
li = []

for _ in range(N):
    a, b = input().split()
    li.append((a, int(b)))
# 1から100までの各数値について、すべてのヒントを満たすかどうかを確認
for a in range(1, 101):
    if all(
        ((op == ">" and a > x) or (op == "<" and a < x) or (op == "/" and a % x == 0))
        for op, x in li
    ):  # all関数のはすべての要素（条件）がTrueの場合にTrueを返す。
        print(a)
        break
# numbers = [2, 4, 6, 8, 10]
# print(all(n % 2 == 0 for n in numbers))  # 出力：True
