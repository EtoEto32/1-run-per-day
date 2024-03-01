N = input().split()

for i in range(len(N)):
    print(N[i], end="")
    if i % 3 == 2:
        print()
    else:
        print(" ", end="")#数字を出力した後に半角