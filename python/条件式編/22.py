n,k,t=map(int,input().split())

t_total=k*t#tターンで何メートル進んでいるか
if t_total%n==0:
    print("YES")
else:
    print("NO")