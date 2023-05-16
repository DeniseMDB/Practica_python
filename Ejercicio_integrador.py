"""
Un gimnasio desea llevar el control de sus miembros.
Cada miembro tiene un número de identificación, nombre, edad y tipo de membresía
(por ejemplo, mensual o anual). La información se encuentra almacenada en cuatro listas paralelas:
una lista con los números de identificación, otra lista con los nombres, una lista con las edades y
una lista con los tipos de membresía.

"""

miembros_id = [0,1,2,3,4]
miembros_nombre = ["Jose", "Ana", "Flor", "Agus", "Carlos"]
miembros_edad = [32, 55, 62, 15, 43]
miembros_membresia = ["anual", "mensual", "anual", "mensual", "anual"]


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
        numero_id = input("Ingrese el numero de id de nuevo miembro: >> ")
        numero_id = int(numero_id)
        nombre = input("Ingrese el nombre: >> ")
        edad = input("Ingrese la edad del miembro: >> ")
        edad = int(edad)
        membresia = input("Ingrese la membresia: (Mensual o anual) >> ")

        miembros_id.append(numero_id)
        miembros_nombre.append(nombre)
        miembros_edad.append(edad)
        miembros_membresia.append(membresia)

        print("Exito.")
    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        for i in range(len(miembros_id)):
            print("ID: {0} | Nombre: {1} | Edad: {2} | Membresia: {3}".format(
                miembros_id[i], miembros_nombre[i], miembros_edad[i], miembros_membresia[i]) )
    
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        n_id = input("Por favor ingrese el numero de id del miembro que desea modificar:  ")
        n_id = int(n_id)
        if n_id in miembros_id:
            miembros_membresia[n_id] = input("Ingrese la nueva membresia: ")
        else:
            print("El numero ingresado es incorrecto")

    # Opcion 4: Buscar información de un miembro
    elif opcion == "4":
        n_id = input("Por favor ingrese el numero de id del miembro que desea buscar:  ")
        n_id = int(n_id)
        if n_id in miembros_id:
            print("ID: {0} | Nombre: {1} | Edad: {2} | Membresia: {3}".format(
                    miembros_id[n_id], miembros_nombre[n_id], miembros_edad[n_id], miembros_membresia[n_id]) )
        else:
            print("El id no ha sido encontrado")

    # OPcion 5: Calcular el promedio de edad de los miembros:
    elif opcion == "5":
        suma_edades = 0
        contador = 0

        for edades in miembros_edad:
            suma_edades += edades
            contador += 1

        promedio = suma_edades / contador

        print("El promedio de edades de los miembros es de: ", promedio)

    # Opcion 6: Buscar el miembro más joven y el más viejo

    elif opcion == "6":

        miembro_mas_joven = miembros_edad[0]
        miembro_mas_viejo = miembros_edad[0]
        i_mas_joven = 0
        i_mas_viejo = 0

        for edad in miembros_edad:
            if edad > miembro_mas_viejo:
                miembro_mas_viejo = edad
            if edad < miembro_mas_joven:
                miembro_mas_joven = edad
        
        for i in range(len(miembros_edad)):
            if miembros_edad[i] == miembro_mas_viejo:
                i_mas_viejo = i
            if miembros_edad[i] == miembro_mas_joven:
                i_mas_joven = i

        print("El miembro más joven es: {0} y tiene {1} años de edad".format(miembros_nombre[i_mas_joven], miembro_mas_joven))
        print("El miembro más viejo es: {0} y tiene {1} años de edad".format(miembros_nombre[i_mas_viejo], miembro_mas_viejo))
            
    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")