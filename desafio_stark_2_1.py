from data_stark import lista_personajes


def stark_normalizar_datos(lista: list):
    if len(lista) > 0:
        for personaje in lista:
            if type(personaje["altura"]) != float:
                personaje["altura"] = float(personaje["altura"])
                print("El dato de altura del personaje {0} ha sido modificado".format(personaje["nombre"]))
                print("Datos normalizados")
            if type(personaje["peso"]) != float:
                personaje["peso"] = float(personaje["peso"])
                print("El dato de peso del personaje {0} ha sido modificado".format(personaje["nombre"]))
                print("Datos normalizados")
            if type(personaje["fuerza"]) != float:
                personaje["fuerza"] = float(personaje["fuerza"])
                print("El dato de fuerza del personaje {0} ha sido modificado".format(personaje["nombre"]))
                print("Datos normalizados")
    else:
        print("Error: Lista de héroes vacía")

def obtener_nombre():
    pass

            