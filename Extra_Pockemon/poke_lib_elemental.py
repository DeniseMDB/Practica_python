import json
import os


_b_red: str = '\033[41m'
_b_green: str = '\033[42m'
_b_blue: str = '\033[44m'
_f_white: str = '\033[37m'
_no_color: str = '\033[0m'


def imprimir_mensaje(mensaje: str, tipo_mensaje: str) -> None:
    """
    This function prints a message with a specified type (error, success, or info) in a colored format.
    :param mensaje: a string containing the message to be printed
    :param tipo_mensaje: The parameter "tipo_mensaje" is a string that represents the type of message
    that will be printed. It can be "Error", "Success", or "Info"
    """
    match tipo_mensaje.strip().capitalize():
        case 'Error':
            print(f'{_b_red}{_f_white}> Error: {mensaje}{_no_color}')
        case 'Success':
            print(f'{_b_green}{_f_white}> Success: {mensaje}{_no_color}')
        case 'Info':
            print(f'{_b_blue}{_f_white}> Information: {mensaje}{_no_color}')



def limpiar_consola() -> None:
    """
    This function clears the console screen and waits for user input to continue.
    """
    _ = input('Presione una tecla para continuar...')
    if os.name in ['ce', 'nt', 'dos']: os.system("cls")
    else: os.system("clear")


# * 01.0 - 
# ```
# Crear la función "pokedex_leer_archivo" la cual recibira como primer parámetro la ruta del archivo a leer (carpetas/nombre.extension)
#y como segundo parámetro la clave del diccionario el cual queremos traernos su valor (una lista)
# Retorno: La lista de diccionarios que representará pokemones.
# ```
def pokedex_leer_archivo(path: str, key: str = 'pokemones') -> list[dict]:
    """
    This function reads a JSON file and returns a list of dictionaries containing information about
    pokemons.
    
    :param path: The path parameter is a string that represents the file path of the JSON file that
    needs to be read
    :type path: str
    :param key: The "key" parameter is a string that specifies the key in the JSON file that contains
    the list of dictionaries representing the pokemons. By default, the value of "key" is set to
    'pokemones', defaults to pokemones
    :type key: str (optional)
    :return: a list of dictionaries containing information about pokemons. The specific key used to
    access the list of dictionaries is determined by the 'key' parameter, which defaults to 'pokemones'.
    """
    with open(path, 'r') as archivo:
        return json.load(archivo)[key]

# * 01.1 - 
# ```
# Crear la función "capitalizar_palabras" la cual recibira como parámetro un texto (que puede contener una o más palabras) y
#debe aplicar capitalización a cada palabra del mismo.
# Retorna: El mismo texto con todas las palabras con la primera letra mayúscula.

def capitalizar_palabras(texto: str) -> str:
    """
    The function capitalizes each word in a given string and returns the modified string.
    
    :param texto: a string that contains one or more words separated by spaces
    :type texto: str
    :return: a string with all the words in the input string capitalized. If the input string is empty,
    the function prints an error message and returns None.
    """
    if texto:
        palabras = texto.split() #crea una lista de palabras
        capitalizadas = [palabra.capitalize() for palabra in palabras] #crea una nueva lista donde cada palabra de la lista palabras se capitaliza
        return " ".join(capitalizadas) #junta cada palabra de la lista añadiendo un espacio
    return print("Error cadena de texto vacia")

# ```
# * 01.1.1 - 
# ```
# Crear la función "obtener_nombre_pokemon" la cual recibira por
# parámetro un diccionario que representará al pokemon, la función deberá obtener el nombre y retornarlo como un string.
# Tips:
#     Reutilizar la función: -> "capitalizar_palabras"
# Retorno: El nombre del pokemon, capitalizado

def obtener_nombre_pokemon(pokemon: dict):
    """
    This function takes a dictionary containing information about a Pokemon and returns the capitalized
    name of the Pokemon.
    
    :param pokemon: A dictionary containing information about a Pokemon, including its name
    :type pokemon: dict
    :return: the capitalized name of a Pokemon, which is obtained from a dictionary containing
    information about the Pokemon.
    """
    nombre_pokemon = pokemon["nombre"]
    nombre_capi = capitalizar_palabras(nombre_pokemon)
    return nombre_capi

# ```
# * 01.2
# ```
# Crear la funcion "pokedex_imprimir_nombre_pokemones" la cual recibira por
# parámetro una lista de pokemones e imprimirá sus nombres.
# Tips:
#     Reutilizar las funciones: -> "obtener_nombre_pokemon" e "imprimir_mensaje"
#     Informar: En caso de no haber pokemones en la lista, se deberá imprimir un mensaje de error.
# Retorno: None
# ```
def pokedex_imprimir_nombre_pokemones(lista_pokemones: list[dict]) -> str:
    """
    This function prints the names of the pokemons in a given list of dictionaries.
    
    :param lista_pokemones: a list of dictionaries representing Pokemon data, where each dictionary
    contains information such as the Pokemon's name, type, and stats
    :type lista_pokemones: list[dict]
    """
    if lista_pokemones:
        for pokemon in lista_pokemones:
            nombre_pokemon = obtener_nombre_pokemon(pokemon)
            imprimir_mensaje(nombre_pokemon, "Success")
    else:
        imprimir_mensaje("Lista Vacia", "Error")

path = r'C:\\Users\\Denise\\Documents\\1 Cuatri\\Programacion_1\\Extra_Pockemon\\data_pokemones.json'
lista_pokemones = pokedex_leer_archivo(path)
#pokedex_imprimir_nombre_pokemones(lista_pokemones)
# * 02.1
# ```
# Crear la función "tiene_id_par" la cual recibira por parámetro un diccionario que representará al pokemon y
#verificará que su id sea par.
# Retorno: True en caso de que sea par, caso contrario retornara False.
# ```
def tiene_id_par(pokemon: dict) -> bool:
    """
    The function checks if a given Pokemon dictionary has an even ID number.
    
    :param pokemon: A dictionary representing a Pokemon, with at least one key-value pair where the key
    is "id" and the value is an integer representing the Pokemon's ID number
    :type pokemon: dict
    :return: a boolean value (True or False) depending on whether the "id" value of the input dictionary
    "pokemon" is even or odd. If the "id" value is even, the function returns True, otherwise it returns
    False.
    """
    #pokemon_id = pokemon["id"]
    if pokemon["id"] % 2 == 0:
        return True
    return False


# * 02.2
# ```
# Crear la función "obtener_id_pokemon" la cual recibira por
# parámetro un diccionario que representará al pokemon, la función deberá obtener el id y retornarlo como un string.
# Retorno: El ID del pokémon como un string.
# ```
def obtener_id_pokemon(pokemon: dict) -> str:
    return str(pokemon["id"])


# * 02.3
# ```
# Crear la función "pokedex_imprimir_pokemon_id_par" la cual recibira por parámetro la lista de pokemones y
# deberá imprimir solo los que cumplan con la condición de tener un ID par.
# Tips:
#     Reutilizar las funciones: -> "tiene_id_par", "imprimir_mensaje" y "obtener_nombre_pokemon"
# Retorno: None
# ```
def pokedex_imprimir_pokemon_id_par(lista_pokemones: list[dict]) -> None:
    """
    This function prints the ID of each Pokemon in a list if it has an even ID, and prints an error
    message if it doesn't have an even ID.
    
    :param lista_pokemones: a list of dictionaries representing different pokemons, where each
    dictionary contains information about a single pokemon such as its name, type, and ID
    :type lista_pokemones: list[dict]
    """
    for pokemon in lista_pokemones:
        if tiene_id_par(pokemon):
            imprimir_mensaje(obtener_id_pokemon(pokemon), "Success")
        imprimir_mensaje("No tiene ID par", "Error")

# * 03.1
# ```
# Crear la función "id_multiplo_25" la cual recibira por parámetro un diccionario que
# representará al pokemon y verificará que su id múltiplo de 25.
# Retorno: True en caso de que sea múltiplo de 25, caso contrario retornara False.
# ```
def id_multiplo_25(pokemon: dict) -> bool:
    """
    The function checks if the ID of a given Pokemon is a multiple of 25.    
    :param pokemon: A dictionary representing a Pokemon, with the following keys:
    :type pokemon: dict
    :return: a boolean value (True or False) depending on whether the "id" value of the input dictionary
    is a multiple of 25 or not.
    """
    if pokemon["id"] % 25 == 0:
        return True
    return False



# * 03.2
# ```
# Crear la función "pokedex_imprimir_pokemon_id_mul_25" la cual recibira por parámetro la lista de pokemones 
#y deberá imprimir solo los que cumplan con la condición de tener un ID múltiplo de 25.
# Tips:
#     Reutilizar las funciones: -> "id_multiplo_25", "imprimir_mensaje" y "obtener_nombre_pokemon"
#     Informar: En caso de no haber pokemones en la lista, se deberá imprimir un mensaje de error.
# Retorno: None
def pokedex_imprimir_pokemon_id_mul_25(lista_pokemones: list[dict]) -> None:
    """
    This function prints the names of all the Pokemon in a given list whose ID is a multiple of 25.
    
    :param lista_pokemones: a list of dictionaries representing Pokemon data. Each dictionary should
    have keys for "id" (an integer), "name" (a string), and other attributes such as "type" or "stats"
    :type lista_pokemones: list[dict]
    """
    if lista_pokemones:
        for pokemon in lista_pokemones:
            if id_multiplo_25(pokemon):
                imprimir_mensaje(obtener_nombre_pokemon(pokemon), "Success")
    else:
        imprimir_mensaje("lista vacia", "Error")


# ```
# * 04.1
# ```
# Crear la funcion "nombre_format_pokemon" la cual recibira por
# parámetro un diccionario que representará al pokemon, la función deberá
# obtener el nombre y su ID y retornarlo como un string formateado
# respetando el estilo: #006 - Charizard
# Tips:
#     Reutilizar las funciones: -> "obtener_id_pokemon" y "obtener_nombre_pokemon"
# Retorno: El string formateado como pide el enunciado

def nombre_format_pokemon(pokemon: dict) -> str:
    """
    The function takes a dictionary representing a Pokemon and returns a formatted string with the
    Pokemon's ID and name.
    
    :param pokemon: A dictionary containing information about a Pokemon, including its ID and name
    :type pokemon: dict
    :return: a formatted string that includes the ID and name of a Pokemon. The ID and name are obtained
    from a dictionary that is passed as an argument to the function.
    """
    id_pokemon = obtener_id_pokemon(pokemon)
    nombre_pokemon =  obtener_nombre_pokemon(pokemon)
    return "#{0} - {1}".format(id_pokemon, nombre_pokemon)

# ```
# * 04.2
# ```
# Crear la funcion "pokedex_imprimir_nombres_poke_fmt" la cual recibira
# una lista de pokemones y deberá imprimirlos formateados respetando el estilo: #006 - Charizard
# Tips:
#     Reutilizar las funciones: -> "imprimir_mensaje" y "nombre_format_pokemon"
#     Informar: En caso de no haber pokemones en la lista, se deberá imprimir un mensaje de error.
# Retorno: None
def pokedex_imprimir_nombres_poke_fmt(lista_pokemones: list[dict]) -> None:
    """
    This function prints the names of the pokemons in a given list of dictionaries in a formatted way.
    
    :param lista_pokemones: a list of dictionaries representing Pokemon data, where each dictionary
    contains information such as the Pokemon's name, type, and stats
    :type lista_pokemones: list[dict]
    """
    if lista_pokemones:
        for pokemon in lista_pokemones:
            imprimir_mensaje(nombre_format_pokemon(pokemon), "Success")
    else:
        imprimir_mensaje("Lista vacia", "Error")


# ```
# * 05.1
# ```
# Crear la funcion "buscar_valor_pokemon_mas_fuerte" la cual recibira por parámetro la lista de pokemones 
# y un string el cual se utilizará para buscar un 'Maximo' o un 'Mínimo'.
# Según lo que reciba en el segundo parámetro se encargará de buscar el número más grande 
# o más pequeño de la clave 'poder' de cada pokemon. Una vez encontrada la retornara como un entero.
# En caso de no haber pokemones en la lista, se deberá imprimir un mensaje de error.
# Retorno: El valor mínimo o máximo de poder entre todos los pokémones.

def buscar_valor_pokemon_mas_fuerte(lista_pokemones: list[dict], modo: str) -> int:
    """
    This function takes a list of dictionaries representing pokemons and a mode (either "maximo" or
    "minimo") and returns the highest or lowest power value among the pokemons, respectively.
    
    :param lista_pokemones: A list of dictionaries representing different pokemons, where each
    dictionary contains information about a single pokemon such as its name, type, and power
    :type lista_pokemones: list[dict]
    :param modo: The "modo" parameter is a string that specifies whether the function should return the
    maximum or minimum value of the "poder" attribute in the list of dictionaries "lista_pokemones". If
    "modo" is "maximo", the function will return the highest value of "poder"
    :type modo: str
    :return: an integer value, which is the maximum or minimum power value of the pokemons in the given
    list, depending on the mode specified.
    """
    if lista_pokemones:
        min_max_poder = lista_pokemones[0]["poder"]
        for pokemon in lista_pokemones:
            if (modo == "maximo" and min_max_poder < pokemon["poder"]) or (modo == "minimo" and min_max_poder > pokemon["poder"]):
                min_max_poder = pokemon["poder"]
        return min_max_poder
    else:
        imprimir_mensaje("Lista vacia", "Error")


# ```
# * 05.2
# ```
# Crear la función "pokedex_pokemones_fuerza_max_min" la cual recibira por parámetro la lista de pokemones
#y un string el cual se utilizará para buscar un 'Maximo' o un 'Mínimo'.
# Primero buscará cuál es el valor Maximo o Mínimo (según el segundo parámetro)
# y una vez encontrado deberá iterar a los pokemones imprimiendo en consola los que
# cumplan la condición de tener ese mismo valor en su key 'poder'.
# Tips:
#     Reutilizar las funciones: -> "buscar_valor_pokemon_mas_fuerte" "imprimir_mensaje" y "nombre_format_pokemon"
#     Informar: En caso de no haber pokemones en la lista, se deberá imprimir un mensaje de error.
# Retorno: None
# ```
def pokedex_pokemones_fuerza_max_min(lista_pokemones: list[dict], modo: str) -> None:
    """
    This function takes a list of dictionaries representing pokemons and a mode (either "max" or "min")
    and prints the name of the pokemon with the highest or lowest power level, respectively.
    
    :param lista_pokemones: A list of dictionaries representing different Pokemon, where each dictionary
    contains information about a single Pokemon such as its name, type, and power
    :type lista_pokemones: list[dict]
    :param modo: The "modo" parameter is a string that determines whether the function should return the
    Pokemon with the highest or lowest "poder" (power) value. It can be either "max" or "min"
    :type modo: str
    """
    if lista_pokemones:
        min_max_fuerza = buscar_valor_pokemon_mas_fuerte(lista_pokemones, modo)
        for pokemon in lista_pokemones:
            if pokemon["poder"] == min_max_fuerza:
                imprimir_mensaje(nombre_format_pokemon(pokemon), "success")
    else:
        imprimir_mensaje("Lista vacia", "Error")




