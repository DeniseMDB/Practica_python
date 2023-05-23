import json
import poke_lib_elemental  as lib_elemental

path = r'C:\\Users\\Denise\\Documents\\1 Cuatri\\Programacion_1\\Extra_Pockemon\\data_pokemones.json'
lista_pokemones = lib_elemental.pokedex_leer_archivo(path)

# * 10.1
# ```
# Crear la funcion "tiene_varios_atributo" la cual recibira como primer parametro un diccionario que representara a un solo pokemon,
# como segundo parámetro el nombre de la clave la cual deberá chequear que posea más de un elemento (ya que su valor es una lista).
# Retorna: En caso de tener más de un elemento, retornara true, false caso contrario.

def tiene_varios_atributos(pokemon: dict, key: str) -> bool:
    """
    The function checks if a given key in a dictionary has a list value with more than one element.
    
    :param pokemon: a dictionary representing a Pokemon, with various attributes as keys and their
    values as values
    :type pokemon: dict
    :param key: The key parameter is a string that represents the attribute we want to check in the
    pokemon dictionary
    :type key: str
    :return: a boolean value (True or False) depending on whether the given key exists in the dictionary
    and its corresponding value is a list with more than one element.
    """
    if key in pokemon:
        if type(pokemon[key]) == list and len(pokemon[key]) > 1:
            return True
    return False
# ```

# * 10.2
# ```
# Crear la función "podekex_pokemones_varios_atributo" la cual recibira como primer parámetro un diccionario que
#representara a un solo pokemon, como segundo parámetro el nombre de la clave a buscar.
# Al encontrar pokemones que posean más de un atributo (tipo, fuerza, evoluciones o debilidad) deberá imprimirlos.
# Ejemplo:
#     Pokemones con múltiples evoluciones:
#     #001 - Bulbasaur
#     #004 - Charmander
#     #006 - Charizard
#     #172 - Pichu
#     #025 - Pikachu
#     #150 - Mewtwo

def podekex_pokemones_varios_atributo(lista_pokemon: list[dict], key: str) -> None:
    """
    This function takes a list of dictionaries representing Pokemon and a key, and prints the names of
    the Pokemon that have multiple attributes for that key.
    
    :param lista_pokemon: a list of dictionaries representing different Pokemon, where each dictionary
    contains information about a single Pokemon such as its name, type, and stats
    :type lista_pokemon: list[dict]
    :param key: The "key" parameter is a string that represents the attribute/key that we want to check
    in each dictionary of the "lista_pokemon" parameter. This function is designed to check if each
    dictionary in the list has multiple attributes with the same key
    :type key: str
    """
    if lista_pokemon:
        for pokemon in lista_pokemon:
            if tiene_varios_atributos(pokemon, key):
                print(lib_elemental.nombre_format_pokemon(pokemon))
    else:
        lib_elemental.imprimir_mensaje("Lista vacia", "error")



# Tips:
#     Reutilizar las funciones: -> "tiene_varios_atributo", "imprimir_mensaje" y "nombre_format_pokemon"
#     Informar: En caso de no haber pokemones en la lista, se deberá imprimir un mensaje de error.
# Retorno: None
# ```
# * 11.1
# ```
# Crear la función "pokemones_atributo_y_cantidad" que recibira como primer parámetro la lista de pokemones y
#como segundo parámetro la clave a evaluar.
# La función deberá iterar los pokemones buscando los que posean más de un atributo (tipo, fuerza, evoluciones o debilidad).
# Al encontrarlos los agregará a una lista.
# Tips:
#     Reutilizar la función: -> "tiene_varios_atributo"
# Retorno: La lista de pokémons con más de un atributo (tipo, fuerza, evoluciones o debilidad)
# ```
def pokemones_atributo_y_cantidad(lista_pokemon: list [dict], key: str) -> list:
    """
    This function takes a list of dictionaries representing Pokemon and a key, and returns a list of
    Pokemon that have multiple values for the specified key.
    
    :param lista_pokemon: a list of dictionaries representing different Pokemon, where each dictionary
    contains information about a single Pokemon such as its name, type, and attributes
    :type lista_pokemon: list [dict]
    :param key: The "key" parameter is a string that represents the attribute of the Pokemon that we
    want to count or analyze. For example, if we want to count the number of Pokemon with the "fire"
    type, we would set the "key" parameter to "type" and then pass the value "
    :type key: str
    :return: a list of dictionaries that have multiple values for a given key. The function takes in a
    list of dictionaries representing Pokemon and a key as input, and returns a list of dictionaries
    that have multiple values for the given key.
    """
    lista_mas_atributos = []
    for pokemon in lista_pokemon:
        if tiene_varios_atributos(pokemon, key):
            lista_mas_atributos.append(pokemon)
    return lista_mas_atributos



# * 11.2
# ```
# Crear la función "imprimir_nombre_cantidad_atributo" que recibira como primer parámetro la lista de pokemones 
# y como segundo parámetro la clave a evaluar.
# Deberá extraer los datos necesarios para formatear un mensaje el cual tendrá los datos del pokémon,
#  la clave evaluada y la cantidad de elementos de la clave para luego imprimirlos en consola.
# Ejemplo:
#     #006 - Charizard Cantidad Evoluciones: 3
# Tips:
#     Reutilizar la función: -> "nombre_format_pokemon" e "imprimir_mensajes"
# Retorno: None
# ```

def imprimir_nombre_cantidad_atributo(lista_pokemon: list [dict], key: str) -> None:
    """
    This function takes a list of dictionaries representing Pokemon and a key, and prints the name of
    each Pokemon and the quantity of the specified attribute.
    
    :param lista_pokemon: A list of dictionaries representing different Pokemon and their attributes
    :type lista_pokemon: list [dict]
    :param key: The "key" parameter is a string that represents the attribute of the Pokemon that we
    want to count the quantity of. For example, if we want to count the number of moves a Pokemon has,
    "key" would be "moves"
    :type key: str
    """
    contador_cantidad = 0
    for pokemon in lista_pokemon:
        for valor in pokemon.values():
            if type(valor) == list:
                contador_cantidad = len(valor)
            else: 
                contador_cantidad = 1
            mensaje = "{0} Cantidad {1}: {2}".format(lib_elemental.nombre_format_pokemon(pokemon), key, contador_cantidad)
        lib_elemental.imprimir_mensaje(mensaje, "success")
            
#imprimir_nombre_cantidad_atributo(lista_pokemones, "evoluciones")
# * 11.3
# ```
# Crear la función "pokedex_pokemones_atributo_y_cantidad" que recibira como primer parámetro la lista de pokemones
#y como segundo parámetro la clave a evaluar.
# La función deberá obtener una lista de pokemones con más de un atributo para luego iterarla 
#e imprimir los datos de cada pokémon que posea más de un atributo.


# Tips:
#     Reutilizar las funciones: -> "pokemones_atributo_y_cantidad", "imprimir_nombre_cantidad_atributo" e "imprimir_mensaje"
#     Mensaje: En caso de que alguna de las listas esté vacía, informar por consola.
# Retorno: None
# 

def pokedex_pokemones_atributo_y_cantidad(lista_pokemon: list [dict], key: str) -> None:
    lista_pokemones_varios_atributos = []
    if lista_pokemon:
        lista_pokemones_varios_atributos = pokemones_atributo_y_cantidad(lista_pokemon, key).copy()
        imprimir_nombre_cantidad_atributo(lista_pokemones_varios_atributos, key)
    else:
        lib_elemental.imprimir_mensaje("Lista vacia", "error")

