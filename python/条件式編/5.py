n=int(input())
val=[]

for i in range(n):
    x=int(input())
    val.append(x)
if 0 not in val:
    print("YES")
else:
    print("NO")
    
"""n = int(input())
a = [int(input()) for _ in range(n)]

x = 1
for ele in a:
    x *= ele

if x == 0:
    print("NO")
else:
    print("YES")"""