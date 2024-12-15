B = int(input())
found = False
for A in range(1, B + 1):
    val = A**A
    if val == B:
        print(A)
        found = True
        break
if not (found):
    print(-1)
