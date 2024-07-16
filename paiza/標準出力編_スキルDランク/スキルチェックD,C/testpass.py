N=int(input())
testpass=0
for _ in range(N):
    scores=list(map(str,input().split()))
    if scores[0]=="s":
        if int(scores[1])+int(scores[2])+int(scores[3])+int(scores[4])+int(scores[5])>=350:
            if (int(scores[2])+int(scores[3]))>=160:
                testpass+=1
    else:
        if int(scores[1])+int(scores[2])+int(scores[3])+int(scores[4])+int(scores[5])>=350:
            if (int(scores[4])+int(scores[5]))>=160:
                testpass+=1
print(testpass)