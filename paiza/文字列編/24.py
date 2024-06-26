N = int(input())  # パスワードの文字数 N が与えられます。
Q = int(input())  # K さんの覚えておく文字数 Q が与えられます。
n = [0] * Q
c = [""] * Q

for i in range(Q):  # 続く Q 行では、何文字目を覚えておくかを表す n_i と覚えておく文字　c_i が与えられます。
    values = input().split()
    n[i] = int(values[0]) - 1  # リストだから-1で帳尻合わせ
    c[i] = values[1]

C = input()  # 最後の行では、パスワードの残りの部分を埋めるための文字 C が与えられます。

ans = [C] * N  # 取り敢えず埋め尽くす
for i in range(Q):
    ans[n[i]] = c[i]

print("".join(ans))
# 既定の文字列を作成するような問題の場合、初めに文字列を用意して、そこに文字を追加していき文字列を作成すると楽なことが多いです。
# N 文字のパスワードを全探索すると実行時間制限に間に合わなくなってしまうので気をつけてください。

"""パスワードの 1 文字目から順に検証しながら、答えとなる文字列の後ろに 1 文字ずつ足していくという方針で上手く実装することができます。
1 ≦ i ≦ N の i について
i が n[i] のいずれかであった場合
パスワードの i 文字目を c[i] にする。（末尾に c[i] を追加する）
それ以外の場合
パスワードの i 文字目を C にする。（末尾に C を追加する）"""
