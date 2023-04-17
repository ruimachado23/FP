a = float (input ("a? "))
b = float (input ("b? "))
c = float (input ("c? "))


def max2(a,b):

    if b < a:
        return a
          
    else:
        return b

def max3(a,b,c):
    if max2(a,b) < c:
        return c

    else:
        return max2(a,b)


print ("Máximo:", max3(a,b,c))
