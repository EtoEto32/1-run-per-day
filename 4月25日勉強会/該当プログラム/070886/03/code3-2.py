birds = ["鳩","雀","オウム","フクロウ","ペンギン"]
print()
#インデックスでアクセス
print(birds[2])

#indexメソッドを使うと値からインデックスが取得できる
print(birds.index("ペンギン"))

#リストはミュータブル
birds[2]= "カラス"
print(birds)