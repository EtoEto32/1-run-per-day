N = int(input())

for i in range(1, N + 1):#この外ループが肝
    for j in range(1, i + 1):#こいつが出力される
        if j == i:#外ループのiとjを比較しiと一致したらj
            print(j)
        else:
            print(j, end=" ")


import sys
N,D=map(int,input().split())
data=[]
for i in sys.stdin:
    data.append(int(i))
print(data)
