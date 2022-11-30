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

    def cambiarEstado(self):
        pass

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

    def tiempoDeEstadia():
        pass

if __name__ == "__main__":
    codReserva = str(input())
    with open("reservas.json", "r") as f:
        data = json.load(f)

    for element in data:
        if element["codReserva"]==codReserva:
           fEnt = datetime.strptime(str(element["fechaEnt"]),"%d-%m-%Y")
           fSal = datetime.strptime(str(element["fechaSal"]),"%d-%m-%Y")
           t = fSal - fEnt
           print(t.days)
#Fio:
#Editar el metodo MostrarDatos de la clase Habitacion y hacer que solo muestre las disponibles 
#Mostrar Reserva 

#Pedro:
#Agregar metodo que calcule la cantidad de días de la estadía del cliente 
#considerando la fecha de llegada y de salida (o sea las fechas que ingresa) (check)

#Validar cantidad de personas con cantidad de habitaciones. Por ejemplo, 10 personas no pueden 
#entrar en 1 habitación, es imposible.