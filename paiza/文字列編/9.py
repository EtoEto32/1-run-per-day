S = input()
# paza
# i
# 2

# paiza
T = input()
N = int(input())
temp = S[:N]  # pa
temp += T  # pai
temp += S[N:]  # za
print(temp)  # paiza
# 文字列のスライスは0から始まる　[以上:未満]
# また、連結を使えばいい


s = input()
t = input()
n = int(input())
print(s[:n] + t + s[n:])#1行にまとめる
