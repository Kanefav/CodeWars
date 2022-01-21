def move_zeros(array):
    zeros = array.count(0)
    locate = 0
    if zeros >= 1:
        for zero in range(0, zeros):
            locate = array.index(0)
            array.pop(locate)
        for zero in range(0, zeros):
            array.append(0)
    return array


print(move_zeros([0, 1, 2, 3, 0]))