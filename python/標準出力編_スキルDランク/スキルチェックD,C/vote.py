N = int(input())
temp = []
count = 0
for _ in range(N):
    temp.append(input())

m = []  #
k = []  # それらの単語の出現回数を保存する
dic = {}
for i in temp:
    if i in m:
        k[m.index(i)] += 1
    else:
        m.append(i)
        k.append(1)
for key, value in zip(m, k):
    dic[key] = value

# バリューからお目当てのキーを取得
search_value = max(dic.values())

for key, value in dic.items():
    if value == search_value:
        print(key)
