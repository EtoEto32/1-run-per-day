N = int(input())
li = []
for i in range(N):
    a, b = input().split()
    li.append([a, int(b)])
K = int(input())


for name, score in li:
    if score >= K:
        print(name)
