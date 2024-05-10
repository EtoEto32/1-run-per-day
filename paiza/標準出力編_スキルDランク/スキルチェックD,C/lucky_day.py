X = input()
count = 0
for i in range(365):  # 0日目からカウントを開始
    if X in str(i):
        count += 1
print(count)
# 0日目も含む（1月1日）から0から数え上げる
