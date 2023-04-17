def med():
    tot = 0
    t = 0
    
    while True:
        n = input("Número: ")
        t += 1
        if n == "":
            break
        v = float(n)
        tot = tot + v
        m = tot / t
    return  m

print(med())
