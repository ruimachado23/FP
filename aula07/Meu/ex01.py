with open('pg3333.txt', 'r', encoding="utf-8") as text:
    letras = {}
    for linha in text:
        for char in linha:
            if char.isalpha():
                char = char.lower()
                if char not in letras:
                    letras[char] = 1
                else:
                    letras[char] += 1

for letra in sorted(letras):
    print(letra, letras[letra])