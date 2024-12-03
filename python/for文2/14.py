a,b=map(int,input().split())
temp=a
count=0
while(temp<=b):
    if a!=0 and b!=0:
        temp*=1.1
        temp=int(temp)
        count+=1
print(count)
    
    