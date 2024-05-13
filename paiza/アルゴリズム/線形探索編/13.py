N=int(input())

result=[]
for i in range(N):
    Nums=input().split()
    result.append(Nums)
k=int(input())

xn,yn=result[-1]
xn=int(xn)
yn=int(yn)
ans=0
for xi,yi in result:
    xi=int(xi)
    yi=int(yi)
    if abs(xi-xn)+abs(yi-yn)<=k:
        ans+=1
print(ans)
    

    

