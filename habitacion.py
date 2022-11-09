import json

if __name__ == "__main__":
    menu="""
1.- Registrar habitacion
2.- Actualizar datos de habitacion
Elija una opcion: """
    option = int(input(menu))
    if option == 1:
    
        print("A continuacion, digite las caracteristicas de la nueva habitacion:")
        estado = input("Estado: ")
        precio = input("Precio: ")
        tipoHabitacion = input("Tipo de habitacion:")
        numHabitacion = input("Numero de habitacion:")
        new_Room= Habitacion(estado,precio,tipoHabitacion,numHabitacion)
        roomn = dict(estado = new_Room._estado, precio = new_Room._precio,tipoHabitacion = new_Room._tipoHabitacion,numHabitacion = new_Room._numHabitacion)
        
        with open("habitaciones_Registradas.json", "r") as f:
            data = json.load(f)

        data.append(roomn)

        with open("habitaciones_Registradas.json", "w") as f:
            json.dump(data, f, indent=4)

    elif option == 2:
        
        pass

    else:
        print("Opcion no valida")