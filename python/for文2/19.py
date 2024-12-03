n = int(input())
# list型で取得
l = [int(i) for i in input().split()]


for index, i in enumerate(l):
    if l[index] == 1:
        print(index + 1)
# enumerate関数はダブリがあっても、きちんとインデックスを
# 振り分けてくれる。

# indexメソッドは、同じ要素があった場合、最初のインデックスを処理してしまう。
