def shorten():
    str = input ("Nome: ")
    u = ""
    for i in str:
        if i.isupper():
            u += i
    return u
print(shorten())