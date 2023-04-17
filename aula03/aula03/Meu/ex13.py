a = float(input ("a? "))
b = float(input ("b? "))
    
def mdc(a,b):

    r = a % b
        
    if r == 0:
        return b
    else:
        return mdc(b,r)
    
print (mdc(a,b))
