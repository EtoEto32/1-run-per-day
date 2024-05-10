n, r = map(int, input().split())
for i in range(1, n + 1):
    h, w, d = map(int, input().split())
    diameter = 2 * r
    if diameter <= h and diameter <= w and diameter <= d:
        print(i)
