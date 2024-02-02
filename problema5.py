# Problema 5:
# Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
# Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
# Ejemplo:
# Número ingresado: 15789000 y Dígito: 0
# Cantidad de veces 0 en el número: 4

def contar_digitos(numero, digito):
    # Convertir el número a cadena para facilitar la manipulación de los dígitos
    numero_str = str(numero)

    # Inicializar contador de ocurrencias
    contador = 0

    # Iterar sobre cada dígito en el número
    for d in numero_str:
        # Verificar si el dígito actual es igual al dígito proporcionado
        if d == str(digito):
            contador += 1

    return contador

# Ejemplo de uso
numero_ingresado = 15789000
digito_solicitado = 0

# Llamar a la función y mostrar el resultado
cantidad_ocurrencias = contar_digitos(numero_ingresado, digito_solicitado)
print(f"Número ingresado: {numero_ingresado} y Dígito: {digito_solicitado}")
print(f"Cantidad de veces {digito_solicitado} en el número: {cantidad_ocurrencias}")
