import json

# 文字列
string = "[2,3]"

# リストに変換
array = json.loads(string)

print(array)
print(type(array))
