def nilai(n):
    if (n >= 80) & (n <=100):
        return("Nilai A")
    elif (n >= 65) & (n <= 79):
        return("Nilai B+")
    elif (n >= 50) & (n <= 64):
        return("Nilai B")
    elif (n >= 35) & (n <= 49):
        return("Nilai C")
    elif (n >= 0) & (n <= 34):
        return("Nilai D. Mahasiswa dinyatakan tidak lulus.")
    else :
        return ("Input tidak valid")

if __name__ == '__main__':
    student_score = 80
    print(nilai(student_score))