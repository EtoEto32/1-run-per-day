def reformat_text():
    import sys

    input = sys.stdin.read
    data = input().split("\n")  # 分割されたものがリストになって保存される。
    # 標準入力されたものを一括で読み取る。
    # 1行目から H, W, X を読み取る
    H, W, X = map(int, data[0].split())
    # 次の H 行を読み取る
    lines = data[1 : H + 1]
    print(lines)

    # すべての行を連結して1つの文字列にする
    full_text = "".join(lines)

    # 出力用のリストを準備する
    output_lines = []
    for i in range(0, len(full_text), X):
        output_lines.append(full_text[i : i + X])

    # 結果を出力する
    for line in output_lines:
        print(line)


# 関数を呼び出す
reformat_text()
