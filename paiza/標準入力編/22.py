N_and_a = list(map(int, input().split()))
N = N_and_a[0]
a = N_and_a[1:]  # インデックス1番めから末尾まで格納

for i in range(N):
    print(a[i])  # 出力部分だけを出力

# 結構脳筋だった。
