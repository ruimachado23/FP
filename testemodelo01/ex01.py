# Calculadora de IMC
# Recebe o peso e a altura, calcula o IMC e imprime o resultado juntamente com a categoria
def main():
    peso = float(input("Digite o peso(kg): "))
    altura = float(input("Digite a altura(m): "))
    print("És ", IMC(peso,altura))

def IMC(peso, altura):
    imc = (peso / (altura**2))
    if imc < 18.5:
        c = "magro"
    elif imc >= 18.5 and imc < 25:
        c = "saudável"
    elif imc >= 25 and imc < 30:
        c = "forte"
    else:
        c = "obeso"
    return c
    
if __name__ == "__main__":
    main()