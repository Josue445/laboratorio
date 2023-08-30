edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

edades_ordenadas = sorted(edades)
edad_minima = min(edades_ordenadas)
edad_maxima = max(edades_ordenadas)
edades.append(edad_minima)
edades.append(edad_maxima)
import statistics
edad_mediana = statistics.median(edades)
import statistics
edad_promedio = statistics.mean(edades)
rango_edades = edad_maxima - edad_minima
valor_min_promedio = abs(edad_minima - edad_promedio)
valor_max_promedio = abs(edad_maxima - edad_promedio)
print("Edades ordenadas:", edades_ordenadas)
print("Edad mínima:", edad_minima)
print("Edad máxima:", edad_maxima)
print("Lista de edades actualizada:", edades)
print("Edad mediana:", edad_mediana)
print("Edad promedio:", edad_promedio)
print("Rango de las edades:", rango_edades)
print("Valor de (mínimo - promedio):", valor_min_promedio)
print("Valor de (máximo - promedio):", valor_max_promedio)
