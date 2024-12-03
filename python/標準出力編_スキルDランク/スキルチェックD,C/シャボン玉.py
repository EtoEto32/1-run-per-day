T, x, y = map(int, input().split())
ans = []
for i in range(T - 1):
    a, b = map(int, input().split())
    a += x
    ans.append(a)
print(max(ans))
