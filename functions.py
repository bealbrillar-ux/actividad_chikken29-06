import os, time


def pausa(x):
    time.sleep(x)

def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar mascota")
    print("2. Buscar mascota")
    print("3. Eliminar mascota")
    print("4. Actualizar estados")
    print("5. Mostrar mascotas")
    print("6. Salir")
    print("=====================================")

def elecion_menu():
    while True:
        try:
            elecion = 0
            while elecion not in [1,2,3,4,5,6]:
                elecion = int(input("Ingrese la eleción del menú: "))
                if elecion not in [1,2,3,4,5,6]:
                    print("Eleción no valida en las opciones.")
            return elecion
        except:
            print("Datos no validos, intente denuevo.")

def _validacion_str(palabra):
    if "" == palabra.strip():
        print("No se permite espacios en blanco ni vacíos.")
        return False
    else:
        return True

def _validacion_int(numero):
    if numero <= 0:
        print("El numero debe ser mayor que 0.")
        return False
    else:
        return True

def _validacion_float(numero):
    if numero <= 0:
        print("El numero debe ser mayor que 0.")
        return False
    else:
        return True


def agregar_mascota():
    while True:
        nombre = str(input("Ingrese el nombre de su mascota: ")).title()
        if _validacion_str(nombre):
            break
    while True:
        especie = str(input("Ingrese la especie de su mascota: ")).title()
        if _validacion_str(especie):
            break
    while True:
        try:
            edad = int(input("Ingrese la edad de su mascota: "))
            if _validacion_int(edad):
                break
        except:
            print("Datos no validos, intente denuevo.")
    while True:
        try:
            peso = float(input("Ingrese el peso de su mascota: "))
            if _validacion_float(peso):
                break
        except:
            print("Datos no validos, intente denuevo.")
    mascota = {
        "nombre":nombre,
        "especie":especie,
        "edad":edad,
        "peso":peso,
        "saludable":False
        
    }
    return mascota

def _validacion_existe(coleccion_general):
    if len(coleccion_general) >0:
        return True
    else:
        print("No existen mascotas guardadas.")
        return False

def buscar_mascota(coleccion_general):
    if _validacion_existe(coleccion_general):
        while True:
            nombre = str(input("Ingrese el nombre de su mascota: ")).title()
            if _validacion_str(nombre):
                break
        for mascota in coleccion_general:

            if mascota["nombre"].strip().upper() == nombre.strip().upper(): #IGNORA LOS ESPACIOS Y MAYUSCULAS
                return coleccion_general.index(mascota)  #EN QUE POSICION SE ENCUENTRA (NUMERO)
        print("no existe ningún registro con ese nombre")
    return -1

def eliminar_mascota(coleccion_general):
    if _validacion_existe(coleccion_general):
        posicion = buscar_mascota(coleccion_general)
        if posicion != -1 :
            coleccion_general.pop(posicion)  #ELIMINA LA POSICION (NUMERO)

def actualizacion(coleccion_general):
    if _validacion_existe(coleccion_general):
        for mascota in coleccion_general:
            mascota["saludable"] = True

def mostrar_mascotas(coleccion_general):
    if _validacion_existe(coleccion_general):
        print("=== LISTA DE MASCOTAS ===")
        actualizacion(coleccion_general)
        for mascota in coleccion_general:
            if mascota["saludable"]:
                estado = "SALUDABLE"
            else:
                estado = "NO SALUDABLE"
            print(f"Nombre: {mascota["nombre"]}")
            print(f"Especie: {mascota["especie"]}")
            print(f"Edad:{mascota["edad"]}")
            print(f"Peso: {mascota["peso"]}")
            print(f"Estado: {estado}")
            print(f"********************************************")
            pausa(1)





