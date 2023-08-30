import random
import string

def generar_contrasena_segura(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    while True:
        contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
        if (any(c.islower() for c in contrasena) and
            any(c.isupper() for c in contrasena) and
            any(c.isdigit() for c in contrasena) and
            any(c in string.punctuation for c in contrasena)):
            return contrasena

longitud_deseada = 12  # Puedes ajustar la longitud de la contraseña según tu preferencia
contrasena_segura = generar_contrasena_segura(longitud_deseada)
print("Contraseña segura generada:", contrasena_segura)