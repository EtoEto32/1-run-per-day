'''
    このプログラムは書面には不掲載
'''
import csv
import tracemalloc

tracemalloc.start()

with open("sample.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",")
    for line in reader:
        print(line)
        
snapshot = tracemalloc.take_snapshot()

top_stats = snapshot.statistics('lineno')

for stat in top_stats[:5]:
    print(stat)