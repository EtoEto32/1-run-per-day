k, n = map(int, input().split())

for i in range(k):
    d_1, d_2 = map(int, input().split())
    per_question = 100 / n
    score = per_question * d_2
    if d_1 <= 0:
        if score >= 80:
            print("A")
        elif score >= 70:
            print("B")
        elif score >= 60:
            print("C")
        else:
            print("D")
    elif d_1 <= 9:
        score *= 0.8
        score = int(score)
        if score >= 80:
            print("A")
        elif score >= 70:
            print("B")
        elif score >= 60:
            print("C")
        else:
            print("D")
    else:
        print("D")
