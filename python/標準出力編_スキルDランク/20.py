Q = int(input())
for i in range(Q):
    values = input().split()
    N = float(values[0])
    M = int(values[1])
    print("{:.{}f}".format(N, M))
