import math

# print(a)
a = '5'
# b = a + 5
b = int(a) + 5
b = a + str(5)
# c = 'a' * 5
# print(c)

# print(math.PI)
print(math.pi)
math.PI = 3.14
print(math.PI)

#IndexError
lst = ['MacOS','Windows','Linux']
# print(lst[3])
#KeyError
dict = {'x':10,'y':20}
print(dict['x'])
print(dict['y'])
# print(dict['z'])

print(dict.get('x'))
print(dict.get('y'))
print(dict.get('z'))
for key in dict.keys():
    print(key)