import json
import poke_lib_elemental  as lib_elemental
import poke_lib_intermedio as lib_intermedio

path = r'C:\\Users\\Denise\\Documents\\1 Cuatri\\Programacion_1\\Extra_Pockemon\\data_pokemones.json'
lista_pokemones = lib_elemental.pokedex_leer_archivo(path)



# * 18.1
# ```
# Crear la función "obtener_atributos_pokemon" la cual recibira como primer parámetro
# un diccionario que representara a un solo pokemon.
# Como segundo parametro recibira un atributo (clave) a evaluar (tipo, evoluciones, fortaleza, debilidad)
# Retorno: Si la clave existe, retornara su valor el cual es una lista, en caso de que no exista, retornara una lista vacía.
# ```
def obtener_atributos_pokemon(pokemon: dict, clave: str) -> list:
    lista_valores = []
    lista_valores = pokemon[clave]
    return lista_valores


# * 18.2
# ```
# Crear la funcion "pokedex_imprimir_multiples_atributos" la cual recibira como primer parametro la lista de pokemones 
# y como segundo parámetro el atributo (clave) a evaluar.
# La función deberá obtener la lista de valores de dicha clave y formatear un mensaje con el número del pokémon,
# su nombre y cada uno de los valores de dicha clave separados por el carácter "|" (pipe)
# (en caso de que tenga valores) o sino deberá aparecer la frase "No Posee".
# Ejemplo:
# # Si la clave a evaluar es 'evoluciones' la salida será:
# #150 - Mewtwo - evoluciones: Mega-mewtwo X | Mega-mewtwo Y
# #151 - Mew - evoluciones: No Posee
# Tips:
#     Reutilizar las funciones: -> "obtener_atributos_pokemon", "imprimir_mensaje",
# "nombre_format_pokemon" y "capitalizar_palabras"
#     Mensaje: En caso de que alguna de las listas esté vacía, informar por consola.
# Retorno: None  

def pokedex_imprimir_multiples_atributos(lista_pokemon: list[dict], key: str) -> None:
    if lista_pokemon:
        for pokemon in lista_pokemon:
            lista_valores = obtener_atributos_pokemon(pokemon, key)
            if len(lista_valores) < 1:
                #lista_valores.append("No tiene")
                mensaje = "{0} - {1}: {2}". format(lib_elemental.nombre_format_pokemon(pokemon), key, "No tiene")
            else:
                cadena_valores = " | ".join(lista_valores)
                cadena_valores = lib_elemental.capitalizar_palabras(cadena_valores)
                mensaje = "{0} - {1}: {2}". format(lib_elemental.nombre_format_pokemon(pokemon), key, cadena_valores)
            lib_elemental.imprimir_mensaje(mensaje, "success")
    else: 
        lib_elemental.imprimir_mensaje("Lista vacia", "error")


