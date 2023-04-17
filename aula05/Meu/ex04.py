
def inputFloatList():
    list = []
    while True:
        n = input("Insira uma equipa: ")
        if n == "":
            break
        else:
            list.append(n)
    return list

def allMatches(list):
    matches = []
    for i in list:
        for x in list:
            if i != x:
                matches.append((i, x))
    return matches


print(allMatches(list))





    
