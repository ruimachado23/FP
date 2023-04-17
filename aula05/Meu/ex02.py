def inputFloatList():
    list = []
    while True:
        n = input("Call a number: ")
        if n == "":
            break
        else:
            n1 = int(n)
            list.append(n1)
    return list

def countLower(list,v):  
    men = []
    for i in list:
        if i < v:
            men.append(i)
    return men

def minmax(list):
    minm = list[0]
    maxm = list[0]
    for i in list:
        if minm < i:
            minm = i
        elif maxm > i:
            maxm = i
    return maxm, minm

def media():
    lista = inputFloatList()
    avg = (minmax(lista)[0] + minmax(lista)[1]) / 2
    menor1 = countLower(lista, avg)

    print(f'A média do minímo e máximo é {avg}')
    print(f'Os números {menor1} são inferiores à media')


media()