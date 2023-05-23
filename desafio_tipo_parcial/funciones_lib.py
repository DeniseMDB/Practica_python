import json
import re

def leer_archivo(path: str)-> list[dict]:
    with open(path, 'r') as archivo:
        return json.load(archivo)['heroes']

# PATH_ARCHIVO = r"C:\\Users\\Denise\\Documents\\1 Cuatri\\Programacion_1\\data_stark.json"



# lista_heroes =  leer_archivo(PATH_ARCHIVO)


def validar_numero(respuesta: str, patron: str) -> int:
    if respuesta:
        if re.match(patron, respuesta):
            return int(respuesta)
        return -1
    

def validar_lista(lista_heroes: list[dict], respuesta: int) -> list[dict]:
    if lista_heroes:
        if respuesta <= len(lista_heroes):
            print("Cantidad correcta")
            return respuesta
        print("Cantidad incorrecta, hay {0} heroes en la lista".format(len(lista_heroes)))
        return len(lista_heroes)
    

def validar_respuesta(respuesta: str, patron: str) -> str:
    if respuesta:
        if re.match(patron, respuesta):
            return respuesta
        return -1



def stark_normalizar_datos(lista: list):
    """
    Esta función normaliza los datos de una lista de personajes convirtiendo sus valores de altura, peso y fuerza a flotantes.
    Recibe una lista de diccionarios que representan personajes con sus atributos como nombre, altura, peso y fuerza
    Retorna la lista de diccionarios con los datos normalizados
    """
    if len(lista) > 0:
        for personaje in lista:
            if type(personaje["altura"]) != float:
                personaje["altura"] = float(personaje["altura"])
            if type(personaje["peso"]) != float:
                personaje["peso"] = float(personaje["peso"])
            if type(personaje["fuerza"]) != float:
                personaje["fuerza"] = int(personaje["fuerza"])
        return lista
    else:
        print("Error: Lista de héroes vacía")

def mostrar_lista(lista_heroes: list[dict], key: str)-> list:
    lista_final = []
    if lista_heroes:
        print("\n")
        for element in lista_heroes:
            if key in element.keys():
                mensaje = f'Nombre: {element["nombre"]} | Identidad: {element["identidad"]} | {key.capitalize()}: {element[key]}'
                lista_final.append(mensaje)
                print(mensaje)
    return lista_final



def indice_min_max(lista_heroes: list[dict], key: str, modo: str) -> int:
    """
    La función devuelve el índice del valor mínimo o máximo en una
    lista de diccionarios según una clave y modo de ordenamiento especificados.
    Recibe: una lista de diccionarios que representan héroes
    El parámetro "key" es una cadena que representa la clave del diccionario en la lista
    de héroes que se utilizará para determinar el valor mínimo o máximo.
    El parámetro "modo" es una cadena que especifica el modo de operación para la función.
    Puede tomar dos valores: "asc" o "desc". Si se pasa "asc",
    la función encontrará el índice del diccionario en la lista con el valor más alto para la clave dada.
    Si se pasa "desc", la función encontrará el índice del diccionario con el valor más bajo para la clave dada.
    Retorna un entero que representa el índice del diccionario en la lista de entrada 
    """
    if lista_heroes:
        i_max_min = 0
        for i in range(len(lista_heroes)):
            if(modo =="asc" and (lista_heroes[i][key] > lista_heroes[i_max_min][key])):
                i_max_min = i
            elif(modo == "desc" and (lista_heroes[i][key] < lista_heroes[i_max_min][key])):
                i_max_min = i
    return i_max_min

def sort_asc_desc(lista_heroes: list, key: str, modo: str)->list:
    """
    La función ordena una lista de héroes en orden ascendente o descendente según una clave especificada.
    Recibe una lista de diccionarios que representan héroes, donde cada diccionario contiene información sobre un héroe como nombre, poder y edad.
    El parámetro "key" es una cadena que representa el atributo del objeto héroe que se utilizará para ordenar la lista.
    "modo" es un parámetro de cadena que determina el modo de ordenamiento.
    Puede tener dos posibles valores: "asc" para orden ascendente o "desc" para orden descendente.
    Retorna una lista ordenada de héroes basada en la clave y el modo especificados.
    """
    lista_copia = lista_heroes.copy()
    for i in range(len(lista_heroes)):
        lista_aux = lista_copia[i:]
        i_min_max = indice_min_max(lista_aux, key, modo) + i
        lista_copia[i], lista_copia[i_min_max] = lista_copia[i_min_max], lista_copia[i]
    return lista_copia

def calcular_promedio(lista_heroes: list[dict], key: str) -> float:
    '''
    Recibe lista de heroes con la key cuyo promedio se quiere calcular
    Calcula el promedio
    Devuelve el promedio
    '''
    suma_key = 0
    for heroe in lista_heroes:
        suma_key += heroe[key]
    promedio = suma_key / len(lista_heroes)
    promedio = round(promedio, 2)
    return promedio

def comparar_mayor_menor(lista: list, key: str, modo: str)->list:
    '''
    recibe lista de heroes con la key a comparar
    hace el promedio
    devuelve lista de mayores a promedio y menores
    ''' 
    lista_copia = lista.copy()
    promedio = calcular_promedio(lista_copia, key)
    promedio = round(promedio, 2)
    lista_final = []
    for elemento in lista_copia:
        if((modo == "mayor") and (elemento[key] > promedio)):
            lista_final.append(elemento.copy())
        elif(modo == "menor" and elemento[key] < promedio):
            lista_final.append(elemento.copy())
    return lista_final


def buscar(lista: list, key: str, modo: str)-> list[dict]:
    """
    La función recibe como entrada una lista de diccionarios, una clave y un modo.
    Busca el modo en la clave "inteligencia" de cada diccionario y devuelve una lista de cadenas que contienen el nombre,
    la identidad y el valor de la clave especificada para cada diccionario coincidente.
    Recibe una lista de diccionarios que contienen información sobre diferentes personajes,
    la key en la que deseamos buscar y el modo que representa lo que estamos buscando en la key.
    Retorna una lista de cadenas, donde cada cadena contiene el nombre,
    la identidad y el valor de la clave especificada para cada diccionario en la lista de entrada que coincida con el modo especificado.
    """
    lista_copia = lista.copy()
    lista_final = []
    print("\n")
    for elemento in lista_copia:
        if(re.search(modo,elemento["inteligencia"],re.IGNORECASE)):
            mensaje = f'Nombre: {elemento["nombre"]} | Identidad: {elemento["identidad"]} | {key.capitalize()}: {elemento[key]}'
            lista_final.append(mensaje)
            print(mensaje)
    return lista_final

#lista_archivo = buscar(lista_heroes, "inteligencia", "good")

def exportar_csv(lista: list,key: str):
    mensaje = ""
    nombre_archivo = "C:\\Users\\Denise\\Documents\\1 Cuatri\\Programacion_1\\desafio_tipo_parcial\\lista_ordenada_{0}.csv".format(key)
    with open(nombre_archivo, 'w') as archivo:
        #for elemento in lista:
        mensaje = "\n".join(lista)
        archivo.writelines(mensaje)

#exportar_csv(lista_archivo, "inteligencia")