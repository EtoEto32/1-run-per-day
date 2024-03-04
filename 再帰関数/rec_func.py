# 参考：https://qiita.com/dhirabayashi/items/2f079e62fa2e286f1766
def total(n):  # 1からnまでの合計
    if n < 1:  # 1未満は合計0
        return 0
    return n + total(n - 1)
#total関数には引数として(n - 1)が渡されるので、total関数が再帰呼び出しされるたびに
#引数nの値は1ずつ小さくなっていきます。
print(total(5))      # 15
print(total(10))     # 55
print(total(100))    # 5050

# 再帰関数のコツとして
# あたかも関数が実装済みであるかのように考える
