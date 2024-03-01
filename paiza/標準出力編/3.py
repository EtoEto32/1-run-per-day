for i in range(10):#改行ごとの入力の場合、for文で対処可能
    if i == 9:
        print(input())
    else:
        print(input(), end=" | ")
        
