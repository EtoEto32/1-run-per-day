from module1 import fruits

# キーの存在確認
if "orange" in fruits:
    print("orangeは存在します")
else:
    print("orangeは存在しません")

# キーの存在確認
if "orangE" in fruits:
    print("orangEは存在します")
else:
    print("orangEは存在しません")


def wordhit():
    for i in fruits.values():
        if i == "バナナ" or i == "ばなな":
            return True
print(wordhit())
