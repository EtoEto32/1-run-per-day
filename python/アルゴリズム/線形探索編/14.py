N=int(input())

result=[]
for i in range(N):
    Nums=list(map(int,input().split()))
    result.append(Nums)
x_s,x_t=map(int,input().split())
y_s,y_t=map(int,input().split())
count=0
for i in  result:
    if (x_s <= i[0] <=x_t) and (y_s <= i[1] <=y_t):
        count+=1
print(count)

        