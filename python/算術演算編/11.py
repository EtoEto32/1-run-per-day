"""変数 N を 10,000 で初期化する
N を A で割った商を N へ代入する
N を B で割った余りを N へ代入する
N を出力する"""
a,b=map(int,input().split())
n=10000
n//=a
n%=b
print(n)