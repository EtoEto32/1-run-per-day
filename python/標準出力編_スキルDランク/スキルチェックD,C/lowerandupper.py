S = input()  # 検閲ルール
T = input()  # 該当文字列
a = "abcdefghijklmnopqrstuvwxyz"

for i in range(26):
    if S[i].isupper():  # 検閲ルールが大文字だったら
        T = T.replace(a[i].lower(), S[i])  # (Tから該当文字列検索,置き換え後の文字)
    else:  # 検閲ルールが小文字だったら
        T = T.replace(a[i].upper(), S[i])
print(T)
