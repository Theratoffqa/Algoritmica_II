import json

class Habitacion:
    
    def __init__(self,estado,precio,tipoHabitacion,numHabitacion): 
        self._estado = estado
        self._precio = precio
        self._tipoHabitacion = tipoHabitacion
        self._numHabitacion = numHabitacion

    def mostrarDatos(self):
        pass

if __name__ == "__main__":
    menu="""
1.- Registrar habitacion
2.- Actualizar datos de habitacion
Elija una opcion: """
    option = int(input(menu))
    if option == 1:
    
        print("A continuacion, digite las caracteristicas de la nueva habitacion:")
        estado = input("Estado: ")
        precio = int(input("Precio: "))
        tipoHabitacion = input("Tipo de habitacion:")
        numHabitacion = int(input("Numero de habitacion:"))
        new_Room= Habitacion(estado,precio,tipoHabitacion,numHabitacion)
        roomn = dict(estado = new_Room._estado, precio = new_Room._precio,tipoHabitacion = new_Room._tipoHabitacion,numHabitacion = new_Room._numHabitacion)
        
        with open("habitaciones_Registradas.json", "r") as f:
            data = json.load(f)

        data.append(roomn)

        with open("habitaciones_Registradas.json", "w") as f:
            json.dump(data, f, indent=4)

    elif option == 2:
        
        with open("habitaciones_Registradas.json", "r") as f:
            data = json.load(f)
        habitacion_busqueda = int(input("Ingrese el numero de habitacion que desea editar:")) 

        for habitacion in data:
            if habitacion["numHabitacion"] == habitacion_busqueda:
                print("Habitacion ANTES:",habitacion)
                habitacion["estado"] = input("Estado: ")
                habitacion["precio"] = int(input("Precio: "))
                habitacion["tipoHabitacion"] = input("Tipo de habitacion:")
                habitacion["numHabitacion"] = int(input("Numero de habitacion:"))
                print("Habitacion DESPUES:",habitacion)
                habitacion= Habitacion(habitacion["estado"],habitacion["precio"],habitacion["tipoHabitacion"],habitacion["numHabitacion"])
    
        data.append(habitacion)

        with open("habitaciones_Registradas.json", "w") as f:
            json.dump(data, f, indent=4)

    else:
        print("Opcion no valida")