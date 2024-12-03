N, L = map(int, input().split())


myself = L

for i in range(N):
    enemy = int(input())
    if myself > enemy:
        myself += int(enemy / 2)
    elif myself == enemy:
        pass
    else:
        myself = int(myself / 2)
print(myself)
