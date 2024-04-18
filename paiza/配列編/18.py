li=[[1,3,5,7],[8,1,3,8]]
for i in range(len(li)):
    for j in range(len(li[i])):
        print(li[i][j], end="")

        if j < len(li[i]) - 1:
            print(end=" ")
        else:
            print()