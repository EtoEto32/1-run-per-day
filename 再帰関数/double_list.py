def double_list(lst):
    if lst == []:
        return []

    first = lst[0]
    rest = lst[1:]
    return [first * 2] + double_list(rest)

print(double_list([1, 2, 3]))    # [2, 4, 6]
print(double_list([4, 5, 6]))    # [8, 10, 12]
