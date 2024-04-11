n = int(input())
# ("le", "ge" はそれぞれ "less than or equal to", "greater than or equal to" の略で「〜以下」「〜以上」の意味)。
# le:以下
# ge:以上
le_value = 0
ge_value = 0
le_lst = []
ge_lst = []
for i in range(n):
    s = input().split()
    s0 = s[0]
    s1 = float(s[1])
    if s0 == "ge":
        ge_lst.append(s1)
    else:
        le_lst.append(s1)
print(max(ge_lst), min(le_lst))

# そもそも分ける
# s1がle,ge分で重複させる。
