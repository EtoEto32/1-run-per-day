N=int(input())

count=0
while(N != 0 and N%2==0):
    if N%2==0:
        N=N/2
        count+=1
print(count)

N = int(input())

div_count = 0
while True:
    if N % 2 == 0:
        N //= 2
        div_count += 1
    else:
        break

print(div_count)
#奇数の場合は、2で割り切れないので、breakでループを抜ける