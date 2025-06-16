def pow(a, b):
    result = 1
    if b == 0:
        return 1
    elif b < 0:
        for _ in range(-b):
            result *= a
        return 1 / result
    else:
        for _ in range(b):
            result *= a
        return result
