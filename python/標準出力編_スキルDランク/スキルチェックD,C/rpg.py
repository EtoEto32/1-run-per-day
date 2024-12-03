N = int(input())  # 道具の個数
a_n = list(map(int, input().split()))  # 商品の単価
T, Q = map(int, input().split())  # Tは所持金
temp = []
for i in range(Q):
    temp = list(map(int, input().split()))
    item_num = temp[0]  # アイテムの識別番号
    item_qty = temp[1]  # アイテムの購入個数
    if (a_n[item_num - 1] * item_qty) <= T:
        T -= a_n[item_num - 1] * item_qty
    else:
        pass  # 何もしない。所持金がないから。
print(T)
