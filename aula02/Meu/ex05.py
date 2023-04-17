s = int(input ("Quantos segundos teve a chamada? "))

if s <= 60:
    print ("O valor da chamada é de 0.12€")

else:
    n = s - 60
    p = n * 0.002
    pf = p + 0.12
    print ("O valor da chamada é de", pf, "€")