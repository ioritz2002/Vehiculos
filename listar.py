import vehiculo
import json
import datetime

def vehiculos_fich_a_lista(file_name):
    vehiculos = []

    try:
        with open(file_name, "r") as archivo:
            contenido = archivo.read()

            if contenido:
                datos = json.loads(contenido)

                for d in datos:
                    ve = vehiculo.Vehiculo()
                    ve.matricula = d["matricula"]
                    ve.marca = d["marca"]
                    ve.modelo = d["modelo"]
                    ve.fecha_creacion = d["fecha_creacion"]

                    vehiculos.append(ve)

        return vehiculos
    except FileNotFoundError:
        print("El fichero no existe")

    pass

def mostrar_datos_formateado(vehiculo):
    print("---Vehiculo---\nMatricula: " + vehiculo.matricula + "\nMarca: " + vehiculo.marca + "\nModelo: " + vehiculo.modelo +
           "\nFecha de creacion: " + datetime.datetime.utcfromtimestamp(vehiculo.fecha_creacion))
    pass

def listar(file_name):
    vehiculos = vehiculos_fich_a_lista(file_name)
    
    for i in vehiculos:
        mostrar_datos_formateado(i)
    
    pass
