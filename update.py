import json
import vehiculo  # No es necesario importar 'agregar_vehiculo' si no se usa en este fragmento de código

def actualizar_vehiculo(file_name, matricula, nueva_marca, nuevo_modelo):
    # Abrir el archivo JSON en modo lectura
    with open(file_name, "r") as archivo:
        vehiculos = json.load(archivo)

    # Iterar sobre la lista de vehículos en el archivo JSON
    for elemento in vehiculos:
        if elemento["matricula"] == matricula:
            elemento["marca"] = nueva_marca
            elemento["modelo"] = nuevo_modelo
            break  # Detener la iteración una vez que se actualice el vehículo

    # Abrir el archivo JSON en modo escritura y guardar los cambios
    with open(file_name, "w") as archivo:
        json.dump(vehiculos, archivo, indent=4)

    print("Objeto actualizado con éxito en el archivo JSON.")

def run(file_name):
# Solicitar valores al usuario mediante input
    nueva_matricula = input("Ingresa una matrícula que exista: ")
    nueva_marca = input("Ingresa la nueva marca: ")
    nuevo_modelo = input("Ingresa el nuevo modelo: ")

# Llamar a la función con los valores ingresados por el usuario
    actualizar_vehiculo(file_name, nueva_matricula, nueva_marca, nuevo_modelo)

