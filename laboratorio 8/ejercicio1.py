# Suponiendo que los datos están disponibles en el archivo countriesdata

# Datos de ejemplo
countriesdata = [
    {"País": "China", "Población": 1444216107, "Idioma": "Chino"},
    {"País": "India", "Población": 1393409038, "Idioma": "Hindi"},
    {"País": "Estados Unidos", "Población": 332915073, "Idioma": "Inglés"},
    # ... otros datos ...
]

# Función para obtener los idiomas más hablados en el mundo
def idiomas_mas_hablados(datos, n=10):
    idiomas = {}
    for dato in datos:
        idioma = dato["Idioma"]
        poblacion = dato["Población"]
        if idioma in idiomas:
            idiomas[idioma] += poblacion
        else:
            idiomas[idioma] = poblacion
    idiomas_ordenados = sorted(idiomas.items(), key=lambda x: x[1], reverse=True)
    return idiomas_ordenados[:n]

# Función para obtener los países más poblados en el mundo
def paises_mas_poblados(datos, n=10):
    paises_ordenados = sorted(datos, key=lambda x: x["Población"], reverse=True)
    return paises_ordenados[:n]

# Llamadas a las funciones
idiomas_top = idiomas_mas_hablados(countriesdata, n=10)
paises_top = paises_mas_poblados(countriesdata, n=10)

print("Idiomas más hablados en el mundo:")
for idioma, poblacion_total in idiomas_top:
    print(f"{idioma}: {poblacion_total}")

print("\nPaíses más poblados en el mundo:")
for pais in paises_top:
    print(f"{pais['País']}: {pais['Población']}")
