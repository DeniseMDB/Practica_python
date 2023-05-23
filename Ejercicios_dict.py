'''
Ejercicio 1
Crea un diccionario que represente los días de la semana,
donde las claves son los nombres de los días y los valores son los números correspondientes
(por ejemplo, {"lunes": 1, "martes": 2, ...}). Imprime el valor correspondiente al día "miércoles".
'''

dias_semana = {"lunes": 1, "martes": 2, "miercoles": 3, "jueves": 4, "viernes": 5,
                "sabado": 6, "domingo":7}

print(dias_semana["miercoles"])

'''
Ejercicio 2

Crea un diccionario que represente los meses del año,
donde las claves son los nombres de los meses y los valores son sus números correspondientes
(por ejemplo, {"enero": 1, "febrero": 2, ...}). Imprime el número correspondiente al mes "julio".
'''

dict_meses = {"enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5,
            "junio": 6, "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10,
            "noviembre": 11, "diciembre": 12 }

print("El mes de Julio corresponde a: ", dict_meses["julio"])

'''
Ejercicio 3
Crea un diccionario que contenga la información de una película,
como título, director y año de estreno. Luego, imprime el título de la película.
'''

pelicula = {"Titulo": "Titanic", "Director": "James Cameron", "Año": 1993}

print("El titulo de la pelicula es: ", pelicula["Titulo"])

'''
Ejercicio 4
Crea un diccionario que contenga la información de una dirección: nombre de la calle, altura, localidad,
código postal, partido y provincia. Luego, imprime el nombre de la calle, seguido de su altura.
'''

Direccion = {"Calle": "Malvinas Argentinas", "Altura": 1870, "Localidad": "Caballito",
            "Codigo postal": 1600, "Partido": "CABA", "Provincia": "Buenos Aires"}

print("El nombre de la calle es: {0} y la altura es: {1}".format(Direccion["Calle"], Direccion["Altura"]))

'''
Ejercicio 8
Crea un diccionario que represente las edades de varias personas, donde
las claves son los nombres de las personas y los valores son sus edades.
Imprime la edad de la persona más joven.
'''

dic_personas = {"Jose": 55, "Pedro": 62, "Bruno": 2, "Omar": 35}

mas_joven = 0

for edad in dic_personas.values():
    if mas_joven == 0 or mas_joven > edad:
        mas_joven = edad
    
print("La edad del mas joven es: ",mas_joven)

'''
Ejercicio 9
Crea un diccionario que contenga las capitales de los países de América del Sur.
Luego, pide al usuario que ingrese el nombre de un país y muestra su capital correspondiente.
'''
capitales_del_sur = {"Argentina": "Buenos Aires", "Brasil": "Brasilia", "Chile": "Santiago", "Peru": "Lima"}

valor = input("Ingresa el nombre de un pais: (Argentina/Chile/Peru/Brasil >> ").capitalize()

if valor in capitales_del_sur:
    print(capitales_del_sur[valor])
else: 
    print("Error")

'''
Ejercicio 10
Crea un diccionario que represente las notas de un examen de varios estudiantes,
donde las claves son los nombres de los estudiantes y los valores son sus notas.
Imprime el promedio de las notas.

'''

notas_estudiantes = {"Jose": 5, "Pedro": 6, "Bruno": 8, "Omar": 2, "Laura": 10}

suma_notas = 0
contador = 0
for notas in notas_estudiantes.values():
    suma_notas += notas
    contador += 1

promedio = suma_notas/contador

print("El promedio de notas es de: ", promedio)

'''
Ejercicio 11
Crea un diccionario que represente una lista de tareas por hacer.
Cada clave del diccionario debe ser el nombre de una tarea y cada valor debe ser su estado
(los estados son:  pendiente, en proceso, completada). Imprimir todas las tareas seguido de su estado
'''

tareas = {"platos": "pendiente", "ropa": "completada", "pisos": "en proceso", "ordenar": "pendiente"}

for tarea,estado in tareas.items():
    print(tarea,"|", estado)

