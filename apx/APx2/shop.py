def loadDataBase(fname, produtos):
    with open(fname, "r") as f:
        listaProdutos = [line.strip().split(";") for line in f][1:]     #Cada palavra de cada linha é guardada numa lista, sendo que a primeira linha é ignorada
        for produto in listaProdutos:
            produtos[produto[0]] = (produto[1], produto[2], float(produto[3]), float(produto[4].replace("%",""))/100)   #Cada linha é guardada como uma tuplo, sendo que o último elemento é convertido para float e dividido por 100 para obter a taxa
        return produtos 
    
    

def registaCompra(produtos):
    dic = {}

    while True:
        answer = input('Code? ')
        arguments = answer.strip().split(' ')
        code = arguments[0]
        
        if answer == "": break      #Se o utilizador não inserir nenhum input, o ciclo é quebrado

        if len(arguments) > 1:
            amount = float(arguments[1])
        else:
            amount = 1      #Por default, o amount é 1
            
        if code in produtos.keys():
            nome, seccao, preco, taxa = produtos[code]      #Como o objeto secção não é utilizado, é subtituído por um underscore
            if code in dic.keys():    
                dic[code] += amount     #Se a key já existir, o amount é incrementado
            else:
                dic[code] = amount 
            print("{:s} {:d} {:.2f}".format(nome, int(amount), (preco + preco*taxa)*amount))
    return dic



def fatura(produtos, compra):
    totalBruto = 0
    totalIVA = 0
    totalLiquido = 0
    produtosSeccao = {}

    for code, amount in compra.items():
        nome, seccao, preco, taxa = produtos[code]    

        precoFinal = (preco + preco * taxa) * amount

        totalBruto += preco * amount
        totalIVA += preco * taxa * amount
        totalLiquido += precoFinal
    
        if seccao not in produtosSeccao.keys():
            produtosSeccao[seccao] = []     #Caso não exista a seccao, é criada uma nova, vazia

        produtosSeccao[seccao].append((amount, nome, int(taxa*100), precoFinal))


    for seccao, lst in produtosSeccao.items():
        print(seccao)
        for prod in lst:
            amount, nome, taxa, precoFinal = prod
            print("{:4d} {:<27s} ({:2d}%) {:11.2f}".format(int(amount), nome, taxa, precoFinal))        #print devidamente formantada

    print("{:>26}Total Bruto: {:>11.2f}".format('',totalBruto))
    print("{:>28}Total IVA: {:>11.2f}".format('',totalIVA))     #print do total bruto, IVA e líquido, formatado à direita
    print("{:>24}Total Liquido: {:>11.2f}".format('', totalLiquido))
 
    

def main(args):
    # produtos guarda a informação da base de dados numa forma conveniente.
    produtos = {'p1': ('Ketchup.', 'Mercearia Salgado', 1.59, 0.23)}
    # Carregar base de dados principal
    loadDataBase("produtos.txt", produtos)
    # Juntar bases de dados opcionais (Não altere)
    for arg in args:
        loadDataBase(arg, produtos)
    
    # Use este código para mostrar o menu e ler a opção repetidamente
    MENU = "(C)ompra (F)atura (S)air ? "
    repetir = True
    faturas = []
    while repetir:
        # Utilizador introduz a opção com uma letra minúscula ou maiúscula
        op = input(MENU).upper()
        # Processar opção
        if op == "C":
            # Esta opção regista os produtos de uma compra
            compra = registaCompra(produtos)
            faturas.append(compra)
            # Aqui pode acrescentar a compra a uma estrutura de dados adequada...
        # Acrescente outras opções aqui...
        elif op == "F":
            n_compra = int(input('Numero compra? '))
            fatura(produtos, faturas[n_compra-1])     #A contagem começa em zero

        elif op == "S":
            repetir = False
            
    print("Obrigado!")


# Não altere este código / Do not change this code
import sys
if __name__ == "__main__":
    main(sys.argv[1:])
        
