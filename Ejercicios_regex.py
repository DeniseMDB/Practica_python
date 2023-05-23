import re
#1- Crear una función llamada es_mayuscula que reciba un string y
#devuelva True en caso de que todas las letras sean mayúsculas o False en el caso contrario

def es_mayuscula(texto: str)->None:
    condicion = re.match("^[A-Z\s]+$", texto) is not None #se agrega el is not None para transformarlo en booleano
    return condicion                        #se sumo el  \s para que tome en cuenta los espacios ademas de las mayus 

#2- Crear una función llamada es_minuscula que reciba un string
#y devuelva True en caso de que todas las letras sean mayúsculas o False en el caso contrario

def es_minuscula(texto: str)->None:
    condicion = re.match("^[a-z\s]+$", texto) is not None
    return condicion

#3- Crear una función llamada es_entero que reciba un string 
#y devuelva True en caso de que se trate de un número entero y False en caso contrario.

def es_entero(texto: str):
    condicion = re.match("^[0-9]+$", texto) is not None
    return condicion

#4- Crear una función llamada es_solo_texto que reciba un string 
#y devuelva True en caso de que trate solo de caracteres alfabéticos 
#y el espacio y False en el caso contrario

def es_solo_texto(texto: str):
    condicion = re.match("^[a-zA-Z\s]+$", texto) is not None
    return condicion

#5- Crear una función llamada es_decimal
'''
Crear una función llamada es_decimal que
reciba dos strings: el primero representa la expresión a evaluar y
el segundo el separador decimal (puede ser punto . o coma ,).
Debe devolver True en caso que se trate de un número decimal y False en el caso contrario.
'''

def es_decimal(expresion: str, separador: str):
    regex = r'^[0-9]+([' + separador + r'][0-9]+)$'
    condicion = re.match(regex, expresion)
    if condicion:
        return True
    else:
        return False
    
#6 - Crear una función llamada es_alfanumerico
'''
Crear una función llamada es_alfanumerico que devuelva True en caso de tratarse de 
solo letras y números y False en el caso contrario (es decir que contenga caracteres especiales)
'''

def es_alfanumerico(texto: str):
    condicion = re.match("^[a-zA-Z0-9\s]+$", texto) is not None #esta bien?
    return condicion

#7 - Crear una función llamada es_binario que devuelva
# True en caso de un número binario válido (solo ceros y unos) o False en el caso contrario

def es_binario(texto: str):
    condicion = re.match("^[01]+$", texto) is not None
    return condicion

# 8 - Crear una función que reciba una lista de palabras 
# y devuelva otra lista con las palabras  que comienzan con la letra ‘U’

def lista_u(lista: list)-> list:
    lista_palabras_u = []
    for palabra in lista:
        palabras_u = re.findall(r"^U\w+", palabra) #la w para decir que le siguen mas caracteres despues
        if palabras_u:
            lista_palabras_u.append(palabras_u)
    return lista_palabras_u

# 9 - Crear una función que reciba un texto y
#devuelva una lista con las palabras que contienen entre 3 y 6 caracteres de largo


def lista_palabras_largas(texto: str)-> list:
    patron_regex = r'\b\w{3,6}\b'
    palabras = re.findall(patron_regex, texto)
    return palabras
print(lista_palabras_largas("Hola si que no"))
