from itertools import permutations

s = input()
t = input()

st = set()
count = 0
for i in permutations(s):
    st.add("".join(i))


for j in st:
    if (t in st) and (s != t):
        print("YES")
        break
    else:
        count += 1
if count == len(st):
    print("NO")
