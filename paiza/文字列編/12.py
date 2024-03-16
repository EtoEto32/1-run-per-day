X=int(input())
Y=int(input())
N=int(input())
total=X+Y
total=str(total)
print(total[N-1:N])#実質的には文字列のスライスを使ってN番目の文字を取り出す

X=int(input())
Y=int(input())
N=int(input())
print(str(X+Y)[N-1])#indexを使ってN番目の文字を取り出す
#文字列もリストと同じようにindexを使って要素を取り出すことができる