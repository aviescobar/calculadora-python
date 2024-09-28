# Calculadora en Python

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def calculadora():
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    opcion = input("Elige una opción (1/2/3/4): ")

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if opcion == '1':
        print(f"{num1} + {num2} = {suma(num1, num2)}")
    elif opcion == '2':
        print(f"{num1} - {num2} = {resta(num1, num2)}")
    elif opcion == '3':
        print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")
    elif opcion == '4':
        print(f"{num1} / {num2} = {division(num1, num2)}")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    calculadora()
