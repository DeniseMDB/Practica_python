import re
import json


def leer_archivo(path_completo: str) -> list[dict]:
    """
    Esta funcion lee un archivo Json y retorna una lista de diccionarios de heroes
    Recibe como parametro un string que representa el path del archivo a leer
    Retorna un diccionario que contiene una lista de diccionarios con informacion acerca de heroes
    """
    with open(path_completo, 'r') as archivo:
        # archivo_json = json.load(archivo)
        # archivo_dict = dict(archivo_json)
        # archivo_lista_dict = archivo_dict["heroes"]
        #return archivo_lista_dict
        return json.load(archivo)['heroes']


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
                print("El dato de altura del personaje {0} ha sido modificado".format(personaje["nombre"]))
                print("Datos normalizados")
            if type(personaje["peso"]) != float:
                personaje["peso"] = float(personaje["peso"])
                print("El dato de peso del personaje {0} ha sido modificado".format(personaje["nombre"]))
                print("Datos normalizados")
            if type(personaje["fuerza"]) != float:
                personaje["fuerza"] = float(personaje["fuerza"])
                print("El dato de fuerza del personaje {0} ha sido modificado".format(personaje["nombre"]))
                print("Datos normalizados")
        return lista
    else:
        print("Error: Lista de héroes vacía")


def validar_numero(respuesta: str, patron_regex: str)-> int:  #valida opcion numerica de menu
    if respuesta: #evalua si es vacio o no, false vacio
        if re.match(patron_regex, respuesta):
            return int(respuesta)
        return -1
    

def buscar_min_max(lista: list, key: str, modo: str)-> int: 
    """
    La función "buscar_min_max" devuelve el índice del valor mínimo o máximo en una lista de diccionarios,
    basándose en una clave especificada y en el modo de ordenamiento (ascendente o descendente).
    Recibe como parametros:
    Una lista de diccionarios, donde cada diccionario representa heroe.
    El parámetro "key" es una cadena que representa la clave del diccionario
    en la lista que se utilizará para comparar los valores.
    El parámetro "modo" es una cadena que especifica el orden de clasificación.
    Puede tomar dos valores: 'asc' para orden ascendente y 'desc' para orden descendente.
    Retorna un entero que representa el índice del elemento mínimo o máximo en la lista,
    dependiendo del valor del parámetro "modo". Si la lista está vacía, devuelve -1.
    """
    retorno = -1
    if lista:    #es igual que len(lista)>0
        i_min_max = 0
        for i in range(len(lista)):
            if ((modo == 'asc' and lista[i][key] < lista[i_min_max][key]) or
                (modo == 'desc' and lista[i][key] > lista[i_min_max][key])):
                i_min_max = i 
        retorno = i_min_max
    return retorno

def sort_pedido(lista: list, key: str = "altura", modo: str = "asc") -> list[dict]:          #
    """
    La función ordena una lista de diccionarios basándose en una key numerica
    y un modo especificado ascendente o descendente.
    Recibe como parametros:
    Una lista de diccionarios, donde cada diccionario representa un heroe en la lista y
    contiene información acerca de ese heroe.
    El parámetro "key" es una cadena que especifica la clave del diccionario cuyo valor se desea ordenar
    ejemplo altura, fuerza, peso etc
    El parámetro "modo" determina el orden de clasificación de la lista.
    Puede ser "asc" para orden ascendente o "desc" para orden descendente, por defecto es "asc".
    Retorna una copia ordenada de la lista de diccionarios de entrada,
    basada en la clave y el modo de ordenamiento especificados. El valor devuelto es una lista de diccionarios.
    """
    lista_copia = lista.copy()
    for i in range(len(lista_copia)):
        lista_aux = lista_copia[i:]
        indice_min_max = buscar_min_max(lista_aux, key, modo) + i #me busca sumando al indice
        lista_copia[i], lista_copia[indice_min_max] = lista_copia[indice_min_max], lista_copia[i]
    return lista_copia

def ordenar_por_altura(lista_heroes: list[dict]) -> list[dict]:
    """
    La funcion ordena por altura especificamente segun una lista de heroes
    Recibe por parametro una lista de heroes
    Retorna una lista de heroes ordenador de acuerdo a la altura
    ordenada de MENOR A MAYOR
    """
    return sort_pedido(lista_heroes)
    ...

def ordenar_por_peso(lista_heroes: list[dict]) -> list[dict]:
    """
    La funcion ordena por peso especificamente segun una lista de heroes
    Recibe por parametro una lista de heroes
    Retorna una lista de heroes ordenador de acuerdo al peso
    ordenada de MAYOR A MENOR
    """
    return sort_pedido(lista_heroes, "peso", "desc")
    ...

def ordenar_por_nombre(lista_heroes: list[dict]) -> list[dict]:
    """
    Crear una función llamada ‘ordenar_por_nombre’
    que reciba como parámetro la lista de héroes y la devuelva la lista de héroes ordenada por nombres de forma alfabética ascendente (de la A a la Z)
    """
    ...

def ordenar_por_largo_nombre(lista_heroes: list[dict]) -> list[dict]:
    """
    Crear una función llamada ‘ordenar_por_largo_nombre’
    que reciba como parámetro la lista de héroes y la devuelva la lista de héroes ordenada por el largo del nombre de forma descendente 
    """
    ...

def ordenar_por_key(lista_heroes: list[dict], key: str, ascendente=True) -> list[dict]:
    """
    La función deberá ordenar la lista de personajes según la key especificada.
    El sentido de ordenamiento lo determina el tercer parámetro, en caso de ser True el orden va a ser ascendente
    (de menor a mayor) y en el caso de ser False el sentido es descendente (mayor a menor)
    """
    ...


# lista_heroes = leer_archivo(r"C:\Users\Denise\Documents\1 Cuatri\Programacion_1\data_stark.json")
# print (lista_heroes)
# lista_normalizada = stark_normalizar_datos(lista_heroes)
# print(sort_pedido(lista_normalizada, "altura", "asc"))