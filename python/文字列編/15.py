S=input()
ans=[]
for i in S:
    if i.islower():
        ans.append(i.upper())
    else:
        ans.append(i.lower())
for i in ans:
    print(i,end="")

# 以下のように書き換えることもできる
s = input()

for ele in s:#文字列の各文字に対して
    if ele.islower():#もし小文字なら
        print(ele.upper(), end="")#大文字に変換して出力する
    else:
        print(ele.lower(), end="")#大文字なら小文字に変換して出力する

print()#改行する