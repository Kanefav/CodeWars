def sum_of_intervals(intervals):
    output = 0
    list = []
    for i in intervals:
        for num in range(i[0], i[1]):
            list.append(num)
            if list.count(num) > 1:
                pass
            else:
                output += 1
    return output


print(sum_of_intervals([(1, 4), (3, 5)]))