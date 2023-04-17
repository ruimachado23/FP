def g(x):
    a = 8 - x**3
    return a

def p(x):
    b = x**2 + 2*x + 3
    return b 

x = int(input('Enter x value for p(x): '))

def main():
    print("g(1) =", g(1))
    print("g(2) =", g(2))
    print("g(10) =", g(10))
    print(p(0))
    print(p(1))
    print(p(2))
    print(f(1))
    
if __name__ == '__main__':
    main()

