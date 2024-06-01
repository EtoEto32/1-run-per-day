a, b = map(int, input().split())  # 基準から見た高さ
n = int(input())

for i in range(n):
    t1, t2 = map(int, input().split())
    if t1 > a:
        print("Low")
    elif t1 == a:
        if t2 > b:
            print("High")
        else:
            print("Low")
    else:
        print("High")
