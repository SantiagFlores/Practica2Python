# Escriba una función de Python que tome un número como parámetro y verifique que el número sea
# primo o no.

def es_primo(numero):
    # Verificar si el número es menor o igual a 1 (no es primo)
    if numero <= 1:
        return False
    # Verificar si el número es divisible por algún número del rango de 2 a la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    # Si no es divisible por ningún número, es primo
    return True

# Ejemplo de uso
numero_ingresado = int(input("Ingrese un número para verificar si es primo: "))

# Llamar a la función y mostrar el resultado
if es_primo(numero_ingresado):
    print(f"{numero_ingresado} es un número primo.")
else:
    print(f"{numero_ingresado} no es un número primo.")
