N = int(input())
score = 0
different_times = 0
correct = []
your_ans = []
for i in range(N):
    words = input().split()
    correct.append(words[0])
    your_ans.append(words[1])
for cor, you in zip(correct, your_ans):
    if len(cor) == len(you):  # 文字の長さが同じ
        for temp1, temp2 in zip(cor, you):
            if temp1 != temp2:
                different_times += 1
        if different_times >= 2:
            score += 0
        elif different_times == 1:
            score += 1
        else:
            score += 2
        different_times = 0
    else:  # 文字の長さが違う
        score += 0
print(score)
