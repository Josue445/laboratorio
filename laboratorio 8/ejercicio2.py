import sys

# Obtener los argumentos de línea de comandos
args = sys.argv
print("Argumentos de línea de comandos:", args)

# Obtener la ruta de búsqueda de los módulos importados
module_paths = sys.path
print("Ruta de búsqueda de módulos:", module_paths)

# Escribir en la salida estándar
sys.stdout.write("Hola, mundo!\n")

# Leer desde la entrada estándar
nombre = input("Ingresa tu nombre: ")
print("Hola,", nombre)
