"""
最初に現れる k の添字を保存する変数 index_of_k を用意し、for 文などのループを用いて数列を先頭から見ていき、
最初に k が現れたときの添字を index_of_k に保存し、ループを抜け index_of_k を出力すればよいです。
index_of_k の初期値を0にしておくと、数列に k が現れなかった場合の処理が楽になります。
"""
n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

index_of_k= -1
for i in range(n):
    if a[i]==k:
        index_of_k=i
        break
print(index_of_k+1)