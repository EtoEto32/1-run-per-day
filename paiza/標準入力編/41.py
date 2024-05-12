N = int(input())
a = []
for i in range(N):
    a_i = list(map(int, input().split()))
    a.append(a_i)

for i in range(N):
    print(*a[i])
# ここで、*を使うことで、リストの中身をそのまま出力することができる。
"""
例えば、print(*a[i]) とすると、リスト a[i] の各要素が print 関数に個別に渡されます。
これは、print(a[i][0], a[i][1], a[i][2], ...) と書くのと同じ効果がありますが、
要素の数が事前にわからない場合や変動する場合に便利です。
"""
