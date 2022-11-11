import json

class Habitacion:
    
    def __init__(self,estado,precio,tipoHabitacion,numHabitacion): 
        self._estado = estado
        self._precio = precio
        self._tipoHabitacion = tipoHabitacion
        self._numHabitacion = numHabitacion

    def buscarHabitacion():
        with open("habitaciones_Registradas.json", "r") as f:
            habitacionTemp = json.load(f)
        habitacion_buscar = int(input("Ingrese el numero de habitacion:"))
        for element in habitacionTemp:
                if element["numHabitacion"] == habitacion_buscar:
                    print("DATOS DE LA HABITACION "+str(habitacion_buscar))
                    print("Estado:"+ element["estado"])
                    print("Precio:"+ str(element["precio"]))
                    print("Tipo de la habitacion:"+ element["tipoHabitacion"])
                    print("Numero de la habitacion:"+ str(element["numHabitacion"]))

    def mostrarDatos():
        with open("habitaciones_Registradas.json", "r") as f:
            habitacionTemp = json.load(f)
        for element in habitacionTemp:
            print("------------------------------------------------------")
            print("DATOS DE LA HABITACION "+str(element["numHabitacion"]))
            print("Estado:"+ element["estado"])
            print("Precio:"+ str(element["precio"]))
            print("Tipo de la habitacion:"+ element["tipoHabitacion"])
            print("Numero de la habitacion:"+ str(element["numHabitacion"]))
            print("------------------------------------------------------")
        

