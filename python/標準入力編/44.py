# map関数は可変長引数を取ることができる

N = int(input())
a = []
for i in range(N):
    M_and_a_i = list(map(int, input().split()))
    a.append(M_and_a_i[1:])  # 2番目以降を取り出す

for i in range(N):
    print(*a[i])
