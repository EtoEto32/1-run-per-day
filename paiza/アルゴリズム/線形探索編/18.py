N = int(input())
li = list(map(int, input().split()))
K = int(input())
li = sorted(li)
print(li[-K])


n = int(input())
a = [int(x) for x in input().split()]

maximum = 1000000001
for i in range(K):
    next_maximum = -1000000001
    for val in a:
        if val < maximum:
            next_maximum = max(next_maximum, val)
    maximum = next_maximum

print(maximum)