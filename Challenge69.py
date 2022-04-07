def last_digit(n1, n2):
    lastN1Digit = str(n1)[-1]
    cycle = []
    power = 0
    while True:
        power += 1
        number = int(lastN1Digit) ** power
        number = str(number)[-1]
        number = int(number)
        if cycle.count(number) == 0:
            cycle.append(number)
        else:
            break
    cycles = n2%(power-1)
    cycles = str(cycles)[-1]
    cycles = int(cycles)
    print(cycle, cycles)
    return cycle[cycles-1]


print(last_digit(42, 9))