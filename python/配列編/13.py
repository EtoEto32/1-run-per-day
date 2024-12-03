li = [[6, 5, 4, 3, 2, 1], [3, 1, 8, 8, 1, 3]]

for i in range(len(li)):
    for j in range(len(li[i])):
        print(li[i][j], end="")

        if j < len(li[i]) - 1:
            print(end=" ")
        else:
            print()