n=int(input())
data1=list(map(int,input().split()))
m=int(input())
data2=list(map(int,input().split()))

for i in data2:
    print(data1[i-1])
    
"""
N = int(input())
A = [int(x) for x in input().split()]
Q = int(input())
B = [int(x) for x in input().split()]

for i in range(Q):
    print(A[B[i]-1])
"""