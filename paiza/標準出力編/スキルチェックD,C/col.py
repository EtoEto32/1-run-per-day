goal=int(input())
a,b,c=map(int,input().split())
if (a+b+c)<=goal:
    print("OK")
else:
    print("NG")