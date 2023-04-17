n = int (input("Call a number: "))
list = []

def division(n):
    if n == 0:
        print("ERROR!") 
    else:  
        for i in range(1,n):
            if n % i == 0:
                print(i,"é divisor de", n) 
                list.append(i)
            value = sum(list)
    if value < n:
        print(n,"é um número deficiente")
    elif value == n:
        print(n,"é um número perfeito")
    else:
        print(n,"é um número abundante")

division(n)
