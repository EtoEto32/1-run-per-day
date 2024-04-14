N=int(input())
val=list(map(int,input().split()))

print(max(val))

N = int(input())
a = list(map(int, input().split()))
max_num = 0
for i in range(N):
    if a[i] > max_num:
        max_num = a[i]
print(max_num)