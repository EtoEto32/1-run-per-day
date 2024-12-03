s=input().split("-")
ans=0
for i in s:
    for j in i:
        j=int(j)
        if j==0:
            ans+=(12*2)
        elif j==1:
            ans+=(3*2)
        elif j==2:
            ans+=(4*2)
        elif j==3:
            ans+=(5*2)
        elif j==4:
            ans+=(6*2)
        elif j==5:
            ans+=(7*2)
        elif j==6:
            ans+=(8*2)
        elif j==7:
            ans+=(9*2)
        elif j==8:
            ans+=(10*2)
        else:#9の場合
            ans+=(11*2)
print(ans)
        
        
        
        
        
        
        