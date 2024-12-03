values = input().split()
N = int(values[0])
M = int(values[1])#入力された値がインデックスの2番目の要素に代入される。

A = [0] * N
values = input().split()

#values = input().split()
#N = int(values[0])
#M = int(values[1])

#A = [int(x) for x in input().split()]
#B = [int(x) for x in input().split()]
#これでも行ける

for i in range(N):
    A[i] = int(values[i])

B = [0] * M
values = input().split()
for i in range(M):
    B[i] = int(values[i])
#要するにリストにそれぞれの要素を代入しただけ
#A[1,2,3,4,5,6,7,8,9,10]
#B[2,6,1,1]
head = 0#次出力するインデックスの情報を保持
for i in B:
    for j in range(i):
        if j == i - 1:# 各行の最後の行を出力し改行するため
            print(A[head])#飽くまでもAのデータを参照し出力、range由来の数値ではない。
        else:
            print(A[head], end=" ")

        head += 1#次のインデックスの確保
    