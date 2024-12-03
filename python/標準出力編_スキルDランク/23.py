N = int(input())
temp = []
for i in range(N):
    temp.append(input())
for j in temp:
    print("{: >3}".format(j))


# もっと簡単に書けた
N = int(input())
for _ in range(N):
    m = input()
    print("{: >3}".format(m))
