lista_1 = list(range(1, 11))
lista_2 = list(range(5, 16))
lista_3 = list(range(10, 21))

conjunto_1 = set(lista_1)
conjunto_2 = set(lista_2)
conjunto_3 = set(lista_3)

print("Conjunto 1:", conjunto_1)
print("Conjunto 2:", conjunto_2)
print("Conjunto 3:", conjunto_3)
conjunto_comun = conjunto_1.intersection(conjunto_2, conjunto_3)

print("Conjunto de números presentes en las tres listas:", conjunto_comun)
conjunto_total = conjunto_1.union(conjunto_2, conjunto_3)

print("Conjunto de números presentes en al menos una lista:", conjunto_total)
conjunto_diferencia = conjunto_1.difference(conjunto_3)

print("Conjunto de números presentes en la primera lista pero no en la última:", conjunto_diferencia)
tupla_comun = tuple(conjunto_comun)
tupla_total = tuple(conjunto_total)
tupla_diferencia = tuple(conjunto_diferencia)

suma_primer_ultimo_comun = tupla_comun[0] + tupla_comun[-1]
suma_primer_ultimo_total = tupla_total[0] + tupla_total[-1]
suma_primer_ultimo_diferencia = tupla_diferencia[0] + tupla_diferencia[-1]

print(suma_primer_ultimo_comun)
print(suma_primer_ultimo_total)
print(suma_primer_ultimo_diferencia)
