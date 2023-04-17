n = int(input ("n?"))

def factorial(n):
    if n < 0:
        print ("ERROR!")
    
    elif n == 0 or n == 1:
        return "1"
    else:
        while n > 1:
            value = n * (n-1)
            n -=1
            return value

print(factorial(n))
    