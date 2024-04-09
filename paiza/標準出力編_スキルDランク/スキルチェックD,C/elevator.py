N = int(input())
ans = 0
init = 1
for i in range(N):
    num = int(input())
    ans += abs(num - init)
    init = num
print(ans)
