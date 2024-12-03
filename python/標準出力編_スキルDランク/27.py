N, A, B = map(str, input().split())
N = int(N)
for i in range(N):
    if i == N - 1:
        print("{}".format((int(A), int(B))))
    else:
        print("{}, ".format((int(A), int(B))), end="")


# 模範解答
values = input().split()
N = int(values[0])
A = int(values[1])
B = int(values[2])

for i in range(N):
    if i < N - 1:
        print("({}, {})".format(A, B), end=", ")
    else:
        print("({}, {})".format(A, B))
# 解説
# pythonのformatメソッドの引数は整数でも文字列でもいい
