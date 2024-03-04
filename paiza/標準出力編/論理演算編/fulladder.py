a,b,c=map(int,input().split())
Cx=int((a and b))#1つめの半加算器
Sy=int((a^b))

Cy=int((Sy and c))#2つめの半加算器
S=int((Sy^c))#出力

C2=int((Cx or Cy))
print(C2,S)

#模範解答
a, b, c1 = map(int, input().split())

# 半加算器のプログラム
def halfAdder(a, b):
    c = a & b
    s = a ^ b
    return (c, s)

cx, sy = halfAdder(a, b)
cy, s = halfAdder(sy, c1)
c2 = cx ^ cy

print(c2, s)