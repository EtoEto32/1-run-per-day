n, k = [int(x) for x in input().split()]

m = 0
while n < k:
    n *= 2
    m += 1

print(m)