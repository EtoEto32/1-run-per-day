s = input()
i, j = map(int, input().split())

print(s[i - 1 : j])  # indexは0から始まるので-1する
# 文字列のスライスはs[開始位置:終了位置]で指定する　[以上：未満]
# 例えば、s="abcde"のとき、s[1:3]は"bc"となる