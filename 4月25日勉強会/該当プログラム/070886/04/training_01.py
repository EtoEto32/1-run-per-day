import glob
print(glob.glob(r".\請求書\*.pdf"))

# import shutil
# shutil.move(r".\請求書\アルキテック202311.pdf", r".\請求書\202311")

# import shutil
# shutil.copy(r".\請求書\アルキテック202311.pdf", r".\請求書\202311")

import os
print(os.stat(r".\請求書\アルキテック202311.pdf"))
print(os.path.abspath(r".\請求書\アルキテック202311.pdf"))
print(os.path.dirname(r".\請求書\アルキテック202311.pdf"))
print(os.path.basename(r".\請求書\アルキテック202311.pdf"))
print(os.path.split(r".\請求書\アルキテック202311.pdf"))
# print(os.path.split(r"C:\Users\ユーザー名\Documents\Python脱初心者本\prg\04\請求書\アルキテック202311.pdf"))
print(os.path.splitext(r".\請求書\アルキテック202311.pdf"))
# print(os.path.splitdrive(r"C:\Users\ユーザー名\Documents\Python脱初心者本\prg\04\請求書\アルキテック202311.pdf"))
print(os.path.getsize(r".\請求書\アルキテック202311.pdf"))