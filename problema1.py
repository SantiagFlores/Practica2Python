# Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
# en el rango de 1500 y 2700 (ambos incluidos)



# Inicializar una lista vacía para almacenar los resultados
resultados = []

# Iterar a través del rango de 1500 a 2700 (ambos incluidos)
for numero in range(1500, 2701):
    # Verificar si el número es divisible por 7 y múltiplo de 5
    if numero % 7 == 0 and numero % 5 == 0:
        # Agregar el número a la lista de resultados
        resultados.append(numero)

# Imprimir los números encontrados
print("Números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700:")
print(resultados)
