# Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
# pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
# materias.
# Puede usar el siguiente esquema a manera de ejemplo
# {
# Alumno: Juan,
# Notas: [10, 12, 15]
# }
# Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
# completo de los alumnos.





# Inicializar una lista para almacenar los datos de los alumnos
lista_alumnos = []

# Solicitar al usuario la cantidad de alumnos (n)
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

# Bucle para ingresar datos de cada alumno
for _ in range(cantidad_alumnos):
    nombre_alumno = input("Ingrese el nombre del alumno: ")

    # Inicializar una lista para almacenar las calificaciones del alumno
    calificaciones = []

    # Bucle para ingresar las 3 calificaciones del alumno
    for i in range(3):
        calificacion = float(input(f"Ingrese la calificación {i + 1} para {nombre_alumno}: "))
        calificaciones.append(calificacion)

    # Crear un diccionario con el nombre del alumno y sus calificaciones
    alumno = {"Alumno": nombre_alumno, "Notas": calificaciones}

    # Agregar el diccionario a la lista de alumnos
    lista_alumnos.append(alumno)

# Imprimir el listado completo de alumnos
print("\nListado completo de alumnos:")
for alumno in lista_alumnos:
    print(alumno)
