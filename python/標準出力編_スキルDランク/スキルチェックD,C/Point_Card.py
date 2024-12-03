N=int(input())
point_total=0
for i in range(N):
    A=list(map(int,input().split()))
    if A[0]==3 or A[0]==13 or A[0]==23 or A[0]==30 or A[0]==31:
        point_total+=(A[1]*0.03)
        point_total=int(point_total)
    elif A[0]==5 or A[0]==15 or A[0]==25:
        point_total+=(A[1]*0.05)
        point_total=int(point_total)
    else:
        point_total+=(A[1]*0.01)
        point_total=int(point_total)
print(point_total)    
        
    
    

