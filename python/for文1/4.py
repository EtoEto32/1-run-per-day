"""
import string
#アルファベットの大文字小文字の出力
print(string.ascii_letters)
#アルファベットの小文字のみの出力
print(string.ascii_lowercase)
#アルファベットの大文字のみの出力
print(string.ascii_uppercase)
#数値の文字列の出力
print(string.digits)
#16進数で扱う文字列の出力
print(string.hexdigits)
#８進法で扱う文字列の出力
print(string.octdigits)
#特殊文字列の出力
print(string.punctuation)
#上記で扱った文字列の出力
print(string.printable)
#スペースや改行など空白に関する文字列の出力
print(string.whitespace)"""

import string

for i in string.ascii_lowercase:
    print(i)