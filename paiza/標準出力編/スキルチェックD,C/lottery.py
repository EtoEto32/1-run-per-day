b=int(input())
bplus=b+1
bminus=b-1
n=int(input())

for i in range(n):#1個ずつ処理できる
    num=input()
    if num==b:
        print("first")
    elif (num==bplus) or (num==bminus):
        print("abjacent")
    elif num[4:]==b[4:]:
        print("second")
    elif num[3:]==b[3:]:
        print("third")
    else:
        print("blank")