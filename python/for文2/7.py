N=input()

total=0
for i in range(len(N)):
    total+=int(N[i:i+1])
print(total)