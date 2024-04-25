import csv
import tracemalloc

tracemalloc.start()

csv_file = open("sample.csv", "r", encoding="utf-8")    

reader = csv.reader(csv_file, delimiter=",")
for line in reader:
    pass

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

for stat in top_stats[:3]:
    print(stat)

print("<<< file close >>>")
csv_file.close()

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

for stat in top_stats[:3]:
    print(stat)