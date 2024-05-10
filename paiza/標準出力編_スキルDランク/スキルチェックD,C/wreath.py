N = int(input())
s1 = input()  # こっち基準
s2 = input()  # こいつずらして比較


# ローテートで行ける。
def rotate_string(s, n):  # 文字列をローテートする関数
    return s2[n:] + s2[:n]


for i in range(N - 1):# 入れ替える回数は(文字列の長さ-1)でいい。→先頭を基準に2番目以降を入れ替えるのみでいいから。
    conpair = rotate_string(s2, i)
    if s1 == conpair:
        print("Yes")
        break
else:
    print("No")
