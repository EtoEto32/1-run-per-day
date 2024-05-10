n=int(input())
a_n=list(map(int,input().split()))

for i in a_n:
    if i%2==0:
        print(a_n.index(i)+1)
        break