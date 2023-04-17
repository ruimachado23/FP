def fact():
    n = int (input("numero: "))
    fact = 1
    
    for i in range (1, n+1):
        fact *= i
    return fact

print (fact())
       



