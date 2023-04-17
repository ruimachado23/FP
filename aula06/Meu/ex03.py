# Complete o programa!

# a)
def loadFile(fname, lst):
    with open(r'C:\Users\ruifa\OneDrive\Documentos\FP\aula06\school1.csv', 'r') as f:
        for line in f:
            if line[0].isnumeric():
                value_list = line.split('\t')
                value_list[0] = int(value_list[0])
                lst.append(tuple(value_list))
    return lst
# b) Crie a função notaFinal aqui...
def notaFinal(reg):
    nota1 = float(reg[-1])
    nota2 = float(reg[-2])
    nota3 = float(reg[-3])
    return (nota1 + nota2 + nota3) / 3

# c) Crie a função printPauta aqui...
def printPauta(lst):
    print("Número{:^100}Nota".format("Nome"))
    for reg in lst:
        print("{:>6}{:^100}{:4.1f}".format(reg[0], reg[1], notaFinal(reg)))

# d)
def main():
    lst = []
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)
    lst.sort()
    printPauta(lst)


# Call main function
if __name__ == "__main__":
    main()


