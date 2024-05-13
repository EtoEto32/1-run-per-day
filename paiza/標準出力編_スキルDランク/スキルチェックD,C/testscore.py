N, M = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]

for i, (score, absences) in enumerate(students, start=1):
    final_score =max(0,score-absences*5)
    if final_score >= M:
        print(i)
