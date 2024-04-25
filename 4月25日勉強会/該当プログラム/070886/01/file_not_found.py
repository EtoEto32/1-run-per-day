#FileNotFoundError
# with open("sample_01.txt","r") as  f: 
#     #一行ずつ読み込む
#     line = f.readline()
#     while line:
#         print(line,end="")
#         line = f.readline()

filename = "sample_01.txt"
try:
    with open(filename,"r") as  f: 
        #一行ずつ読み込む
        line = f.readline()
        while line:
            print(line,end="")
            line = f.readline()
except FileNotFoundError:
    print(filename + "が存在しません")
