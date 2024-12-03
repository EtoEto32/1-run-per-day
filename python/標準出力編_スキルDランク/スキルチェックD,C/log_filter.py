N = int(input())
G = input()
A = [input() for _ in range(N)]

count = 0

for i in range(N):
    if G in A[i]:
        print(A[i])
    else:
        count += 1

if count == N:
    print("None")
