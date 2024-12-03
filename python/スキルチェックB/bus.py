#まだまだCランクの問題集とスキルチェックが必要
#思考ビタロックしてた
n,m=map(int,input().split())
fare_data=[list(map(int,input().split())) for _ in range(n)]
x = int(input())
routes=[list(map(int, input().split())) for _ in range(x)]

totalfare=0
nextindex=0
beforefare=0

for route in routes:
    row=route[0]-1
    column=route[1]-1
    beforefare=fare_data[row][nextindex]#前の駅の料金
    afterfare=fare_data[row][column]#次の駅の料金
    totalfare+=abs(beforefare-afterfare)#場所によっては負になるかも
    nextindex = column#移動先インデックスの更新
print(totalfare)