def pangkat(base, pangkat):
    if pangkat == 0:
        return 1
    elif pangkat < 0:
        return 1 / pangkat(base, -pangkat)
    else:
        result = 1
        for _ in range(pangkat):
            result *= base
        return result

if __name__ == '__main__':
    print(pangkat(2, 3)) # 8
    print(pangkat(5, 3)) # 125
    print(pangkat(10, 2)) # 100
    print(pangkat(2, 5)) # 32
    print(pangkat(7, 3)) # 343