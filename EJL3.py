#DEFINICION DE LAS FUNCIONES
def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multi(x, y):
    return x * y

def divi(x, y):
    return x / y

def cuadrado(x):
    return x * x

def cubo(x):
    return x * x * x

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

def potencia(x, y):
    return x ** y

def modulo(x, y):
    return x % y

def raiz(x):
    return x ** 0.5
#MENU DE OPCIONES 
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Divicion")
print("5. Cuadrado")
print("6. Cubo")
print("7. Factorial")
print("8. Potencia")
print("9. Modulo")
print("10. Raiz cuadrada")

opcion = int(input("Elige una opcion (1-10): "))

if opcion == 1:
    x = float(input("Ingresa el primer numero: "))
    y = float(input("Ingresa el segundo numero: "))
    print("El resultado es:", suma(x, y))
elif opcion == 2:
    x = float(input("Ingresa el primer numero: "))
    y = float(input("Ingresa el segundo numero: "))
    print("El resultado es:", resta(x, y))
elif opcion == 3:
    x = float(input("Ingresa el primer numero: "))
    y = float(input("Ingresa el segundo numero: "))
    print("El resultado es::", multi(x, y))
elif opcion == 4:
    x = float(input("Ingresa el primer numero: "))
    y = float(input("Ingresa el segundo numero: "))
    print("El resultado es:", divi(x, y))
elif opcion == 5:
    x = float(input("Ingresa un numero: "))
    print("El resultado es:", cuadrado(x))
elif opcion == 6:
    x = float(input("Ingresa un numero: "))
    print("El resultado es:", cubo(x))
elif opcion == 7:
    x = int(input("Ingresa un numero que no sea negativo: "))
    print("El resultado es:", factorial(x))
elif opcion == 8:
    x = float(input("Ingresa la base: "))
    y = float(input("Ingresa la potencia: "))
    print("El resultado es:", potencia(x, y))
elif opcion == 9:
    x = float(input("Ingresa el primer numero: "))
    y = float(input("Ingresa el segundo numero: "))
    print("El resultado es:", modulo(x, y))
elif opcion == 10:
    x = float(input("Ingresa un numero que no sea negativo: "))
    print("El resultado es:", raiz(x))
else:
    print("Opcion Invalida")