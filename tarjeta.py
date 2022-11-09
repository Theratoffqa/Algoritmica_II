from datetime import datetime
import json

class Tarjeta:

    def _init_(self,numTarjeta,fechCaducidad,codSeguridad,nomTarjeta,apellTarjeta):
        self._numTarjeta = numTarjeta
        self._fechCaducidad = fechCaducidad
        self._codSeguridad = codSeguridad
        self._nombTarjeta = nomTarjeta
        self._apellTarjeta = apellTarjeta

    def verificarTarjeta(N_tarjeta):
        passed = False
        if len(str(N_tarjeta)) == 16:
            passed = True
            return passed
    
    def verificarCaducidad(F_Venci,F_Actu):
        passed = False
        if F_Venci > F_Actu:
            passed = True
            return passed
    
    def verificarBloqueo(Num_Tarjeta):
        passed = False
        for number in NumerosBloqueados:
            if Num_Tarjeta == number:
                passed = True
                return passed
            

NumerosBloqueados = [0000000000000000]



if __name__ == "__main__":
    menu="""Ingresar tarjeta"""

    NombreTarjeta = input("Nombre: ")
    ApellidoTarjeta = input("Apellido: ")
    NumeroTarjeta = input("Tarjeta: ")
    CodigoTarjeta = input("Codigo de seguridad: ")
    FechaCaducidadTarjeta = input("Fecha Caducidad: ")
    if Tarjeta.verificarTarjeta(NumeroTarjeta):
        print("Numero de Tarjeta valido")
        valido = True
    else:
        print("Numero de Tarjeta invalido")

    if valido == True:
        if Tarjeta.verificarCaducidad(FechaCaducidadTarjeta,datetime.date()):
            print("Tarjeta vigente")
        else:
            print("Tarjeta vencida")

        if Tarjeta.verificarBloqueo(NumeroTarjeta):
            print("Tarjeta operativa")
        else:
            print("Tarjeta bloqueada")

