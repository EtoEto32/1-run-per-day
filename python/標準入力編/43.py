N,M= map(int,input().split())
a = []
for i in range(N):
    a_i = list(map(int, input().split()))
    a.append(a_i)

for i in range(N):
    print(*a[i])