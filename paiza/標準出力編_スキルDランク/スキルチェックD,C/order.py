N=int(input())
temp=[]  # 確かめる用の正規のデータ
nums=[]  # 確かめる対象データ
for i in range(1,N+1):
    temp.append(i)
    nums.append(int(input()))
de_data=[]
for i in nums:
    if i not in temp:
        de_data.append(i)
s = set(nums)
result = sorted(s, key=nums.index)

for j in de_data:
    result.pop(result.index(j))  # pop()メソッドの結果をresultに再代入しない
print(len(temp)-len(result))  # resultの長さを使用

#これだとエラーがでるなぜか？？？？
#result.pop(result.index(j)) この行が原因
#pop()メソッドはjが見つからない場合、ValueErrorを返す
#なので、if文で条件分岐してからpop()メソッドを使う
#これでエラーがでない

#模範解答
N=int(input())
temp=[]  # 確かめる用の正規のデータ
nums=[]  # 確かめる対象データ
for i in range(1,N+1):
    temp.append(i)
    nums.append(int(input()))
de_data=[]
for i in nums:
    if i not in temp:
        de_data.append(i)
s = set(nums)
result = sorted(s, key=nums.index)

for j in de_data:
    if j in result:  # Check if j is in result before trying to remove it
        result.pop(result.index(j))  # pop()メソッドの結果をresultに再代入しない
print(len(temp)-len(result))  # resultの長さを使用
