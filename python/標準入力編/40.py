import sys

# 3x3の行列を読み込む
matrix = [list(map(int, input().split())) for _ in range(3)]

# 読み込んだ行列をそのまま出力する
for row in matrix:
    print(
        " ".join(map(str, row))
    )  # 半角スペース区切りに対応し受け取った2次元配列の要素（配列型）を文字列型に変換して出力する
