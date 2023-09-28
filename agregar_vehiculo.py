import json
import vehiculo

def guardar_vehiculo_en_json(vehiculo):
    # Cargar datos existentes (si los hay) desde el archivo JSON
    try:
        with open("personas.json", "r") as archivo:
            vehiculos = json.load(archivo)
    except FileNotFoundError:
        # Si el archivo no existe, crear una lista vacía
        vehiculos = []

def insertar_vehiculo(vehiculos):
    # Agregar la nueva vehiculo a la lista
    vehiculos.append(vehiculo.__dict__)

    # Guardar la lista actualizada en el archivo JSON
    with open("vehiculos.json", "w") as archivo:
        json.dump(vehiculos, archivo, indent=4)

        matricula = input("Ingresa el matricula: ")
        marca = input("Ingresa el marca: ")
        modelo = input("Ingresa el modelo: ")
        fecha_creacion = int(input("Ingresa la fecha_creacion: "))
        nuevo_vehiculo = vehiculo.Vehiculo(matricula, marca, modelo, fecha_creacion)
        guardar_vehiculo_en_json(nuevo_vehiculo)
        print("Vehiculo añadido exitosamente al archivo JSON.")