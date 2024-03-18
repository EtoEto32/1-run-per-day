S = input()
C = input()
S = S.index(C) + 1 #文字列の変数名.find(検索したい文字や文字列) print(S.find(C) + 1)
print(S)

S = input()
C = input()
for i,ele in enumerate(S):
    if ele ==C:
        print(i+1)
        
