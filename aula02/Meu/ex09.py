ctp = float (input ("Nota da CTP:"))
cp = float (input ("Nota da CP:"))

if (ctp or cp) < 6.5 :
    print ("Nota final: 66 (Reprovado por nota mínima) ")

    atpr = float (input("Nota da ATPR:"))
    apt = float (input("Nota da APT:"))

    nr = 0.3 * max(ctp, atpr) + 0.7 * max(cp, apt)

    print ("Nota final (por recurso)", nr)

else:
    nf = 0.3 * ctp + 0.7 * cp
    print ("Nota final", nf)
    