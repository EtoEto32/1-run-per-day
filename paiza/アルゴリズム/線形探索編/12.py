import numpy as np

H,W,X=map(int,input().split())
# H: 高さ, W: 幅, X: ウインドウ変更後の高さ

#"empty"で埋め尽くされた行列を作成

matrix=np.full(H,W,"empty")
print(matrix)
