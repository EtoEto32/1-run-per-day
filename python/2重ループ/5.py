H, W = map(int, input().split())
li = [[int(x) for x in input().split()] for i in range(H)]

for i in range(len(li)):
    for j in range(len(li[i])):
        print(li[i][j], end="")

        if j < len(li[i]) - 1:
            print(end=" ")
        else:
            print()
