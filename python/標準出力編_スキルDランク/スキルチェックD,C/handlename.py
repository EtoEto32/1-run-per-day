s = input()
ans = []

for i in s:
    if i.lower() not in ["a", "i", "u", "e", "o"]:
        ans.append(i)
print("".join(ans))

temp = "A"
temp.lower()
print(temp)

temp = temp.lower()
print(temp)

# わざわざ代入操作をしない限り値は更新されない。
