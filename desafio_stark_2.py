from data_stark import lista_personajes


def print_nombre (personaje: dict, item: str) -> str:
    print("El personaje mas {0} es: {1}".format(item, personaje["nombre"]))

# ---- Nombres superheroes Masculino y femenino -----

def personaje_masc_fem (lista: list, genero: str)->str:
    for personaje in lista:
        if personaje["genero"] == genero :
            print(personaje["nombre"])
            

# ---- Superheroes Masculino o Fememino mas alto o mas bajo-----

def personaje_alto_bajo (lista: list, genero: str, min_max: str):
    superheroe_alto_bajo = None
    for personaje in lista:
        if personaje["genero"] == genero:
            if superheroe_alto_bajo is None:
                superheroe_alto_bajo = personaje
            else:
                if min_max == "alto":
                    if float(superheroe_alto_bajo["altura"]) < float(personaje["altura"]):
                        superheroe_alto_bajo = personaje
                elif min_max == "bajo":
                    if float(superheroe_alto_bajo["altura"]) > float(personaje["altura"]):
                        superheroe_alto_bajo = personaje               
    return superheroe_alto_bajo
    #print("El personaje masculino mas alto es: {0} y mide {1}".format(masculino_alto["nombre"], masculino_alto["altura"]))


# ---- Superheroe Femenino mas alto ----


def promedio_alturas(lista: list, genero: str)-> float:
    suma_alturas = 0
    contador = 0
    for personaje in lista:
        if personaje["genero"] == genero:
            personaje["altura"] = float(personaje["altura"])
            suma_alturas += personaje["altura"]
            contador += 1
    promedio = suma_alturas / contador
    return promedio

# ---- Tipo de color de ojos y pelo  e inteligencia----

def cant_item(lista: list, item: str) -> dict:
    """
    Cuenta la cantidad de personajes que cumplen con una condicion
    Recibe una lista y una condicion a buscar
    Retorna un diccionario con la condicion y la cantidad
    """

    contador_cualidad_item = {}
    for personaje in lista:
        color_item = personaje[item]
        if color_item in contador_cualidad_item:
            contador_cualidad_item[color_item] += 1
        else:
            contador_cualidad_item[color_item] = 1
    return contador_cualidad_item
    
# ---- Tipo de color de ojos ----
def print_cant_ojos():
    contador_colores_ojos = cant_item(lista_personajes, "color_ojos")
    for color_ojos, contador in contador_colores_ojos.items():
        if color_ojos == "":
            color_ojos = "No Tiene"        
        print("Hay {0} superheroes con color de ojos {1}".format(contador, color_ojos))

# ---- Tipo de color de pelo ----
def print_cant_pelo():
    contador_colores_pelo = cant_item(lista_personajes, "color_pelo")
    for color_pelo, contador in contador_colores_pelo.items():
        if color_pelo == "":
            color_pelo = "No Tiene"        
        print("Hay {0} superheroes con color de pelo {1}".format(contador, color_pelo))

# ---- Tipo de inteligencia ----
def print_cant_inteligencia():
    contador_inteligencia = cant_item(lista_personajes, "inteligencia")
    for inteligencia, contador in contador_inteligencia.items():
        if inteligencia == "":
            inteligencia = "No Tiene"
        print("Hay {0} superheroes con {1} inteligencia".format(contador, inteligencia))


while True:
    print("Elija una opcion:  ")
    opcion = input("\n1 - Superheroes masculinos\n2 - Superheroes Femeninos\n3 - Superheroe mas alto \n4 - Superheroe mas bajo\n5 - Altura promedio\n6 - Cantidad de superheroes\n7 - Lista\n>> ")
    match opcion:
        case "1":
            personaje_masc_fem(lista_personajes, "M")
        case "2":
            personaje_masc_fem(lista_personajes, "F")
        case "3":
            genero = input("Desea saber el mas alto femenino o masculino? F o M: ")
            genero = genero.upper()
            if genero == "F" or genero == "M":
                personaje = personaje_alto_bajo(lista_personajes, genero, "alto")
                print_nombre(personaje, "alto")
            else:
                print("Error")
        case "4":
            genero = input("Desea saber el mas bajo femenino o masculino? F o M: ")
            genero = genero.upper()
            if genero == "F" or genero == "M":
                personaje = personaje_alto_bajo(lista_personajes, genero, "bajo")
                print_nombre(personaje, "bajo")
            else:
                print("Error")
        case "5":
            genero = input("Desea saber la altura promedio femenina o masculina? F o M:  ")
            genero = genero.upper()
            if genero == "F" or genero == "M":
                print("El promedio de alturas {0} es de: {1}".format(genero,promedio_alturas(lista_personajes, genero)))
            else:
                print("Error")
        case "6":
            item = input("Desea saber la cantidad de superheroes con color de ojos, de pelo o inteligencia iguales?:  OJOS, PELO, INTELIGENCIA ")
            item = item.upper()
            match item:
                case "OJOS":
                    print_cant_ojos()
                case "PELO":
                    print_cant_pelo()
                case "INTELIGENCIA":
                    print_cant_inteligencia()
        case "7":
            item = input("Desea una lista cantidad de superheroes con color de ojos, de pelo o inteligencia iguales?:  OJOS, PELO, INTELIGENCIA ")
            item = item.upper()
            match item:
                case "OJOS":
                    print(cant_item(lista_personajes, "color_ojos"))
                case "PELO":
                    cant_item(lista_personajes, "color_pelo")
                case "INTELIGENCIA":
                    cant_item(lista_personajes, "inteligencia")




