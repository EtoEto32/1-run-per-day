B=int(input())

answer=1
found=False
for i in range(1,B+1):
  if i**i>B:
    break
  elif i**i==B:
    found=True
    answer=i
    print(answer)
    break
if not found:
  print(-1)
#B問題だからそんな難しくない、普通にゴリ押し全探索だけは辞めとけよみたいな感じだった。
