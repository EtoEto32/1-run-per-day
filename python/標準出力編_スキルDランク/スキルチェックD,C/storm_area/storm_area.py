"""
xc yc r_1 r_2
n
x_1 y_1
x_2 y_2
...
x_n y_n

"""
xc,yc,r_1,r_2=map(int,input().split())
n=int(input())
for i in range(n):
    nums=input().split()
    x=int(nums[0])
    y=int(nums[1])
    if ((r_1)**2<=(x-xc)**2+(y-yc)**2) and ((x-xc)**2+(y-yc)**2<=(r_2)**2):
        print("yes")
    else:
        print("no")