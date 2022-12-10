import json

file_path = "habitaciones_Registradas.json"

class Habitacion:
    
    def _init_(self,estado,precio,tipoHabitacion,numHabitacion): 
        self.estado = estado
        self.precio = precio
        self.tipoHabitacion = tipoHabitacion
        self.numHabitacion = numHabitacion

    def buscarHabitacion():
        with open(file_path, "r") as f:
            habitacionTemp = json.load(f)
        habitacion_buscar = int(input("Ingrese el numero de habitacion:"))
        for element in habitacionTemp:
                if element["numHabitacion"] == habitacion_buscar:
                    print("DATOS DE LA HABITACION "+str(habitacion_buscar))
                    print("------------------------------------------------------")
                    print("Estado:"+ element["estado"])
                    print("Precio:"+ str(element["precio"]))
                    print("Tipo de la habitacion:"+ element["tipoHabitacion"])
                    print("Numero de la habitacion:"+ str(element["numHabitacion"]))
                    print("------------------------------------------------------")

    def mostrarDatos():
        with open(file_path, "r") as f:
            habDatos = json.load(f)
        for element in habDatos:
            if element["estado"]=="Disponible":
                print("------------------------------------------------------")
                print("DATOS DE LA HABITACION "+str(element["numHabitacion"]))
                print("Estado:"+ element["estado"])
                print("Precio:"+ str(element["precio"]))
                print("Tipo de la habitacion:"+ element["tipoHabitacion"])
                print("Numero de la habitacion:"+ str(element["numHabitacion"]))
                print("------------------------------------------------------")