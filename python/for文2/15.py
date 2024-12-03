n = int(input())


def funciton(n):
    if n == 1:
        return 1
    return funciton(n - 1) * n


ans = funciton(n)
print(ans)
