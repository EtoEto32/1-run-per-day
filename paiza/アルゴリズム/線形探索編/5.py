nums=list(map(int,input().split()))

minimum=nums[0]
maximum=nums[0]
for i in nums:
    if maximum<i:
        maximum=i
     
for i in nums:
    if minimum>i:
        minimum=i
        
        
print(maximum,minimum)
        
        
