N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for l in range(N)]
maximum = -1
for i in matrix:
    for j in i:
        maximum = max(maximum, j)
print(maximum)
