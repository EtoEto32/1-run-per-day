lst_a = [1,2,3,4,5,]
lst_b = lst_a

lst_b[0] = 10

print(f"lst_aは{lst_a}")
print(f"lst_bは{lst_b}")

print(id(lst_a))
print(id(lst_b))