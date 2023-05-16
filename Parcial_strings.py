#Escribir una función que reciba un string y devuelva el mismo string todo en mayúsculas.

def mayus (texto: str)-> str:
    texto = texto.upper()
    return texto

# Escribir una función que reciba un string y devuelva el mismo string todo en minúsculas.
def minus (texto: str)-> str:
    texto = texto.lower()
    return texto

#Escribir una función que tome dos strings y
#devuelva un nuevo string que contenga ambos strings concatenados, separados por un espacio.
def concatenar ( texto_uno: str, texto_dos: str)-> str:
    texto_tres = texto_uno + " " + texto_dos
    return texto_tres

#Escribir una función que tome un string y devuelva el número de caracteres que tiene el string.
def contar(texto: str)->int:
    cantidad = len(texto)
    return cantidad

#Escribir una función que tome un string y un carácter y devuelva
#el número de veces que aparece ese carácter en el string.
def buscar(texto: str, busqueda: str)->int:
    cantidad = texto.count(busqueda)
    return cantidad

#Escribir una función que tome un string y un carácter
#y devuelva una lista con todas las palabras en el string que contienen ese carácter.
def buscar_lista(texto: str, busqueda: str)->list:
    lista_caracter = []
    palabras_totales = texto.split()
    for palabra in palabras_totales:
        if busqueda in palabra:
            lista_caracter.append(palabra)

    return lista_caracter

#Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados
def eliminar_espacios(texto: str)->str:
    texto = texto.replace(" ", "")
    return texto

#Escribir una función que reciba dos string (nombre y apellido) y devuelva un diccionario con el nombre
#y apellido, eliminando los espacios del comienzo y el final y colocando la primer letra en mayúscula
def dict_nombre_apellido(nombre: str, apellido: str)-> dict:
    diccionario_nombre_apellido = {}
    nombre = nombre.strip()
    nombre = nombre.capitalize()
    apellido = apellido.strip()
    apellido = apellido.capitalize()
    diccionario_nombre_apellido["Nombre"] = nombre
    diccionario_nombre_apellido["Apellido"] = apellido
    return diccionario_nombre_apellido

#9. Escribir una función que tome una lista de nombres y los una en una sola 
#cadena separada por un salto de línea, por ejemplo:
# ["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".

def lista_a_string (lista: list)-> str:
    texto = "\n".join(lista)
    return texto

# 10. Escribir una función que tome un nombre y un apellido
#y devuelva un email en formato "inicial_nombre.apellido@utn-fra.com.ar".

def crear_mail(nombre: str, apellido: str)->str:
    nombre = nombre.replace(" ","")
    apellido = apellido.replace(" ","")
    inicial = nombre[0]
    mail = "{0}_{1}.{2}@utn-fra.com.ar".format(inicial,nombre,apellido)
    return mail

#11. Escribir una función que tome una lista de palabras y devuelva un string que contenga
#todas las palabras concatenadas con comas y "y" antes de la última palabra.
#Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"],
#el string resultante debería ser "manzanas, naranjas y bananas"..

def lista_unida (lista: list)-> str:
    #verificar lista vacia?
    str_palabras = ", ".join(lista[:-1])
    str_palabras = str_palabras + " y {0}".format(lista[-1])
    return str_palabras

#12. Escribir una función que tome un número de tarjeta de crédito como input,
#verificar que todos los caracteres sean numéricos y devolver los últimos cuatro dígitos
#y los primeros dígitos como asteriscos, por ejemplo: "**** **** **** 1234". 

def borrar_numeros()-> str:
    numero = input("Por favor ingrese el numero de la tarjeta:  ")
    numero = numero.replace(" ","")
    revisar = numero.isdigit()
    if revisar:
        ultimos_numeros = numero[-4:]
        numero_oculto = "**** " * 3
        numero_tarjeta = numero_oculto + ultimos_numeros
        return numero_tarjeta
    else:
        print("El numero ingresado no es correcto")

#13. Escribir una función que tome un correo electrónico
#y elimine cualquier carácter después del símbolo @, por ejemplo: "usuario@gmail.com" -> "usuario".

def limpiar_usuario(mail: str)-> str:
    usuario = mail.split("@")
    usuario = usuario[0]
    return usuario

#14. Escribir una función que tome una URL y devuelva solo el nombre de dominio,
#por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..

def limpiar_dominio(URL: str)-> str:
    dominio = URL.split(".")
    dominio = dominio[1]
    return dominio

#15. Escribir una función que tome una cadena de texto y devuelva solo los caracteres alfabéticos,
# eliminando cualquier número o símbolo (sólo son válidos letras y espacios),
#por ejemplo: "H0l4, m4nd0!" -> "Hl mnd”

def limpiar_numeros (texto: str)->str:
    caracteres_validos = []
    for caracter in texto:
        if caracter.isalpha() or caracter.isspace():
            caracteres_validos.append(caracter)
    texto_limpio = "".join(caracteres_validos)
    return texto_limpio

print(limpiar_numeros("H0l4, m4nd0!"))


#16. Escribir una función que tome una cadena de texto y la convierta en un acrónimo,
#tomando la primera letra de cada palabra, por ejemplo:
#"Universidad Tecnológica Nacional Facultad Regional Avellaneda" -> "UTNFRA”.

def crear_acronimo(texto: str)-> str:
    acronimo = ""
    lista_palabras = texto.split(" ")
    for palabra in lista_palabras:
        for letra in palabra:
            letra_inicial = palabra[0]
            acronimo += letra_inicial
            break
    return acronimo

#17. Escribir una función que tome un número binario y lo convierta en una cadena de 8 bits,
#rellenando con ceros a la izquierda si es necesario, por ejemplo: "101" -> "00000101".

def convertir_numero(numero: str)-> int:
    revisar = numero.isdigit()
    if revisar:
        if len(numero) < 8:
            numero_convertido = numero.zfill(8)
        else:
            numero_convertido = numero
    return numero_convertido

#18. Escribir una función que tome una cadena de caracteres y reemplace todas las letras
#mayúsculas por letras minúsculas y todas las letras minúsculas por letras mayúsculas,
#por ejemplo: "HoLa" -> "hOlA"
def convertir_mayus_minus(texto: str)-> str:
    cadena_convertida = ""
    for letra in texto:
        if letra.islower():
            letra = letra.lower()
            cadena_convertida += letra
        else:
            letra = letra.upper()
            cadena_convertida += letra
    return cadena_convertida

#19. Escribir una función que tome una cadena de caracteres y cuente
#la cantidad de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.
        
def contar_digitos (texto: str) -> str:
    contador_numeros = 0
    for caracter in texto:
        if caracter.isdigit():
            contador_numeros += 1
    print("El {0} contiene {1} digitos".format(texto, contador_numeros))


#20. Escribir una función que tome una lista de direcciones de correo electrónico y
#las una en una sola cadena separada por punto y coma,
#por ejemplo: ["juan@gmail.com", "maria@hotmail.com"] -> "juan@gmail.com;maria@hotmail.com".

def lista_cadena(lista: list)-> str:
    cadena_mails = ""
    cadena_mails = ";".join(lista)
    return cadena_mails

    



import os

def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')

