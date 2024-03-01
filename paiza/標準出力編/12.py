N = int(input())#今回出力する数列（？）の数
M = [0] * N
values = input().split()#valuesの正体はリスト
for i in range(N):
    M[i] = int(values[i])
#新しいリストを作ってint型にしただけ
#入力例の時
#4
#2 4 3 1
for i in range(N):#iはMの配列を参照する役割
    for j in range(1, M[i] + 1):#丁度リストの個数分
        if j == M[i]:#i=0のときだったらずっと2と比較
            print(j)
        else:
            print(j, end=" ")

N = int(input())
M = [int(x) for x in input().split()]

for i in range(N):
    for j in range(1, M[i] + 1):
        if j == M[i]:
            print(j)
        else:
            print(j, end=" ")
