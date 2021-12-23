def double_every_other(lst):
    for item in range(len(lst)):
        if item % 2 != 0:
            lst[item] = lst[item] * 2
    return lst


print(double_every_other([1, 2, 4]))