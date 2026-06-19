from functions import *


coleccion_general = []

acceso = True

while acceso:
    menu()

    elecion = elecion_menu()

    if elecion == 1:
        coleccion_general.append(agregar_mascota())
    elif elecion == 2:
        posicion = buscar_mascota(coleccion_general)
        if posicion != -1:
            mascota = coleccion_general[posicion]
            if mascota["saludable"]:
                estado = "SALUDABLE"
            else:
                estado = "NO SALUDABLE"
            print(f"Nombre:{mascota["nombre"]}")
            print(f"Especie:{mascota["especie"]}")
            print(f"Edad:{mascota["edad"]}")
            print(f"Peso:{mascota["peso"]}")
            print(f"Estado:{estado}")
    elif elecion ==  3:
        eliminar_mascota(coleccion_general)
    elif elecion == 4:
        actualizacion(coleccion_general)
    elif elecion == 5:
        mostrar_mascotas(coleccion_general)
    else:
        print("Gracias por usar el sistema. Vuelva Pronto")
        acceso = False