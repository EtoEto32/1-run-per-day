N = int(input())
ans = []
for i in range(N):
    values = input().split()
    if values[0] == "n" or values[1] == "n":
        ans.append(i+1)
print(len(ans))
for j in ans:
    print(j)
