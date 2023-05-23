from data_stark import lista_personajes

"""
1) Analizar detenidamente el set de datos
2) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
3) Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
4) Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
5) Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
6) Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
7) Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
8) Calcular e informar cual es el superhéroe más y menos pesado.
9) Ordenar el código implementando una función para cada uno de los valores informados.
10) Construir un menú que permita elegir qué dato obtener

"""
def nombres_personajes():
    for personaje in lista_personajes:
        print (personaje["nombre"])

def nombre_altura_personajes ():
    for personaje in lista_personajes:
        print ("Nombre:", personaje["nombre"], ", Altura: ",personaje["altura"])   

def personaje_alto ():
    personaje_mas_alto = lista_personajes[0]
    for personaje in lista_personajes:
        personaje_mas_alto["altura"] = float(personaje_mas_alto["altura"])
        personaje["altura"] = float(personaje["altura"])
        if personaje_mas_alto["altura"] < personaje["altura"]:
            personaje_mas_alto = personaje
        else:
            continue
        return personaje_mas_alto
    print("El personaje mas alto es: {0} y mide {1} cm de altura".format(personaje_mas_alto["nombre"], personaje_mas_alto["altura"]))

def personaje_bajo ():
    personaje_mas_bajo = lista_personajes[0]
    for personaje in lista_personajes:
        personaje_mas_bajo["altura"] = float(personaje_mas_bajo["altura"])
        personaje["altura"] = float(personaje["altura"])
        if personaje_mas_bajo["altura"] > personaje["altura"]:
            personaje_mas_bajo = personaje
        else:
            continue

    print("El personaje mas bajo es: {0} y mide {1} cm de altura".format(personaje_mas_bajo["nombre"], personaje_mas_bajo["altura"]))

def altura_promedio():
    suma_alturas = 0
    contador = 0
    for personaje in lista_personajes:
        personaje["altura"] = float(personaje["altura"])
        suma_alturas += personaje["altura"]
        contador += 1

    promedio = suma_alturas / contador
    print("El promedio de alturas es de: ", promedio)

def identidad_personaje ():
    pass

def personaje_pesado ():
    personaje_mas_pesado = lista_personajes[0]
    for personaje in lista_personajes:
        personaje_mas_pesado["peso"] = float(personaje_mas_pesado["peso"])
        personaje["peso"] = float(personaje["peso"])
        if personaje_mas_pesado["peso"] < personaje["peso"]:
            personaje_mas_pesado = personaje
        else:
            continue

def personaje_liviano ():
    personaje_mas_liviano = lista_personajes[0]
    for personaje in lista_personajes:
        personaje_mas_liviano["peso"] = float(personaje_mas_liviano["peso"])
        personaje["peso"] = float(personaje["peso"])
        if personaje_mas_liviano["peso"] > personaje["peso"]:
            personaje_mas_liviano = personaje
        else:
            continue
    


while True:
    print("Ingrese una opcion: ")
    respuesta = input("\n1 - Nombre de superheroes \n2 - Nombre y altura de superheroes \n3 - Superheroe mas alto \n4 - Superheroe mas bajo\n5 - Altura promedio \n6 ID de personaje mas alto o mas bajo\n7 - Personaje mas pesado\n8 - Personaje menos pesado\n\n")
    if(respuesta == "1"):
        nombres_personajes()
    elif(respuesta == "2"):
        nombre_altura_personajes ()
    elif(respuesta == "3"):
        personaje_alto ()
    elif(respuesta == "4"):
        personaje_bajo ()
    elif(respuesta == "5"):
        altura_promedio()
    elif(respuesta == "6"):
        opcion = input("Desea saber el ID del personaje mas alto o mas bajo?")
        if opcion == "alto":
            pass
    elif(respuesta == "7"):
        personaje_pesado ()
    elif(respuesta == "8"):
        personaje_liviano ()


