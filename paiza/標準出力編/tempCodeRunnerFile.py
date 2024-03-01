N,M=input().split()
N=int(N)
M=int(M)
dis= [int(input()) for _ in range(N)]
print(dis)
total=0
for i in dis:
    if i <= M:
        total+=i
print(total)   