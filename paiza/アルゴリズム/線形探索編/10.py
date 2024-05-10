N=int(input())
A_n=list(map(int,input().split()))
K=int(input())
Ans=[]
for i in range(N):
    if A_n[i]>=K:
        Ans.append(A_n[i])

print(min(Ans))