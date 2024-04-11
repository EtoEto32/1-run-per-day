n,m=map(int,input().split())

a,b,c=map(int,input().split())
#a=1店舗当たりの建築費用　b=1店舗あたりの毎月の人件費を表す整数B
#c=ラーメン一杯当たり利益
ans=0
for i in range(n):
    s=int(input())
    if (s*c-a)-(b*m)<0:
        ans+=1
print(ans)
        