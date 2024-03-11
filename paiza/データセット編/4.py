n,q=map(int,input().split())
A=[int(x) for x in input().split()]
#1行　半角スペース区切りで整数が入力される
#半角区切りでなくてもリストに入る
#複数行の入力をリストに入れる
for _ in range(q):
    query=[int(x) for x in input().split()]
    #[0, 10]
    #[0, 12]
    #このようにリストに入る
    cmd = query[0]
    #print(cmd)	
    #0
    #0
    #2
    #1
    #2
    if cmd==0:
        A.append(query[1])
    elif cmd==1:
        A.pop()#末尾を削除
    else:
        print(" ".join(map(str,A)))