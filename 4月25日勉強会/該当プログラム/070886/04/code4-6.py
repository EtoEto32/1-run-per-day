import glob
import shutil
import os 


dir_files ={}

for orig_obj in glob.glob(r".\請求書\*.pdf"):
    print(os.path.splitext(os.path.basename(orig_obj))[0][-6:])  #後ろから6文字
    dest_dir = r".\請求書\\" + os.path.splitext(os.path.basename(orig_obj))[0][-6:]
    dir_files.setdefault(dest_dir,[])
    dir_files[dest_dir].append(orig_obj)

# print(dir_files)
#辞書からキーを取り出す
for dest_dir in dir_files.keys():
    print(dest_dir)
    os.mkdir(dest_dir)
    for orig_obj in dir_files[dest_dir]:
        print(orig_obj)
        shutil.move(orig_obj, dest_dir)