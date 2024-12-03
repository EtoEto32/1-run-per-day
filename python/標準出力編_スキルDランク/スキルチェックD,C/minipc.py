n=int(input())
var1=0
var2=0
for i in range(n):
    s=input().split(" ")
    if s[0]=="SET" and s[1]=="1":
        var1=s[2]
    elif s[0]=="SET"and s[1]=="2":
        var2=s[2]
    elif s[0]=="ADD":
        var1=int(var1)
        s[1]=int(s[1])
        var2=var1+s[1]
    elif s[0]=="SUB":
        var1=int(var1)
        s[1]=int(s[1])
        var2=var1-s[1]
print(var1,var2)
    
    