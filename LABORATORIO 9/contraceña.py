import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''

    # Asegurar que la contraseña cumple con los requisitos de seguridad
    while True:
        contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
        if (any(c.islower() for c in contrasena) and
            any(c.isupper() for c in contrasena) and
            any(c.isdigit() for c in contrasena) and
            any(c in string.punctuation for c in contraseña)):
            break

    return contraseña


longitud = int(input("Ingrese la longitud deseada de la contraseña: "))


contraseña_segura = generar_contrasena(longitud)
print("La contraseña segura generada es:", contraseña_segura)
