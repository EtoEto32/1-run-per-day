n = int(input())
a = [int(x) for x in input().split()]

maximum = 1000000001
for i in range(2):
    next_maximum = -1000000001
    for val in a:
        if val < maximum:
            next_maximum = max(next_maximum, val)
    maximum = next_maximum

print(maximum)