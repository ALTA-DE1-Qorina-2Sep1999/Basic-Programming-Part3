def palindrome(s):
    return s == s[::-1]

if palindrome:
    print("True.")
else:
    print("False.")

if __name__ == '__main__':
    print(palindrome("civic")) # True
    print(palindrome("katak")) # True
    print(palindrome("kasur rusak")) # True
    print(palindrome("kupu-kupu")) # False
    print(palindrome("lion")) # False