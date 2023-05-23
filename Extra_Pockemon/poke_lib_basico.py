import poke_lib_elemental  as lib_elemental

# * 07.1
# ```
# Crear la función "buscar_promedio_segun_atributo" la cual recibira por parámetro la lista de pokemones como primer parámetro,
# el nombre de la clave en la cual buscará un valor específico como segundo parámetro y
#como tercer parámetro el valor a buscar que debe buscar en la key.
# Al encontrar el/los pokemones que tengan dicho valor en la key,
# deberá calcular el promedio de "poder" entre todos los pokemones que cumplan la condición.
# Retorno: El promedio como float
def buscar_promedio_segun_atributo(lista_pokemones: list[dict], key: str, valor: str) -> float:
    """
    This function calculates the average "poder" attribute value of all the pokemons in a given list
    that have a specific key-value pair.
    
    :param lista_pokemones: a list of dictionaries representing different pokemons, where each
    dictionary contains information about a single pokemon such as its name, type, and power
    :type lista_pokemones: list[dict]
    :param key: The key parameter is a string that represents the attribute of the Pokemon dictionary
    that we want to use to filter the list. For example, if we want to filter the list based on the type
    of Pokemon, we would set key to "type"
    :type key: str
    :param valor: The value of the attribute that we want to search for in the list of dictionaries
    :type valor: str
    :return: a float value which represents the average "poder" attribute of the pokemons in the input
    list that have a specific value for the input key.
    """
    suma_promedio = 0
    contador = 0
    for pokemon in lista_pokemones:
        if pokemon[key] == valor:
            suma_promedio += pokemon["poder"]
            contador += 1
    promedio = suma_promedio / contador
    return promedio

# ```
# * 07.2
# ```
# Crear la función "pokedex_promedio_poder_tipo" la cual recibira por parámetro la lista de pokemones como primer parámetro,
# el nombre de la clave en la cual buscará un valor específico como segundo parámetro y
# como tercer parámetro el valor a buscar que debe buscar en la key.
# Al encontrar el valor promedio deberá imprimir un mensaje por consola informandolo.
# Ejemplo:
#     > El poder promedio de pokemones con tipo psíquico es: 24.5
# Tips:
#     Reutilizar la función: -> "buscar_promedio_segun_atributo"
#     Informar: En caso de no haber pokemones en la lista, se deberá imprimir un mensaje de error.
# Retorno: None
# ```

def pokedex_promedio_poder_tipo(lista_pokemones: list[dict], key: str, valor: str) -> None:
    if lista_pokemones:
        promedio = buscar_promedio_segun_atributo(lista_pokemones, key, valor)
        mensaje = "El poder promedio de pokemones con {0} {1} es: {2}".format(key, valor, promedio)
        print(mensaje)
    else:
        lib_elemental.imprimir_mensaje("Lista vacia", "Error")

