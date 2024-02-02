# Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
# función acepta el número como argumento.


def factorial(numero):
    # Verificar si el número es 0 o 1 (el factorial es 1 para estos casos)
    if numero == 0 or numero == 1:
        return 1
    # Calcular el factorial para números mayores que 1
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado

# Ejemplo de uso
numero_ingresado = int(input("Ingrese un número para calcular su factorial: "))

# Llamar a la función y mostrar el resultado
resultado_factorial = factorial(numero_ingresado)
print(f"El factorial de {numero_ingresado} es {resultado_factorial}")
