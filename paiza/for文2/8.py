n=int(input())
val=list(map(int,input().split()))

for i in range(1,n+1):
    print(i*val[i-1])