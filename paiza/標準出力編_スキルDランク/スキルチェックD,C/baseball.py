N = int(input())
c1 = 0  # ボールをカウント
c2 = 0  # ストライクをカウント
for i in range(N):
    s = input()
    if s == "ball":
        c1 += 1
        if c1 == 4:
            print("fourball!")
            break
        print("ball!")
    elif s == "strike":
        c2 += 1
        if c2 == 3:
            print("out!")
            break
        print("strike!")
