# 入力の読み取り
N, M = map(int, input().split())
input_data = []
type_card = []
count = 0
# カードの全種類をリストに格納
for i in range(1, M + 1):
    # リストに追加
    type_card.append(i)

for _ in range(N):
    num = int(input())
    input_data.append(num)
# すべてのtype_cardのデータがinput_dataに含まれているか確認
if all(data in input_data for data in type_card):
    # 今まで開封したカードの種類を格納するためのsset
    collected = set()
    # カードを順番に開けていく
    for idx, card_value in enumerate(input_data, 1):
        # idxは1~Nまでの数値（要するに何回開封したか）,cardはinput_dataの値
        collected.add(card_value)
        # すべてのカードを開け終わったので抜ける。
        if len(collected) == M:
            count = idx
            break
else:
    print("unlucky")
    exit(0)
print(count)
