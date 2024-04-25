import csv

#sample.csvはutf-8, BOM付き
#csv_file = open("sample.csv", "r", encoding="utf-8")    
# csv_file1 = open("sample01.csv", "r", encoding="utf-8")    
csv_file1 = open("sample01.csv", "r", encoding="shift_jis")    

reader1 = csv.reader(csv_file1, delimiter=",")
for line in reader1:
        print(line)

# closeしなかったら
# csv_file.close()

csv_file2 = open("sample02.csv", "r", encoding="shift_jis")    

reader2 = csv.reader(csv_file2, delimiter=" ")
for line in reader2:
        print(line)