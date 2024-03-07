n = int(input())
data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))
for i, j in zip(data1, data2):
    print(i - j)

# 模範解答

"""N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(N):
    print(a[i] - b[i])"""

n, a, b = map(int, input().split())
data = list(map(int, input().split()))

a = sum(data[a - 1 : b])
print(a)
