n,m,k=map(int,input().split())
#N が M ずつ増えるとき、何回目に K を越えるか出力してください。
count=0
temp=n
while(temp<=k):
    if n!=0 and m!=0 and k!=0:
        count+=1
        temp+=m
print(count)
    
    
    