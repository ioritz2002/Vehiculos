import json
import vehiculo

def guardar_vehiculo_en_json(vehiculo, file_name):
    # Cargar datos existentes (si los hay) desde el archivo JSON
    try:
        with open(file_name, "r") as archivo:
            vehiculos = json.load(archivo)
    except FileNotFoundError:
        # Si el archivo no existe, crear una lista vacía
        vehiculos = []

    # Agregar la nueva vehiculo a la lista
    vehiculos.append(vehiculo.__dict__)

    # Guardar la lista actualizada en el archivo JSON
    with open(file_name, "w") as archivo:
        json.dump(vehiculos, archivo, indent=4)

def crear_vehiculo(file_name):
    nuevo_vehiculo= vehiculo.Vehiculo()
    nuevo_vehiculo.matricula = input("Ingresa el matricula: ")
    nuevo_vehiculo.marca = input("Ingresa el marca: ")
    nuevo_vehiculo.modelo = input("Ingresa el modelo: ")
    #fecha_creacion = int(input("Ingresa la fecha_creacion: "))
    guardar_vehiculo_en_json(nuevo_vehiculo, file_name)
    print("Vehiculo añadido exitosamente al archivo JSON.")