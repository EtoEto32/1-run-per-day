N = int(input())
val = list(map(int, input().split()))

print(min(val))

N = int(input())
a = list(map(int, input().split()))
min_num = 0
for i in range(N):
    if a[i] > min_num:
        min_num = a[i]
print(min_num)
