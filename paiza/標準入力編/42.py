M = int(input())
a = []
for i in range(3):
    a_i = list(map(int, input().split()))
    a.append(a_i)

for i in range(3):
    print(*a[i])

# 変数M関係なくて草
