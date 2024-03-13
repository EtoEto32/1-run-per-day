n=int(input())
s=[int(input()) for i in range(n)]
max1=s[0]
for i in s:
    if max1 < i:
        max1=i

print(max1)
    
n=int(input())
A=[0]*n#Aをn個の0で初期化（テーブル化）
for i in range(n):
    A[i]=int(input())  #A[i]に値を代入
print(max(A))#Aの最大値を出力