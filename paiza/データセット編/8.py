n = int(input())
nums = list(map(int, input().split()))
ans = [0] * 10  # 0で埋める

for i in nums:
    ans[i] += 1

for j in range(len(ans)):
    if j == len(ans) - 1:
        print(ans[j])
    else:
        print(ans[j], end=" ")
