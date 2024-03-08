n=int(input())
m=list(map(int,input().split()))
total=0
for i in m:
    if i%2==1:
        break
    total+=i
print(total)