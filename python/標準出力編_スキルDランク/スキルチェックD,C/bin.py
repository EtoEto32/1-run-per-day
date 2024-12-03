
n,x=map(int,input().split())
results=[]
for i in range(n):
    num=int(input())
    binary = bin(x)[2:][::-1]
    print(binary[num-1])