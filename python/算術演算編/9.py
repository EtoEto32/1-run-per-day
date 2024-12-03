"""変数 N を 0 で初期化する
N に A を足した値を N へ代入する
N に B をかけた値を N へ代入する
N を C で割ったあまりを N へ代入する
N を出力する"""
n=0
a,b,c=map(int,input().split())
n+=a
n*=b
n%=c
print(n)