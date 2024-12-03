a,b=map(int,input().split())

count=0

while True:
    if a%b==0:
        a=a/b
        count+=1
    else:
        break
print(count)