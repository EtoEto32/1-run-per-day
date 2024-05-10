N=input()  # 嫌いな数字
M=int(input())  # 病室の総数

preferred_rooms=[]  # 嫌いな数字が含まれていない部屋を保存するリスト

for i in range(M):
    Num = input()
    if N not in Num:  # 文字として比較
        preferred_rooms.append(Num)

# 嫌いな数字が入っていない部屋が1つもなければ"none"を出力
if not preferred_rooms:#つまりからだったらnoneを返すという意味
    print("none")
else:
    for room in preferred_rooms:
        print(room)
