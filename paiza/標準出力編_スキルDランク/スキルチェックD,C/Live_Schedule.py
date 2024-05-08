N = int(input())
Band_A = []
Band_B = []
Sumarry_Days = ["x"] * 31
A_Days = ["x"] * 31
B_Days = ["x"] * 31
hoge = True  # トグル用
for _ in range(N):
    Band_A.append(int(input()))

M = int(input())
for _ in range(M):
    Band_B.append(int(input()))

for A in Band_A:
    A_Days[A - 1] = "〇"
for B in Band_B:
    B_Days[B - 1] = "〇"

# 以下ループ文の説明である。
# A_DaysとB_daysのそれぞれの要素をタプルにし（zip関数）インデックスを
# それぞれの組に振り分けている。
for i, (a, b) in enumerate(zip(A_Days, B_Days)):
    if a == "〇" and b == "〇":
        if hoge == True:  # トグルで交互にA,Bを代入
            hoge = bool(1 - int(hoge))
            Sumarry_Days[i] = "A"  #
        else:
            hoge = bool(1 - int(hoge))
            Sumarry_Days[i] = "B"  # ぶっちゃけインデックス同じだからA,B
            # どっちでもいい
    elif a == "〇":
        Sumarry_Days[i] = "A"
    elif b == "〇":
        Sumarry_Days[i] = "B"

for k in Sumarry_Days:
    print(k)
