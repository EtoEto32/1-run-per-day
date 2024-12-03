s = input()
st = set()
for ele in s:
    if ele not in st:
        st.add(ele)
        print(ele, end="")

# Pythonのjoinメソッドを使うと、リストの要素を文字列に連結することができます。
# 具体例を見てみましょう。

# リストの要素を文字列に連結する例
lst = ['Hello', 'World', '!']
result = ''.join(lst)
print(result)  # Output: HelloWorld!

# 文字列を特定の文字で連結する例
str_list = ['apple', 'banana', 'cherry']
result_str = ', '.join(str_list)
print(result_str)  # Output: apple, banana, cherry