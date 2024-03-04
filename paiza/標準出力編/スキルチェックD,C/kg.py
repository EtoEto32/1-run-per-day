n, p, q = map(int, input().split())
# n仕入れる量,p生で売れる割合,q惣菜で売れる割合
# 入力値例1,80,40

p = p / 100  # 割合に直す
q = q / 100

n_1 = n * p  # 生の売れた量
n_2 = n - n_1  # 売れ残りを加工した惣菜
n_3 = n_2 * q  # 惣菜を販売した量

print("{:.4f}".format(n_3 - n_2))
# 悔しい有効数字.....
