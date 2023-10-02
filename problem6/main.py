def cekdigit(n):
    while (n):
        dig = n % 10
        if (dig != 2 and
            dig != 3 and dig != 5
            and dig != 7):
            return False
        n = int((n / 10)-int(dig/10))
    return True

def prima(n):
    if (n == 1):
        return False
    i = 2
    while i * i <= n :
        if(n % i == 0):
            return False
        i = i + 1
    return True

def full_prima(n):
    return (cekdigit(n) and prima(n))

if __name__ == '__main__':
    print(full_prima(2)) # True
    print(full_prima(3)) # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # False
    print(full_prima(37)) # True
    print(full_prima(41)) # False
    print(full_prima(43)) # False
    print(full_prima(53)) # True