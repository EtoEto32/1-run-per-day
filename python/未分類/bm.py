def build_bad_char_table(pattern):
    """
    不一致文字規則用のテーブルを作る関数
    petternに含まれる各文字が、最後に出現する位置を記録する。
    出現しない文字は-1とする。
    """
    table = [-1] * 256
    # とりあえずASCII文字を想定する。
    for i, ch in enumerate(pattern):
        table[ord(ch)] = i
        # ord(ch)で文字chに対応するASCIIコードを返す。
        # table[ord(ch)]=iにより、その文字のパターンが何番目に出現するのかをマッピング
    return table


# テキストを検索し一致したパターンの先頭の位置を返す関数
def bm_search(text, pattern):
    if pattern == "":
        # 空文字は一致とみなす。
        return 0

    bad_char_table = build_bad_char_table(pattern)
    m = len(pattern)  # パターンの長さ
    n = len(text)  # 検索テキストの長さ
    s = 0  # テキストを検索する中でパターンを重ねる位置を記憶する変数

    # 検索するテキストの方がでかいはず
    while s <= n - m:
        j = m - 1
        # 末尾から比較＆操作する。

        while j >= 0 and pattern[j] == text[s + j]:
            # こいつらが同じなら更に前の文字へ移動
            j -= 1

        # この条件のときはすべての文字が一致したとの事
        if j < 0:
            return s
        else:
            # jが0以上つまり不一致が少なくとも見つかったという意味
            # ここで肝となるずらしの処理が入る
            bad_char_pas = bad_char_table[ord(text[s + j])]
            # 不一致が起きたテキスト側の文字text[s+j]を基に、
            # パターン内でその文字が最後に出現した位置をbad_car_posに取得する。
            # 出現しない場合は、仕様上-1が返ってくる。
            shift = max(1, j - bad_char_pas)
            # 最低でも1はずらす事で無駄な比較を減らす事が出来る。

            s += shift
            # 比較位置の新たな更新
    return -1


# テキストを最後まで検索してもパターンが見つからない場合は-1を返す。
# テスト
text = "takada kenshi"
pattern = "kenshi"

pos = bm_search(text, pattern)
print(pos)
