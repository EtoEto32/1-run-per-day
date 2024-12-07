N = int(input())
li = []
sort_item = []
sort_count = []
for i in range(N):
    li.append(input())

set_to_li = set(li)
for j in set_to_li:
    sort_count.append(li.count(j))
sort_item = sorted(set_to_li)
for ans1, ans2 in sorted(zip(set_to_li, sort_count)):
    print(ans1, ans2)
