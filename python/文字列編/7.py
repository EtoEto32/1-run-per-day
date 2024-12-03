n=int(input())
Strings=[input().split() for i in range(n)]#二次元配列になる
s=""
for i in Strings:#2次元配列を1次元配列にする
    for j in i:#1次元配列を文字列にする
        s+=j
print(s)

n = int(input())

ans = ""
for _ in range(n):
    ans += input()

print(ans)
#模範解答この方が自然