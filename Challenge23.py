def is_prime(num):
    verf = 0
    if num <= 1: return False
    if num == 2: return True
    if num % 2 == 0: return False
    for number in range(1, 99999, 2):
        if num % number == 0:
            verf += 1
    if num > 99999:
        verf += 1
    if verf == 2:
        return True
    return False


print(is_prime(6))