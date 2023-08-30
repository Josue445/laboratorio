operaciones = [
    ("+", 8 + 6, ""),
    ("-", 8 - 6, ""),
    ("*", 8 * 6, ""),
    ("/", 8 / 6, "{:.2f}"),
    ("%", 8 % 6, ""),
    ("//", 8 // 6, ""),
    ("**", 8 ** 6, "")
]

for operacion in operaciones:
    simbolo, resultado, formato = operacion
    if formato:
        print(f"8 {simbolo} 6 = {formato.format(resultado)}")
    else:
        print(f"8 {simbolo} 6 = {resultado}")
