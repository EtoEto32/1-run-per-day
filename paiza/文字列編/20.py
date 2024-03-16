s = input().split("/")
ans = ""
temp = []
for i in s:
    if ":" in i:
        temp = i.split(":")
        for j in temp:
            print(j)
    else:
        print(i)
