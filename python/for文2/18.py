n=int(input())
# list型で取得
l = [int(i) for i in input().split()]
temp=[]
for index,i in enumerate(l) :#より正確なインデックスを把握する事が可能。
    temp.append(i+(index+1))
print(min(temp))
    

