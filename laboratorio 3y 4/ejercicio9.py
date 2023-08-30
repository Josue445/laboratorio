def cifrado_cesar(mensaje, desplazamiento):
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra.isalpha():
            codigo = ord(letra)
            if letra.isupper():
                codigo = (codigo - 65 + desplazamiento) % 26 + 65
            else:
                codigo = (codigo - 97 + desplazamiento) % 26 + 97
            letra_cifrada = chr(codigo)
            mensaje_cifrado += letra_cifrada
        else:
            mensaje_cifrado += letra
    return mensaje_cifrado

mensaje = "Estoy aprendiendo Python"
desplazamiento = 3

mensaje_cifrado = cifrado_cesar(mensaje, desplazamiento)

print("Mensaje cifrado:", mensaje_cifrado)
