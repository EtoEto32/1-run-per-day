s=input()
set1=[]
for i in s:
    set1.append(i)
set1=set(set1)
if len(set1)<len(s):
    print("NG")    
else:
    print("OK")

test = ['ab', 'c', 'de',4]
map_result = map(str, test)
print(map_result)
result = ''.join(map_result)
print(result)