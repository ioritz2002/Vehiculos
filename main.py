
#!/usr/bin/env python3

import json
import vehiculo
import agregar_vehiculo


import json
import listar
import vehiculo
import agregar_vehiculo

file_name = "vehiculos.json"
continuar = True
while continuar:

    print("1. Agregar una vehiculos")
    print("2. Listar vehiculos")
    print("3. Eliminar")
    print("4. Actualizar")
    print("5. Salir")
    opcion = int(input("Selecciona una opción: "))


    if opcion == 1:
        agregar_vehiculo.insertar_vehiculo()
    
    elif opcion == 2:
        listar.listar(file_name)

    elif opcion == 3:
        print("Eliminar")

    elif opcion == 4:
        print("Actualizar")
    
    elif opcion == 5:
        print("Saliendo del programa.")
        continuar = False
    else:
        print("Opcion no valida")