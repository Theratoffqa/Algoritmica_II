import datetime
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
    
    def verificarCaducidad(fechaVenci):
        passed = False
        fechaActual = datetime.datetime.now()
        fechaV = datetime.datetime.strptime(fechaVenci, "%d/%m/%Y")
        if fechaV > fechaActual:
            passed = True
        return passed
    
    def verificarBloqueo(num_Tarjeta):
        passed = False
        with open("numerobloqueado.json", "r") as f:
            numerosBloqueados = json.load(f)
        for element in numerosBloqueados:
            if element["numero"] == num_Tarjeta:
                passed = True
        return passed        
            

#NumerosBloqueados = [0000000000000000]



if __name__ == "__main__":
    menu="""Ingresar tarjeta"""

    nombreTarjeta = input("Nombre: ")
    apellidoTarjeta = input("Apellido: ")
    numeroTarjeta = int(input("Tarjeta: "))
    codigoTarjeta = int(input("Codigo de seguridad: "))
    fechaCaducidadTarjeta = input("Fecha Caducidad: ")

    if Tarjeta.verificarTarjeta(numeroTarjeta):
        print("Numero de Tarjeta valido")
        if Tarjeta.verificarBloqueo(numeroTarjeta) == False:
            print("Tarjeta operativa")
            if Tarjeta.verificarCaducidad(fechaCaducidadTarjeta):
                print("Tarjeta vigente")
            else:
                print("Tarjeta vencida")
        else:
            print("Tarjeta bloqueada")
    else:
        print("Numero de Tarjeta invalido")