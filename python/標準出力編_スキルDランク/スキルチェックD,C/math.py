E=input().split('+')
result = 0
for num in E:
    tens = num.count('<')
    ones = num.count('/')
    result += tens * 10 + ones
print(result)

