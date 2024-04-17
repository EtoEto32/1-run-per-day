N, M = map(int, input().split())
# 入力 10 2
# 出力 1010

# 10進数をn進数に変更（変数的に言うと、m進数法）
base = ""
while N > 0:
    base += str(N % M)  # 一回目"0",二回目"1",三回目"0".四回目"1"
    N //= M  # 一回目"5",二回目"2",三回目"1",四回目"0"

print(base[::-1])  # 逆順にすることが出来る。

"""このアルゴリズムは、10進数を任意の基数（この場合はM）に変換するためのものです。以下にその詳細を説明します。
初期化: baseという空の文字列を作成します。これは、最終的な結果を保存するためのものです。
ループ: Nが0より大きい間、以下の操作を繰り返します。
NをMで割った余りをbaseに追加します。これは、NをM進数に変換したときの各桁の値を求めるためのものです。
NをMで割ります。これにより、次の桁の値を求める準備ができます。
逆順にする: 最後に、baseを逆順にします。なぜなら、上記のループでは最低位から最高位の順に値を求めているため、逆順にすることで正しい順序になります。
このアルゴリズムが成り立つ理由は、我々が普段使っている10進数のシステムと同じ原理に基づいています。10進数では、各桁は10のべき乗を表しています（例えば、100の位は102、10の位は101、1の位は100）。同様に、このアルゴリズムでは、各桁はMのべき乗を表しています。したがって、このアルゴリズムは任意の基数に対して有効です。この原理は、コンピュータ科学におけるビット演算やエンコーディングの基礎となっています。"""
