n=int(input())
val=list(map(int,input().split()))

even=0#偶数の個数カウンター
odd=0#奇数の個数カウンター
for i in val:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even,odd)