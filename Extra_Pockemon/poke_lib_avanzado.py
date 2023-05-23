import json
import re

import poke_lib_int_avan as lib_int_avan

import poke_lib_elemental as lib_elemental


path = r'C:\\Users\\Denise\\Documents\\1 Cuatri\\Programacion_1\\Extra_Pockemon\\data_pokemones.json'
lista_pokemones = lib_elemental.pokedex_leer_archivo(path)


# 22.1
"""
Crear la función "tiene_al_menos_un_atributo" la cual recibira como primer parametro un diccionario
que representara a un pokemon y como segundo parámetro un string que representara el atributo a evaluar
(tipo, evoluciones, fortaleza, debilidad).
Retorno: True en caso de tener al menos un atributo en la lista seleccionada, False caso contrario.
"""
def tiene_al_menos_un_atributo(pokemon: dict, key: str) -> bool:
    """
    The function checks if a given dictionary has at least one attribute with a specified key, which is
    a list with at least one element.
    
    :param pokemon: a dictionary representing a Pokemon with various attributes
    :type pokemon: dict
    :param key: "evoluciones"
    :type key: str
    :return: The function `tiene_al_menos_un_atributo` is being called with arguments
    `lista_pokemones[0]` and `"evoluciones"`. The function checks if the key `"evoluciones"` exists in
    the dictionary `lista_pokemones[0]` and if its corresponding value is a list with at least one
    element. If both conditions are true,
    """
    if key in pokemon:
        if type(pokemon[key]) == list and len(pokemon[key]) >= 1:
            return True
    return False


# 22.2
"""
Crear la función "obtener_variedades_atributos" la cual recibira como primer parámetro un diccionario
que representara a un pokemon y como segundo parámetro un string que representara el atributo a evaluar
(tipo, evoluciones, fortaleza, debilidad).
Deberá iterar todos los pokemones y armar UN SET con todos las variedades de atributos según 
el segundo parámetro (todas las variedades de tipo o debilidades o fortalezas o evoluciones).
Tips:
    Reutilizar la funcion: -> "tiene_al_menos_un_atributo"
Retorno: Un set con la variedad única de atributos pasado por parámetro.
"""
def obtener_variedades_atributos(lista_pokemon: list[dict], key: str) -> set:
    """
    The function obtains a set of attributes from a list of dictionaries containing Pokemon data based
    on a specified key.
    
    :param lista_pokemon: a list of dictionaries representing different Pokemon and their attributes
    :type lista_pokemon: list[dict]
    :param key: The key parameter is a string that represents the attribute of the Pokemon that we want
    to obtain the varieties of. For example, if key is "types", the function will return a set of all
    the different types of Pokemon in the given list
    :type key: str
    :return: a set of attributes from the given key for all the Pokemon in the given list that have at
    least one attribute for that key.
    """
    atributos_set = set()
    for pokemon in lista_pokemon:
        if tiene_al_menos_un_atributo(pokemon, key):
            atributos = pokemon[key]
            atributos_set.update(atributos)
    return atributos_set



# 22.3
"""
Crear la función "obtener_dict_pokemones_agrupados_por_tipo" la cual recibira como primer parametro
un diccionario que representara a un pokemon y como segundo parámetro un string que
representara el atributo a evaluar (tipo, evoluciones, fortaleza, debilidad).
La función deberá iterar la variedad de atributos buscando en cada uno de los pokemones que posean ese atributo,
en caso de encontrar uno que cumpla la condición, tendrá que armar un diccionario donde la clave sea dicho atributo
y el valor será una lista donde tendrá que agregar el nombre de cada pokemon que tenga dicho atributo.
Ejemplo:
{"Volador": ["Charizard", "Articuno", "Zapdos", "Moltres"],
"Agua": ["Blastoise"],
"Fantasma": ["Gengar"]}
Tips:
    Reutilizar la funcion: -> "obtener_variedades_atributos", "obtener_nombre_pokemon" y "imprimir_mensaje"
    Mensaje: En caso de que alguna de las listas esté vacía, informar por consola.
Retorno: Un diccionario donde cada clave es una variedad de atributo del pokemon y
cada valor es una lista de nombres de los pokemones que tienen ese atributo.
"""
def obtener_dict_pokemones_agrupados_por_tipo(lista_pokemones: list[dict], key: str) -> dict:
    """
    This function groups a list of dictionaries containing Pokemon data by a specified attribute and
    returns a dictionary with the attribute values as keys and a list of Pokemon names as values.
    
    :param lista_pokemones: A list of dictionaries representing Pokemon data
    :type lista_pokemones: list[dict]
    :param key: The key parameter is a string that represents the attribute of the Pokemon dictionary
    that will be used to group the Pokemon by type. For example, if key is "type", the function will
    group the Pokemon by their type attribute
    :type key: str
    :return: a dictionary containing the Pokemon grouped by their type, where the keys are the different
    types and the values are lists of Pokemon names belonging to that type. If the input list is empty,
    the function returns an error message.
    """
    dict_atributo = {}
    if lista_pokemones:
        lista_copia = lista_pokemones.copy()
        lista_atributos = list(obtener_variedades_atributos(lista_copia, key))
        for atributo in lista_atributos:
            lista_nombres = []
            for pokemon in lista_copia:
                if key in pokemon and atributo in pokemon[key]:
                    lista_nombres.append(lib_elemental.obtener_nombre_pokemon(pokemon))
                dict_atributo[atributo.capitalize()] = lista_nombres
        lib_elemental.imprimir_mensaje(dict_atributo, "success")
        return dict_atributo
    else:
        return lib_elemental.imprimir_mensaje("Lista vacia", "error")
                
    




# 22.4
"""
Crear la función "formatear_lista_en_string" la cual recibira como primer parámetro
una lista de palabras y como segundo parámetro un string que será usado como separador
de palabras.
La función debe convertir la lista en un string de palabras, separadas por el segundo parámetro.
Retorno: Un string de palabras separadas con un string separador
"""
def formatear_lista_en_string(lista_palabras: list, separador: str) -> str:
    if lista_palabras:
        cadena_formateada = separador.join(lista_palabras)
    return cadena_formateada



# 22.5
"""
Crear la función "pokedex_clasificacion_por_tipos" la cual recibira como único parametro
la lista de pokemones.
La función debe pedir al usuario que ingrese 'TIPO' y mediante una expresión RegEx
verificar que coincida
Tips:
    Reutilizar la funcion: -> "obtener_dict_pokemones_agrupados_por_tipo", "imprimir_mensaje" y "formatear_lista_en_string"
    Mensaje: En caso de que alguna de las listas esté vacía, informar por consola.
    Mensaje: En caso de que no coincida el ingreso del usuario con lo que debe matchear, informar por consola.
Retorno: None.
"""

def pokedex_clasificacion_por_tipos(lista_pokemonnes: list[dict]) -> None:
    tipo = input("Ingrese un tipo: ")
    if lista_pokemones:
        pass

# 23.1
"""
Crear la función "obtener_atributos" la cual recibira como primer parámetro
un diccionario que representara a un pokemon,
como segundo parámetro el atributo a buscar (tipo, evoluciones, fortaleza o debilidad)
como tercer parámetro un string que será la separación usada para concatenar cada palabra
contenida en la lista de atributos buscada.
La función deberá obtener la lista de atributos elegida según el segundo parámetro.
iterar cada palabra capitalizandola y finalmente concatenandolas en un string
el cual tendrá un separador (3er parámetro) entre cada palabra.
Tips:
    Reutilizar la función: -> "capitalizar_palabras"
Retorno: Un string con los atributos concatenados y separados por el separador.
"""

def obtener_atributos(lista_pokemones:list[dict], key: str, separador: str) -> str:
    lista_atributos_segun_key = list(obtener_variedades_atributos(lista_pokemones, key))
    lista_capitalizada = []
    for atributo in lista_atributos_segun_key:
        atributo_capitalizado = lib_elemental.capitalizar_palabras(atributo)
        lista_capitalizada.append(atributo_capitalizado)
    return formatear_lista_en_string(lista_capitalizada, separador)

print(obtener_atributos(lista_pokemones, "tipo", ", "))



# 23.2
"""
Crear la función "pokedex_info_detallada_pokemones" la cual recibira
como único parámetro la lista de pokemones.
Deberá iterar la lista y crear un template con la información de cada uno de ellos.
Ejemplo de template:


Pokemon: #150 - Mewtwo                                                                            
Tiene Evoluciones: True                                                                            
Evoluciones: Mega-mewtwo X # Mega-mewtwo Y                                                        
Tipos: Psiquico                                                                                    
Fortalezas: Agua | Planta | Fuego | Eléctrico                                                      
Debilidades: Fantasma | Oscuridad                                                                  
_________________________________


Una vez realizado el template del pokemon iterado, imprimir por consola.


Tips:
    Reutilizar la función: -> "nombre_format_pokemon", "imprimir_mensaje", "obtener_atributos" y "tiene_al_menos_un_atributo"
    Mensaje: En caso que la lista esté vacía, informarlo por consola como un error.
Retorno: None.
"""
# 24.1
"""
Crear la función "es_de_tipo" la cual recibira como primer parámetro un diccionario que representara a un pokemon
y como segundo parámetro un string que representa un tipo (fuego, eléctrico, etc).
La función deberá verificar que el tipo ingresado por parámetro sea uno de los que el pokemon posea.
Retorno: True en caso de que el pokémon sea de ese tipo, False caso contrario.
"""
# 24.2
"""
Crear la función "obtener_pokemones_de_tipo" la cual recibe como primer parámetro la lista de pokemones 
y como segundo parámetro el tipo de pokemones a buscar (fuego, eléctrico, etc). La función deberá crear un diccionario con una clave que respete el formato: "pokemones_X" (donde X es el tipo ingresado por parámetro para buscar, fuego, eléctrico, etc). Como valor, la clave tendrá una lista con todos los pokemones que sean de ese tipo buscado.
Tips:
    Reutilizar la funcion: -> "es_de_tipo"
Retorno: Un diccionario de una única clave y una lista de pokemones como valor, acordes al tipo buscado.
"""
# 24.3
"""
Crear la función "guardar_archivo" la cual recibira como
primer parámetro la ruta completa del archivo a crear y como segundo parámetro un diccionario el cual usara para crear el JSON.
La función deberá crear un archivo JSON con el diccionario pasado por parámetro.
Retorno: True si pudo guardar el archivo, False caso contrario.
"""
# 24.4
"""
Crear la función "pokedex_pokemones_elegidos_por_tipo" la cual recibira como único parámetro la lista de pokemones.
La función deberá obtener toda la lista/set de tipos de pokemones para luego pedir por consola al usuario elegir uno de los posibles tipos a buscar (validándolo con RegEx y luego de que exista en la lista/set de tipos). Una vez validado deberá obtener la lista de pokémons que cumpla la condición de ser tener entre sus tipos (xq pueden tener más de uno) posea el que el usuario ingresó. Al tener dicha lista, volcarla a un archivo json.
Tips:
    Reutilizar la funcion: -> "obtener_variedades_atributos", "imprimir_mensaje", "guardar_archivo" y "obtener_pokemones_de_tipo"
    Mensaje: En caso de crear el archivo, informarlo por consola como un success (que se vea el nombre del archivo creado).
    Mensaje: En caso de que la lista esté vacía, informar por consola como un error.
    Mensaje: En caso de no matchear la búsqueda, informar por consola con un error.
Retorno: None.
"""

# 25.1
"""
Crear la función "ordenar_pokemones_por" la cual recibira como primer parámetro la lista de pokemones,
una clave para ordenar como segundo parámetro y un booleano como tercer parámetro que indicará si se ordena
de forma ascendente o descendente.
La función debe iterar la lista ordenando los pokemones según la clave pasada por parámetro de manera ascendente o descendente.
Al realizar un swap, deberá imprimir por consola el nombre de los dos pokemones que fueron intercambiados de lugar 
respetando el formato de mensaje:
"Pikachu fue intercambiado con Moltres". Finalmente deberá retornar la lista ordenada.
Tips:
    Reutilizar la función: -> "imprimir_mensaje"
Retorno: La lista de pokemones ordenada.
"""

# 25.2
"""
Crear la función "pokedex_ordenar_pokemones" la cual recibira como único parámetro la lista de pokemones.
La función deberá pedir al usuario la clave a ordenar (mostrando en el mensaje las opciones a elegir) y luego pedirle como quiere ordenarla (ASC o DESC). Validar ambos inputs con RegEx.
Al ordenar la lista, deberá guardarla en un archivo JSON con un nombre de formato, por ejemplo, "pokemones_ordenados_por_poder_ASC.json".
En caso de algún error, informar en consola con un mensaje.
Tips:
    Reutilizar la funcion: -> "ordenar_pokemones_por", "imprimir_mensaje" y "guardar_archivo".
    Mensaje: En caso de que la lista esté vacía, informar por consola como un error.
    Mensaje: En caso de que no haya match con la key a ordenar, informar por consola como un error.
    Mensaje: En caso de que no haya match con ASC o DESC, informar por consola con un error.
Retorno: None.
"""