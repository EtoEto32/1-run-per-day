N,K=map(int,input().split())
matrix=[list(map(int,input().split())) for l in range(N)]
for i in matrix:
    total=0
    for j in i:
        total+=j
    
    print(total)
    
    