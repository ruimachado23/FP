n = 1

def isPrime(n):
    div = 0
    for i in range(1,n):
        if n % i == 0:
            div += 1
            if div > 1:
                break
    if div > 1:
        print(n,"não é primo.")
    else:
        print(n,"é primo.")
    
while n <= 100:
    isPrime(n)
    n += 1

