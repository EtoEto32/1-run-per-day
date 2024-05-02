#行と列
H,W=map(int,input().split())
#パネルの状態を表すマトリックスを読み込む（1つずつ）
matrix=[]
score_total=0
for _ in range(H):
    row=list(input())
    matrix.extend(row)
#パネルの得点を表すマトリックスを読み込む（1つずつ）
numbers=[]
for _ in range(H):
    row=list(map(int,input().split()))
    numbers.extend(row)
for i,j in zip(matrix,numbers):
    if i=='o':
        score_total+=j
print(score_total)        
