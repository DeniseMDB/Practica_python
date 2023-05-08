'''
Ejercicio 1
Dado un número entero n, imprimir todos los números desde n hasta 1 en orden descendente.
'''

n = input("Por favor ingrese un numero entero: >>")
n = int(n)

while n > 0:
    print(n)
    n = n - 1

'''
Ejercicio 2
Dado un número entero n, imprimir todos los números desde 1 hasta n en orden ascendente.

'''
n = input("Por favor ingrese un numero entero: >>")
n = int(n)
numero = 1
while n > 0 and numero <= n:
    print(numero)
    numero = numero + 1
    
'''
Ejercicio 3
Dada una cadena de texto, imprimir cada uno de los caracteres en la cadena.
'''
texto = "esternocleidomastoideo"
i = 0

while i < len(texto):
    print(texto[i])
    i += 1

'''
Ejercicio 4
Dada una lista de números, imprimir la suma de todos los elementos de la lista.
'''
lista_numeros = [1, 5, 8, 14, 30, 120, 4, 25]

i = 0

while i < len(lista_numeros):
    print(lista_numeros[i])
    i += 1

'''
Ejercicio 5
Dado un número entero n, imprimir si el número es primo o no.
'''

n = input("Ingrese un numero y le dire si es un numero primo: >> ")
n = int(n)

es_primo = True
numeros = 2
while numeros < n:
    if n % numeros == 0:
        es_primo = False
        break
    numeros += 1
if es_primo:    
    print("El numero {0} es primo".format(n))
else:
    print("El numero {0} no es primo".format(n))

'''
Ejercicio 6 
Dado un número entero n, imprimir la suma de todos los números pares menores o iguales a n.
'''