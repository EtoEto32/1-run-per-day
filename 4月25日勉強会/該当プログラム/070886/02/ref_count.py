import sys 

dict_a = {"a":123}

print(f"1.dict_a refcount : {sys.getrefcount(dict_a)}")
#変数dict_aとsys.getrefcount関数がこのオブジェクトを参照しているので、カウントは2になります。
dict_b = dict_a
print(f"2.dict_a refcount : {sys.getrefcount(dict_a)}")

#コピーした変数を削除
del dict_b
print(f"3.dict_a refcount : {sys.getrefcount(dict_a)}")