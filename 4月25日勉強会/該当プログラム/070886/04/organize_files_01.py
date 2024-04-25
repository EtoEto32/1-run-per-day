import glob
import shutil
import os
from collections import defaultdict

dir_files = defaultdict(list)  # リストを初期値

for orig_obj in glob.glob(r".\請求書\*.pdf"):
    dest_dir = r".\請求書\\" + os.path.splitext(os.path.basename(orig_obj))[0][-6:]
    dir_files[dest_dir].append(orig_obj)

for dest_dir in dir_files.keys():
    os.mkdir(dest_dir)
    for orig_obj in dir_files[dest_dir]:
        shutil.move(orig_obj, dest_dir)
