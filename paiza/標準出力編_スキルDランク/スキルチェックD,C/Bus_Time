N, K = map(int, input().split())
Bus_time = []
Ans = []
Corrent_minite = 0
Time_difference = []
temp = []  # 最後の昇順にする為
for i in range(N):
    K_N = int(input())
    Bus_time.append(K_N)

for i in Bus_time:
    Time_difference.append(abs(K - i))
Early_time = min(Time_difference)
for i, j in zip(Time_difference, Bus_time):
    if i == Early_time:
        temp.append(j)
temp = sorted(temp)

for i in temp:
    print(i)
