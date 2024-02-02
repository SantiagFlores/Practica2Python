# Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
# Nota: La secuencia de Fibonacci es la serie de números:
# 0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
# Cada número siguiente se obtiene sumando los dos números anteriores

# Inicializar los primeros dos números de la serie de Fibonacci
fibonacci = [0, 1]

# Generar la serie de Fibonacci hasta el número 50
while fibonacci[-1] + fibonacci[-2] <= 50:
    siguiente_numero = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(siguiente_numero)

# Imprimir la serie de Fibonacci
print("Serie de Fibonacci hasta el número 50:")
print(fibonacci)
