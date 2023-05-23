import re
import json
from stark_desafio_5 import leer_archivo, obtener_nombre_y_dato
from funciones_stark_desafio_06 import *


# Crear la función 'leer_archivo' la cual recibirá por parámetro un string que indicará el nombre y
# extensión del archivo a leer (Ejemplo: archivo.json). Dicho archivo se abrirá en modo lectura únicamente
# y retornará la lista de héroes como una lista de diccionarios
# """

PATH_ARCHIVO = r"C:\\Users\\Denise\\Documents\\1 Cuatri\\Programacion_1\\data_stark.json"
lista_heroes =  leer_archivo(PATH_ARCHIVO)
lista_heroes_normalizada = stark_normalizar_datos(lista_heroes)



while True:
    print("==== MENÚ ====")
    print("1. Ordenar por altura (menor a mayor)")
    print("2. Ordenar por peso (mayor a menor)")
    print("3. Ordenar por nombre")
    print("4. Ordenar por largo del nombre")
    print("5. Ordenar por key")
    print("6. Salir")

    opcion = input("Ingrese la opción deseada: ")


    if opcion == "1":
        lista_altura = ordenar_por_altura(lista_heroes_normalizada)
        print(type(lista_altura))
        for heroe in lista_altura:
            print(obtener_nombre_y_dato(heroe, "altura"))
    elif opcion == "2":
        lista_peso = ordenar_por_peso(lista_heroes_normalizada)
        print(type(lista_peso))
        for heroe in lista_peso:
            print(obtener_nombre_y_dato(heroe, "peso"))
    elif opcion == "3":
        # llamar a la función ordenar_por_nombre
        pass
    elif opcion == "4":
        # llamar a la función ordenar_por_largo_nombre
        pass
    elif opcion == "5":
        key = input("Ingrese la key por la cual desea ordenar: ")
        sentido = input("Ingrese el sentido de ordenamiento (ascendente/descendente): ")
        ascendente = True if sentido.lower() == "ascendente" else False
        # llamar a la función ordenar_por_key
        pass
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print("Opción inválida, intente de nuevo")