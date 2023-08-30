def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    try:
        temperatura = float(input("Ingrese una temperatura: "))
        unidad = input("Ingrese la unidad de temperatura (C o F): ")

        if unidad.upper() == "C":
            resultado = celsius_a_fahrenheit(temperatura)
            print(f"{temperatura} grados Celsius equivalen a {resultado} grados Fahrenheit.")
        elif unidad.upper() == "F":
            resultado = fahrenheit_a_celsius(temperatura)
            print(f"{temperatura} grados Fahrenheit equivalen a {resultado} grados Celsius.")
        else:
            print("La unidad de temperatura ingresada es incorrecta.")

    except ValueError:
        print("Ha ocurrido un error. Asegúrese de ingresar una temperatura válida.")

if __name__ == "__main__":
    main()
