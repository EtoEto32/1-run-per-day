ATK, DEF, AGI = map(int, input().split())
N = int(input())
data = []
for i in range(N):
    string, ATK_above, ATK_below, DEF_above, DEF_below, AGI_above, AGI_below = (
        input().split()
    )
    data.append(
        [
            string,
            int(ATK_above),
            int(ATK_below),
            int(DEF_above),
            int(DEF_below),
            int(AGI_above),
            int(AGI_below),
        ]
    )
count = 0
found = False  # 進化条件を満たすモンスターが見つかったかどうかを追跡するための変数
for row in data:
    count += 1
    if (
        (row[1] <= ATK <= row[2])
        and (row[3] <= DEF <= row[4])
        and (row[5] <= AGI <= row[6])
    ):
        print(row[0])
        found = True
if not found:  # 進化条件を満たすモンスターが1つも見つからなかった場合
    print("no evolution")
