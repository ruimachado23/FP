a1 = float(input('a1:'))

b1 = float(input('b1:'))

a2 = float(input('a2:'))

b2 = float(input('b2:'))


def intersects(a1,b1,a2,b2):
    if a1>b1 or a2>b2:
        print('Erro')
        exit()

    elif a1 > b2 or a2 > b1:
        return False
        
    else:
        return True

print(intersects(a1,b1,a2,b2))