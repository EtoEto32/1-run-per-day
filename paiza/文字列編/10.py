s=input()#文字列を受け取る
values=input().split()#文字列を受け取ってリストに文字列を格納する
i=int(values[0])#リストの0番目の要素を整数に変換してiに代入
c=int(values[1])#リストの1番目の要素を整数に変換してjに代入

print(s[:i-1]+c+s[i:])#文字列のスライスを使ってi番目の文字をcに置き換える
#元の文字列の変更する文字の位置より前の部分 + 変更した文字 + 元の文字列の変更する文字の位置より後ろの部分