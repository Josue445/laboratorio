def es_palindromo(frase):
    frase = frase.replace(" ", "").lower()
    frase = ''.join(c for c in frase if c.isalnum())

    return frase == frase[::-1]

frase = "Anita lava la tina"

if es_palindromo(frase):
    print("La frase es un palíndromo")
else:
    print("La frase no es un palíndromo")
