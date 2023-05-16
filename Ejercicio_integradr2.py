"""
Un gimnasio desea llevar el control de sus miembros.
Cada miembro tiene un número de identificación, nombre, edad y tipo de membresía
(por ejemplo, mensual o anual). La información se encuentra almacenada en una lista de listas,
donde cada sublista representa a un miembro y contiene los siguientes elementos:
número de identificación, nombre, edad y tipo de membresía.
"""

lista_miembros = [
    [0, "Jose Martinez", 35, "mensual"],
    [1, "Maria Gonzalez", 50, "anual"],
    [2, "Florencia Rodriguez", 20, "mensual"],
    [3, "Fulano de tal", 32, "anual"]
    ]

while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")


    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":
        print("Por favor ingrese los siguientes datos >> ")
        id = int(input("Numero de id: "))
        nombre = input("Nombre del miembro:  ")
        edad = int(input("Edad:  "))
        membresia = input("Tipo de membresia: ")

        lista_miembros.append([id, nombre, membresia])

        print("Exito.")


    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        for miembro in lista_miembros:
            id = miembro[0]
            nombre = miembro[1]
            edad = miembro[2]
            membresia = miembro[3]
            print("Nro ID: {0} | Nombre: {1} | Edad: {2} | Tipo membresia: {3}".format(id,nombre,edad,membresia))

    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        n_id = int(input("Ingrese el numero de ID:  "))
        for miembros in lista_miembros:
            if n_id == miembros[0]:
                print("Modificaras la membresia de: ", miembros[1])
                membresia_nueva = input("Ingrese la nueva membresia:  ")
                miembros[3] = membresia_nueva
                print("Se ha registrado el cambio")


    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        n_id = int(input("Ingrese el numero de ID:  "))
        for miembros in lista_miembros:
            if n_id == miembros[0]:
                print("Nro ID: {0} | Nombre: {1} | Edad: {2} | Tipo membresia: {3}".format(miembros[0],miembros[1],miembros[2], miembros[3]))


    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        suma_edades = 0
        contador = 0

        for miembro in lista_miembros:
            suma_edades += miembro[2]
            contador += 1
        promedio = suma_edades / contador

        print("El promedio de edad de los miembros es de: ", promedio)


    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        miembro_mas_joven = lista_miembros[0][2]
        miembro_mas_viejo = lista_miembros[0][2]
        i_mas_joven = 0
        i_mas_viejo = 0

        for miembro in lista_miembros:
            if miembro[2] < miembro_mas_joven:
                miembro_mas_joven = miembro[2]
                i_mas_joven = miembro
            if miembro[2] > miembro_mas_viejo:
                miembro_mas_viejo = miembro[2]
                i_mas_viejo = miembro


        print("El miembro más joven es: {0} y tiene {1} años de edad".format(i_mas_joven[1], miembro_mas_joven))
        print("El miembro más viejo es: {0} y tiene {1} años de edad".format(i_mas_viejo[1], miembro_mas_viejo))


    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")
