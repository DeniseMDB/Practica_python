'''
Ejercicio 1
Dada una lista de números, imprimir el número más grande de la lista.
'''

lista_numeros = [1,2,3,4,5,6,7,8,9,0]
numero_mayor = lista_numeros[0]

for numero in lista_numeros:
    if numero_mayor < numero:
        numero_mayor = numero

print("El mayor numero de la lista es: ", numero_mayor)

'''
Ejercicio 2
Dada una lista de palabras, imprimir la palabra más larga de la lista.
'''

lista_palabras = ["hola", "chau", "adios", "bienvenido", "esternocleidomastoideo"]

palabra_larga = lista_palabras[0]

for palabra in lista_palabras:
    if len(palabra_larga) < len(palabra):
        palabra_larga = palabra

print("La palabra mas larga de la lista es: {0} y contiene {1} letras".format(palabra_larga, len(palabra_larga)))

'''
Ejercicio 3
Dado un número entero n, imprimir la secuencia de números pares menores o iguales a n.
'''
n = 26
print("Numeros pares menores o iguales a {0} : ".format(n))
for i in range(n+1):
    if i % 2 == 0:
        print(i)



'''
Ejercicio 4
Dado un número entero n, imprimir la suma de los números impares menores o iguales a n.
'''

n = input("Ingrese un numero entero: >> ")
n = int(n)
suma = 0
for i in range(n+1):
    if i % 2 != 0:
        suma += i
print("La suma de numeros impares menores o iguales a {0}: es de {1} ".format(n,suma))


'''
Ejercicio 5
Dada una lista de números, imprimir el número más pequeño de la lista.
'''


lista_numeros = [1,2,3,4,5,6,7,8,9,0]
numero_menor = lista_numeros[0]

for numero in lista_numeros:
    if numero_menor > numero:
        numero_menor = numero

print("El menor numero de la lista es: ", numero_menor)

'''
Ejercicio 6
Dada una lista de palabras, imprimir la cantidad total de vocales en la lista.

'''

lista_palabras = ["hola", "chau", "adios", "bienvenido", "esternocleidomastoideo"]

contador = 0
for palabra in lista_palabras:
    for letra in palabra:
        if letra in ["a", "e", "i", "o", "u"]:
            contador += 1
    
print("La cantidad de vocales en la lista es de: ", contador)

'''
Ejercicio 7
Dado un número entero n, imprimir la secuencia de números impares menores o iguales a n.
'''

n = input("Ingrese un numero entero: >> ")
n = int(n)
print("Numeros impares menores o iguales a {0}: ".format(n))
for i in range(n+1):
    if i % 2 != 0:
        print(i)


'''
Ejercicio 8
Dado un número entero n, imprimir la suma de los números pares menores o iguales a n.
'''

n = input("Ingrese un numero entero: >> ")
n = int(n)
suma = 0
for i in range(n+1):
    if i % 2 == 0:
        suma += i
print("La suma de numeros pares menores o iguales a {0}: es de {1} ".format(n,suma))

'''
Ejercicio 9
Dada una lista de números, imprimir la cantidad de números negativos en la lista.
'''

lista_numeros = [1,2,3,4,5,6,7,8,9,0, -1, -10, -13]
contador = 0

for numero in lista_numeros:
    if numero < 0:
        contador += 1

print ("La cantidad de numeros negativos es: ", contador)

'''
Ejercicio 10
Dada una lista de palabras, imprimir las palabras que comienzan y terminan con la misma letra.
'''

'''
Ejercicio 11
Dado un número entero n, imprimir la secuencia de números primos menores o iguales a n.
'''

'''
Ejercicio 16
Dada una lista de palabras, imprimir las palabras que tienen una letra específica.

'''
lista_palabras = ["hola", "chau", "adios", "bienvenido", "esternocleidomastoideo"]

for palabra in lista_palabras:
    for letra in palabra:
        if "s" in palabra:
            print(palabra)
            break
        else:
            break

'''
Ejercicio 18
Dada una lista de números,
imprimir la suma de los números en la lista que son mayores que el promedio de la lista.
'''

lista_numeros = [1, 5, 8, 14, 30, 120, 4, 25]

contador = 0
suma_numero = 0
for numero in lista_numeros:
    suma_numero += numero
    contador += 1

promedio = suma_numero / contador
suma_numero_mayor = 0
for numero in lista_numeros:
    if numero > promedio:
        suma_numero_mayor += numero

print("La suma de los numeros mayores al promedio es: >> {0}, siendo el promedio: {1}".format(suma_numero_mayor, promedio))