import string

lower = list(string.ascii_lowercase)
N = int(input())
S = list(input())
re = [S.count(y) for y in lower]
print(" ".join(map(str, re)))

# 内包表記使うとスッキリする。（気持ち考えもまとまる気がする。）
