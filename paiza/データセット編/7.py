H, W, r, c = map(int, input().split())
maze = [input() for _ in range(H)]#1次元配列に格納、実際には2次元配列

if maze[r - 1][c - 1] == "#":#配列の中にある文字を指定している
    print("Yes")
else:
    print("No")
#入力例と出力例
#
# 3 4 1 2
#   ..#.
#   #.##
#   ....


#出力例1
#No