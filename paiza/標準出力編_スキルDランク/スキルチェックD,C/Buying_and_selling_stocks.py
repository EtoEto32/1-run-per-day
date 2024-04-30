N1, C1, C2 = map(int, input().split())
stacks = 0
nums = [int(input()) for i in range(N1)]
day = 0
benefit = 0
for num in nums:
    day += 1  # 日にち更新
    if day == N1:
        # 持ち株全部売る
        benefit += num * stacks
        stacks = 0
    elif num <= C1:
        # 株を1つ買う
        stacks += 1
        benefit -= num
    elif num >= C2:
        # 持ち株全部売る
        benefit += num * stacks
        stacks = 0
    else:
        pass

print(benefit)
