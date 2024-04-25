# forループでリスト生成
lst_01 = [0,1,2,3,4,5,6,7,8,9]
lst_02 = [] #空のリスト
for i in lst_01:
    lst_02.append(i**2)
print(f"lst_02 {lst_02}")

lst_02.insert(3,6)
print(f"6を追加 {lst_02}")

lst_02.pop(3)
print(f"[3]の値を削除 {lst_02}")

lst_02.sort(reverse = True)
print(f"降順に並び替え {lst_02}")

lst_02.sort()
print(f"昇順に並び替え {lst_02}")

lst_03= [5,1,2,8,6,7,3,9,4]
lst_03.reverse()
print(f"逆順に並び替え {lst_03}")