def primesUpTo():
    n = int(input("Enter the number: "))
    primes = []
    for i in range(2, n+1):
        if i in primes:
                continue
        else:
            primes.append(i)
        
            
