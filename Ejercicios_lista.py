'''
Ejercicio 1
Crea una lista con los números del 1 al 10 e imprime solo los números impares.
'''

lista_numeros = list(range(1,11))

for numero in lista_numeros:
    if numero % 2 != 0:
        print(numero)

'''
Ejercicio 2
Crea una lista con 5 números enteros. Luego solicita un nuevo número y 
reemplaza el tercer elemento de la lista por el número ingresado.
Finalmente imprime todos los números
'''

lista_numeros = [2, 4, 10, 15, 16]

numero_nuevo = input ("Ingrese un numero: >>")
numero_nuevo = int(numero_nuevo)

lista_numeros[2] = numero_nuevo

print(lista_numeros)

'''
Ejercicio 3

Crea una lista vacía y pide al usuario que ingrese números enteros hasta que
ingrese un número negativo. Luego, muestra la suma de todos los números ingresados.
'''

lista_numeros = []

flag = True

while flag:
    numero = input("Ingrese numeros, para deterse ingrese un numero negativo: >>>")
    numero = int(numero)
    if numero < 0:
        flag = False
    lista_numeros.append(numero)

suma_numeros = 0
for numero in lista_numeros:
    suma_numeros += numero

print("La suma de todos los numeros es: ",suma_numeros)

'''
Ejercicio 4
Crea una lista vacía y pide al usuario que ingrese una palabra.
Luego, muestra la primera letra de la palabra.
Repite este proceso hasta que el usuario ingrese una palabra que comience con la letra "z".
'''

lista_palabra = []

while True:
    palabra = input("Por favor ingrese una palabra: >> ")
    inicial = palabra[0]
    print(inicial)
    if inicial == "z":
        break

'''
Ejercicio 5
Crea una lista con los nombres de 5 ciudades y luego imprime el último elemento de la lista.
'''


lista_ciudades = ["bsas", "cordoba", "mendoza", "neuquen", "santiago"]

print(lista_ciudades[-1])

'''
Ejercicio 6
Crea una lista con 3 números enteros y luego agrega un nuevo número al final de la lista.
'''
print(lista_numeros)
lista_numeros = [62, 50, 15]

lista_numeros.append(input("ingrese un numero: >>"))

print(lista_numeros)

'''
Ejercicio 7
Crea una lista con los nombres de tus 3 deportes favoritos y
luego agrega otro deporte al final de la lista.
'''

lista_deportes = ["tennis", "basket", "futbol"]

deporte_extra = input("Ingrese un deporte: >> ")

lista_deportes.append(deporte_extra)

