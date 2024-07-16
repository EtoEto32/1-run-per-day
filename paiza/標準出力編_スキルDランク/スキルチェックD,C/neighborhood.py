N, D = map(int, input().split())
X, Y = map(int, input().split())
neighborhood = 0
for i in range(N):
    x_n, y_n = map(int, input().split())
    distance = abs(X - x_n) + abs(Y - y_n)
    if distance <= D:
        neighborhood += 1
print(neighborhood)
