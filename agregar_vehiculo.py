import json
import vehiculo
import datetime  # Asegúrate de importar datetime

def comprobar_fecha(fecha):
    try:
        datetime.datetime.strptime(fecha, "%d/%m/%Y")
        return True  # La fecha es válida
    except ValueError:
        return False  # La fecha no es válida

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
    nuevo_vehiculo = vehiculo.Vehiculo()
    nuevo_vehiculo.matricula = input("Ingresa el matricula: ")
    nuevo_vehiculo.marca = input("Ingresa el marca: ")
    nuevo_vehiculo.modelo = input("Ingresa el modelo: ")
    fecha_creacion = input("Ingresa la fecha de creación (dd/mm/yyyy): ")
    if comprobar_fecha(fecha_creacion):
        nuevo_vehiculo.fecha_creacion = fecha_creacion
        guardar_vehiculo_en_json(nuevo_vehiculo, file_name)
        print("Vehiculo añadido exitosamente al archivo JSON.")
    else:
        print("La fecha ingresada no es válida. Por favor, usa el formato dd/mm/yyyy.")


