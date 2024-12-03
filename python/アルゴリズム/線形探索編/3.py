n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

index_of_k=-1

for i in range(n):
    if k not in a:
        print(0)
        break
else:
    for i in range(n-1,0,-1):
        if a[i]==k:
            index_of_k=i
            print(index_of_k+1)
            break
