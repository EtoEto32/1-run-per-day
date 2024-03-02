# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
n,d=map(int,input().split())
data=[int(input()) for i in range(n-1)]
ans=d

for i in data:
    ans+=(d-i)
    

print(ans*d)
