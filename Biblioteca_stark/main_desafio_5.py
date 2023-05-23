from stark_desafio_5 import stark_marvel_app_5, leer_archivo

PATH_ARCHIVO = r"C:\Users\Denise\Documents\1 Cuatri\Programacion_1\data_stark.json"
lista_heroes =  leer_archivo(PATH_ARCHIVO)

stark_marvel_app_5(lista_heroes)