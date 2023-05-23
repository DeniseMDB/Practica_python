import json
import re
import funciones_lib as lib

"""
1 - Listar los primeros N héroes. El valor de N será ingresado por el usuario  (Validar que no supere max. de lista)
2 - Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)
3 - Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)
4 - Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio
(preguntar al usuario la condición: ‘menor’ o ‘mayor’) se deberá listar en consola aquellos que cumplan con ser mayores o menores según corresponda.
5 - Buscar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda. (Usando RegEx)
6 - Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]
Aclaraciones:
Los puntos deben ser accedidos mediante un menú. Para todas las opciones, validar lo ingresado por consola con RegEx
El set de datos proviene de un json
Realizar las validaciones que crea pertinentes
En todos los casos se deberá trabajar con una copia de la lista original
"""

PATH_ARCHIVO = r"C:\\Users\\Denise\\Documents\\1 Cuatri\\Programacion_1\\data_stark.json"


lista_heroes =  lib.leer_archivo(PATH_ARCHIVO)


def print_menu():
    menu =\
    '''
    ==== MENÚ ====
    1. Listar n cantidad de heroes
    2. Ordenar por altura (asc o desc)
    3. Ordenar por fuerza (asc o desc)
    4. Calcular promedio de: 
    5. Buscar heroes por inteligencia
    6. Exportar lista ordenada en archivo CSV
    7. Salir
    '''
    print(menu)



# def validar_opcion_menu():
#     print_menu()
#     respuesta = input("Elija una opcion: >> ")
#     if re.match("^[0-7]{1}$", respuesta):
#         return respuesta
#     return -1

def desafio_tipo_parcial(lista: list[dict]):
    lista_archivo = []
    while True:
        print_menu()
        respuesta = input("Elija una opcion: >>")
        respuesta = lib.validar_numero(respuesta, "[1-7]{1}$")
        print(respuesta)
        lista_normalizada = lib.stark_normalizar_datos(lista_heroes).copy()
        output = "C:\\Users\\Denise\\Documents\\1 Cuatri\\Programacion_1\\desafio_tipo_parcial\\data.csv"
        match respuesta:
            case 1:
                #funcion Listar los primeros N héroes
                n = input("Ingrese la cantidad de heroes que desea ver:  ")
                n = lib.validar_numero(n, "[1-9]{1,2}$")
                key = "altura"
                cantidad = lib.validar_lista(lista_heroes, n)
                lista_copy = lista_heroes[:cantidad].copy()
                lista_archivo = lib.mostrar_lista(lista_copy, key)
                
            case 2:
                #funcion Ordenar y Listar héroes por altura
                modo = input("Desea ordenar de manera ascendente o descendente? (asc o desc)>>> ")
                modo = lib.validar_respuesta(modo, "^a[c-s]{2}|d[e-s]{2}c$")
                key = "altura"
                lista_ordenada = lib.sort_asc_desc(lista_normalizada,key, modo)
                lista_archivo = lib.mostrar_lista(lista_ordenada, key)
                
            case 3:
                #funcion Ordenar y Listar héroes por fuerza
                modo = input("Desea ordenar de manera ascendente o descendente? (asc o desc)>>> ")
                modo = lib.validar_respuesta(modo, "^a[c-s]{2}|d[e-s]{2}c$")
                key = "fuerza"
                lista_ordenada= lib.sort_asc_desc(lista_normalizada,key, modo)
                lista_archivo = lib.mostrar_lista(lista_ordenada, key)
                
            case 4:
                #funcion Calcular promedio de cualquier key numérica
                print("Indique cual es el promedio que desea calcular: ")
                key = input("Altura, Peso o Fuerza >> ").lower()
                print("El promedio de {0} es de: {1}".format(key, lib.calcular_promedio(lista_normalizada, key)))
                modo = input("Desea saber aquellos que son mayores o menores que el promedio? (mayor/menor) >> ")
                lista_modo = lib.comparar_mayor_menor(lista_normalizada, key, modo)
                print("\n")
                print("Aquellos que son {0}es son: ".format(modo))
                lista_archivo = lib.mostrar_lista(lista_modo, key)
                
                
            case 5:
                lista_copia = lista_heroes.copy()
                key= "inteligencia"
                modo = input("Seleccione inteligencia: good, average, high  >>> \n")
                modo = lib.validar_respuesta(modo, "good|average|high")
                lista_archivo = lib.buscar(lista_copia, "inteligencia", modo)
                #lib.mostrar_lista(lista_archivo, "inteligencia")
            case 6:
                lib.exportar_csv(lista_archivo,key)
                print("Archivo generado")
            case 7:
                print("Saliendo...")
                break
                
desafio_tipo_parcial(lista_heroes)