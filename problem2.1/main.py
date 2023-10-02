def faktor_bilangan(n):
    bil_faktor = []

    for i in range(1, n+1):
        if n % i == 0:
            bil_faktor.append(str(i))
    return '\n'.join(bil_faktor)

if __name__ == '__main__':
    print(faktor_bilangan(6))
    print(faktor_bilangan(20))