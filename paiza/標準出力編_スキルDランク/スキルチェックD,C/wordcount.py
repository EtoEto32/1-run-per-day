""""String=input().split()
val=[]
name=[]
for i in String:#個数と名前
    ans=String.count(i)#実際に入っている数
    val.append(ans)
    name.append(i)
print(val)
print(name)
val=set(val)#重複を削除
name=set(name)#重複を削除
print(val)
print(name)
for i,j in zip(name,val):
    print(i,j)"""""
############################################################################################
#上記のは不完全、同じ個数の要素があったら処理できない（半強制的に重複を削除してしまうから）
#少し考えてみる
""""Strings=input().split()
count=[]
name=[]
for i in Strings:#個数と名前
    name.append(i)
name=set(name)

for i in name:
    count.append(Strings.count(i))
      
for i,j in zip(name,count):
    print(i,j)"""""
###########################################################################################
#完全に分からん、順番が変ってしまう。
#英単語を出現した順番で保存しておく配列と、その出現回数を記録する配列を用意し、英単語を順に見ていきながら処理していけばよいです。
#辞書とかセットは順番が保持されない場合があるから気を付けろ
#配列を用いて、出現する英単語とその出現回数を保存します。
#配列の index メソッドを用いると、指定した要素が格納されている最初のインデックスを取得することができます。指定した要素が 1 つもなかった場合は nil が返ってきます。
li = input().split()#文字列追加

m = []
k = []

for i in li:
    if i in m:
        k[m.index(i)] += 1#対応するインデックスに加算+1
    else:
        m.append(i)#今まで出てきた要素を格納
        k.append(1)#対応するインデックスにはじめの1カウント

for i in range(len(m)):
    print(m[i], k[i])
