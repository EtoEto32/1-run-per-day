data = list(map(str, input().split()))  # Bob=X Alice=Y
total1 = 0
total2 = 0
for index, i in enumerate(data, 1):
    for j in i:
        if index == 1:
            j = int(j)
            total1 += j
        else:
            j = int(j)
            total2 += j
total1 = str(total1)
result1 = total1[-1]
total2 = str(total2)
result2 = total2[-1]
if result1 > result2:
    print("Bob")
elif result1 == result2:
    print("Draw")
else:
    print("Alice")
