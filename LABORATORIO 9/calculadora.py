def suma(num1, num2):
    return num1 + num2
def resta(num1, num2):
    return num1 - num2
def multiplicacion(num1, num2):
    return num1 * num2
def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        raise ValueError("No se puede dividir entre cero.")
def main():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        operacion = input("Ingrese la operación a realizar (+, -, *, /): ")
        if operacion == "+":
            resultado = suma(num1, num2)
            print(f"El resultado de la suma es: {resultado}")
        elif operacion == "-":
            resultado = resta(num1, num2)
            print(f"El resultado de la resta es: {resultado}")
        elif operacion == "*":
            resultado = multiplicacion(num1, num2)
            print(f"El resultado de la multiplicación es: {resultado}")
        elif operacion == "/":
            resultado = division(num1, num2)
            print(f"El resultado de la división es: {resultado}")
        else:
            print("Operación no válida.")
    except ValueError:
        print("Ha ocurrido un error. Asegúrese de ingresar números válidos.")

if __name__ == "__main__":
    main()
