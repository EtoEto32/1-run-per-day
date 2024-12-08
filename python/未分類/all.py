N = int(input().strip())
numbers = list(map(int, input().strip().split()))
M = int(input().strip())

if all(M % x == 0 for x in numbers):
    print("YES")
else:
    print("NO")
