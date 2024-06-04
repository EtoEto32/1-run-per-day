import itertools
data=list(map(int, input().split()))
#4!にすることで後で計算が楽になる。
permutations=list(itertools.permutations(data, 4))
max_sum = 0
for perm in permutations:
    num1 = int(str(perm[0]) + str(perm[1]))
    num2 = int(str(perm[2]) + str(perm[3]))
    current_sum = num1 + num2
    if current_sum > max_sum:
        max_sum = current_sum
print(max_sum)
