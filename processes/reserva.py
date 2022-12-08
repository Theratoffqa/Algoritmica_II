import random
from datetime import datetime
import json
#from entities.habitacion import *
#error al momento de importar entities.habitacion

class Reserva:
    
    def __init__(self,codReserva,titular,fechaEnt,fechaSal,numDias,cantPersonas,cantHabitaciones,habitacionesSolicitadas): 
        self._codReserva = codReserva
        self._titular = titular
        self._fechaEnt = fechaEnt
        self._fechaSal = fechaSal
        self._numDias = numDias
        self._cantPersonas = cantPersonas
        self._cantHabitaciones = cantHabitaciones
        self._habitacionesSolicitadas = habitacionesSolicitadas
        
    def separarHabitaciones(cantHabitaciones):
        habitacionesSolicitadas = []
        for i in range(cantHabitaciones):
            habitacionesSolicitadas.append(input("Ingrese el numero de la "+str(i+1)+" habitacion que desea reservar:"))    

        return habitacionesSolicitadas

    def reservar(self):
        reservan = dict(codReserva = self._codReserva,titular = self._titular,fechaEnt = self._fechaEnt,fechaSal = self._fechaSal,numDias =self._numDias,cantPersonas =self._cantPersonas,canthabitaciones = self._cantHabitaciones,habitacionesSolicitadas =self._habitacionesSolicitadas)
        
        with open("reservas.json", "r") as f:
            data = json.load(f)

        data.append(reservan)

        with open("reservas.json", "w") as f:
            json.dump(data, f, indent=4)
   
    def generarCod():
        caracteres="123456789abcdefghijklmnopqrstuvwxyz"
        longitud = 5
        muestra = random.sample(caracteres,longitud)
        codigo = "".join(muestra)

        return codigo

    def cambiarEstado(habitacionesSolicitadas):
        for element in habitacionesSolicitadas: 
            with open("habitaciones_Registradas.json", "r") as f:
                data = json.load(f)
            for habitacionSolicitada in data:
                if str(habitacionSolicitada["numHabitacion"])== element:
                    habitacionSolicitada["estado"] = "No disponible"
                              
            with open("habitaciones_Registradas.json", "w") as f:
                json.dump(data, f, indent=4)


    def mostrarReserva(codReserva):
       
            with open("reservas.json", "r") as f:
                data = json.load(f)
        
            for element in data:
                if element["codReserva"]==codReserva:
                    print("------------------------------------------------------")
                    print("DATOS DE LA RESERVA DE LA HABITACION")
                    print("Codigo de reserva:"+ str(element["codReserva"]))
                    print("Titular:"+ str(element["titular"]))
                    print("Fecha de entrada:"+ str(element["fechaEnt"]))
                    print("Fecha de salida:"+ str(element["fechaSal"]))
                    print("Numero de dias de la estadia:",element["numDias"])
                    print("Cantidad de personas:", element["cantPersonas"])
                    print("Cantidad de habitaciones:", element["canthabitaciones"])
                    print("Habitaciones solicitadas:"+ str(element["habitacionesSolicitadas"]))
                    print("------------------------------------------------------")

    def tiempoDeEstadia( E, S):
        fEnt = datetime.strptime(str(E),"%d-%m-%Y")
        fSal = datetime.strptime(str(S),"%d-%m-%Y")
        t = fSal - fEnt
        return t.days
    
    def validarNumPers(codReserva):
        with open("reservas.json", "r") as f:
            data = json.load(f)
    
        for element in data:
            if element["codReserva"]==codReserva:
                n = element["canthabitaciones"]
                tipo = element["habitacionesSolicitadas"]
                cantpers = element["cantPersonas"]
                NumPers = 0
                with open("habitaciones_Registradas.json", "r") as g:
                    data2 = json.load(g)
                for i in range(n):
                    for element in data2:
                        if element["numHabitacion"] == int(tipo[i]):
                            if element["tipoHabitacion"] == 'Simple':
                                NumPers = NumPers + 1
                            elif(element["tipoHabitacion"] == 'Doble' or element["tipoHabitacion"] == 'Matrimonial'):
                                NumPers = NumPers + 2
                            elif(element["tipoHabitacion"] == 'Triple'):
                                NumPers = NumPers + 3
        if cantpers > NumPers:
            print("La cantidad de personas para la reserva es mayor al espacio pedido. Por favor pedir más habitaciones.")
            return False
        else:
            return True        