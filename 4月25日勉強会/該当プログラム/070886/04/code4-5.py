import glob
import shutil  # フォルダ操作
import os
print("aiueo")
# r=raw文字列　特殊な文字ではないという意思表示。

for orig_obj in glob.glob(r".\請求書\*.pdf"):
    # print(orig_obj)
    # print(os.path.split(orig_obj)[1])   #ファイル名のみを取得
    # print(os.path.split(orig_obj)[0])   #フォルダ名を取得
    # print(os.path.basename(orig_obj))   #拡張子を含むファイル名
    # print(os.path.splitext(os.path.basename(orig_obj)))
    # print(os.path.splitext(os.path.basename(orig_obj))[0])
    # print(os.path.splitext(os.path.basename(orig_obj))[0][-6:])  #後ろから6文字
    dest_dir = r".\請求書\\" + os.path.splitext(os.path.basename(orig_obj))[0][-6:]
    print(dest_dir)
    # print(os.path.exists(dest_dir))
    if os.path.exists(dest_dir):
        shutil.move(orig_obj, dest_dir)
    else:
        os.mkdir(dest_dir)
        shutil.move(orig_obj, dest_dir)
