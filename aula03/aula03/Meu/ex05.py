a = float (input ("a? "))
b = float (input ("b? "))


def max(a,b):

    if b < a:
        return a
          
    else:
        return b
        
print ("Máximo:", max(a,b))
