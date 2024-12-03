N = int(input())
ans = 0
init = 1
for i in range(N):
    num = int(input())
    ans += abs(num - init)
    init = num#その時点での現在地を保存
print(ans)
