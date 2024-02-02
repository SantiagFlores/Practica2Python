# Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
# ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
# números.
# Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
# números pares e impares.
# Ejemplo:
# “Desea ingresar un número?”: SI
# “Ingrese el número:” 5
# “¿Desea ingresar un número?”: SI
# “Ingrese el número: ” 7
#“Desea ingresar un número?”: NO
#Números ingresados: [ 5,7, 6, 7, 8, 9, 1, 2, 3, 4]
#Cantidad de números pares: 5
#Cantidad de números impares: 4

# Inicializar una lista para almacenar los números ingresados

numeros = []

# Bucle while para permitir al usuario ingresar números
while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()

    if respuesta != "SI":
        break

    numero = int(input("Ingrese el número: "))
    numeros.append(numero)

# Imprimir la lista de números ingresados
print("Números ingresados:", numeros)

# Contar la cantidad de números pares e impares
numeros_pares = sum(1 for num in numeros if num % 2 == 0)
numeros_impares = len(numeros) - numeros_pares

# Imprimir la cantidad de números pares e impares
print("Cantidad de números pares:", numeros_pares)
print("Cantidad de números impares:", numeros_impares)
