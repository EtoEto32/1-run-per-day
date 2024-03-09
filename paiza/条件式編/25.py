a,b=map(int,input().split())#・ A ≦ B
if not(a<0 and b>0):
    if abs(a)<abs(b):#絶対値取得
        print(a*a)
    else:
        print(b*b)
elif a>0:
    print(b*b)
else:
    print(a*b)
    
a, b = [int(x) for x in input().split()]

if a <= 0 and b >= 0:
    # a から b の間に 0 が含まれる
    print(a * b)
elif a > 0:
    # a と b が両方とも正の数
    print(a * a)
else:
    # a と b が両方とも負の数
    print(b * b)