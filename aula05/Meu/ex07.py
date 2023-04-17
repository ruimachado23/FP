s = input("Nome: ")

def is_palindrome(s):
    f = str(s)
    return s == s[::-1]

print(is_palindrome(s))
