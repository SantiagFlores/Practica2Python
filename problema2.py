# Escriba un programa en Python para construir el siguiente patrón.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# Número de filas en la parte superior del patrón
num_filas_superiores = 5

# Construir la parte superior del patrón
for i in range(1, num_filas_superiores + 1):
    print('* ' * i)

# Construir la parte inferior del patrón
for i in range(num_filas_superiores - 1, 0, -1):
    print('* ' * i)



