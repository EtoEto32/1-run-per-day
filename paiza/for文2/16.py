# coding: utf-8
# Your code here!
N=int(input())
def factorial(N):
    result = 1
    for i in range(1, N + 1):
        result *= i
    return result

N=str(factorial(N))[::-1]

count=0

for i in N:
    if i=="0":
        count+=1
    else:
        break
print(count)

        
    
        



        
    
        


