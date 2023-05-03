#Ejercicio 1

numero = input("Ingrese un numero: >>")
numero = int(numero)

if numero > 0 :
    print("El numero ingresado es positivo")
elif numero <= 0:
    print("El numero ingresado es cero o negativo")

#Ejercicio 2

edad = input("Ingrese su edad: >>")
edad = int(edad)

if edad > 18 :
    print("Eres mayor de edad")
elif edad < 18:
    print("Eres menor de edad")

#Ejercicio 3

numero = input("Ingrese un numero entero: >>")
numero = int(numero)

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

#Ejercicio 4

numero_uno = input("Ingrese un numero entero: >>")
numero_uno = int(numero_uno)

numero_dos = input("Ingrese un numero entero: >>")
numero_dos = int(numero_dos)

if numero_uno > numero_dos:
    print("El primer numero es mayor")
elif numero_uno < numero_dos:
    print("El segundo numero es mayor")
elif numero_uno == numero_dos:
    print("Los dos numeros son iguales")
else:
    print("Error")

#Ejercicio 5

nombre = input("Por favor ingresa tu nombre:>> ")
nombre = str.lower(nombre)

if nombre == "juan" or "maria" or "pedro":
    print("Hola {0}".format(nombre))
else:
    print("Hola desconocido")

#Ejercicio 6

nombre = input("Por favor ingresa tu nombre:>> ")
nombre = str.lower(nombre)

edad = input("Ingrese su edad: >>")
edad = int(edad)

if edad >= 18 and edad <=65 :
    print("Puedes votar")

else:
    print("No puedes votar")

#Ejercicio 7
#numero primo

#Ejercicio 8
#Cuadrado perfecto
numero = input("Ingrese un numero entero: >>")
numero = int(numero)

#Ejercicio 9

letra = input("Ingrese una letra:>> ")
letra = str.lower(letra)

if letra in ["a", "e", "i", "o", "u"]:
    print("La letra {0} es una vocal".format(letra))
else:
    "Es una consonante"

#Ejercicio 10

numero = input("Ingrese un numero entero: >>")
numero = int(numero)

if numero >0 and numero/2 == 0:
    print("El numero es positivo y par")
else:
    print("EL numero no cumple niguna condicion")

#Ejercicio 11

edad = input("Ingrese su edad: >>")
edad = int(edad)

if edad < 12:
    print("Eres un nino")
elif edad > 12 and edad < 17:
    print("Eres un adolescente")
elif edad > 18 and edad < 64:
    print("Eres un adulto")

#Ejercicio 12

numero_uno = input("Ingrese un numero entero: >>")
numero_uno = int(numero_uno)

numero_dos = input("Ingrese un numero entero: >>")
numero_dos = int(numero_dos)

if numero_uno > 0 :
    print("El primer numero ingresado es positivo")
if numero_dos > 0:
    print("El segundo numero es positivo")
elif numero_uno < 0  and numero_dos < 0 :
    print("Ambos numeros son negativo")

#Ejercicio 13






