n=int(input())
val=map(int,input().split())

for i in val:
    if i%2==0:
        print("even")
    else:
        print("odd")