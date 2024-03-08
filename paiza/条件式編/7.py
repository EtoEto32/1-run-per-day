import string
c=input()

uppers=string.ascii_uppercase

if c in uppers:
    print("YES")
else:
    print("NO")
"""c = input()

if c.isupper():
    print("YES")
else:
    print("NO")
    Python では、文字の Unicode でのコードポイントを調べるとき ord 関数を使います。
Unicode のコードポイントは A から Z まで連番になっているので、ord("A") 以上 ord("Z") 以下がアルファベットの大文字の範囲となります。
従って、条件式は ord(c) >= ord("A") and ord(c) <= ord("Z") となります。"""
    

"""c = input()

if ord(c) >= ord("A") and ord(c) <= ord("Z"):
    print("YES")
else:
    print("NO")"""