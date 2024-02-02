def omitir_vocales(cadena):
    # Crear una cadena sin vocales
    cadena_sin_vocales = ''.join(caracter for caracter in cadena if caracter.lower() not in {'a', 'e', 'i', 'o', 'u'})
    return cadena_sin_vocales

# Ejemplo de uso
texto_ingresado = input("Ingrese una cadena de texto: ")
resultado = omitir_vocales(texto_ingresado)
print(f"Resultado: {resultado}")
