n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

index_of_k=-1

for i in range(n):
    if k not in a:
        pass
else:
    for i in range(n):
        if a[i]==k:
            index_of_k=i
            print(index_of_k+1)


#以下模範解答

n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

for i in range(n):
    if a[i] == k:
        print(i + 1)
#結構簡単に行けた