for i in range(1, 10):
	for j in range(1, 10):
		print(i * j, end=" ")
	print()

print("===========================================")
for i in range(1, 10):
    for j in range(1, 10):
        if j == 9:
            print(i * j)
        else:
            print(i * j, end=" ")