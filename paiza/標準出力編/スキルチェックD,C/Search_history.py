n=int(input())
Strings=[input() for x in range(n)]
val=[]
ans=[]
#以前のモノ
#['book','candy', 'apple', 'book', 'candy']
#['candy', 'apple', 'book', 'candy']
#['apple', 'book', 'candy']
#['book', 'candy']
#['candy']
#[]
count=0
strlist_copy = Strings.copy()  #コピーの作成
for i in range(len(Strings)):#どんどんStringが減ってくから別の参照用のコピーをつくるべき
    for j in strlist_copy:
        count+=1
        compair=strlist_copy[count:]
        if j in compair:
            Strings.pop(i)
Strings.reverse()
for i in Strings:
    print(i)
    