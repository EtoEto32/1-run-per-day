n,a,b=map(int,input().split())
data=list(map(int,input().split()))
sum_ans=0

for i in range(a-1,b):#リストのインデックスは0から始まるため、1から3番目だったらリストの0から2番目までを取り出す
    sum_ans+=data[i]
print(sum_ans)
    