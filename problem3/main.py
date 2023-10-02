def prime_number(num):
    num_int = int(num)
    if num_int > 1:
        for i in range(2, int(num_int/2)+1):
            if (num_int % i) == 0:
                return 'Not Prime'
        else:
            return 'Prime'
    else:
        return 'Not Prime'

if __name__ == '__main__':
    print(prime_number(11)) # "Prime"
    print(prime_number(13)) # "Prime"
    print(prime_number(17)) # "Prime"
    print(prime_number(20)) # "Not Prime"
    print(prime_number(35)) # "Not Prime"