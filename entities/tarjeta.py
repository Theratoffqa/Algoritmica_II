import datetime
import json

class Tarjeta:

    def __init__(self,numTarjeta,fechCaducidad,codSeguridad,nomTarjeta,apellTarjeta,emisorTarjeta):
        self.__emisor = emisorTarjeta
        self._numTarjeta = numTarjeta
        self.__fechCaducidad = fechCaducidad
        self.__codSeguridad = codSeguridad
        self.__nombTarjeta = nomTarjeta
        self.__apellTarjeta = apellTarjeta

    def verificarTarjeta(emisorTarjeta,numeroTarjeta,fechaCaducidadTarjeta,codigoTarjeta,nombreTarjeta,apellidoTarjeta):
        passed = False

        with open("tarjetas.json", "r") as f:
            tarjetas = json.load(f)

        for element in tarjetas:
            p = True if element["emisor"] == emisorTarjeta else False
            q = True if element["numTarjeta"] == numeroTarjeta else False
            r = True if datetime.datetime.strptime(fechaCaducidadTarjeta, "%m/%Y") == datetime.datetime.strptime(element["fechCaducidad"], "%m/%Y") else False
            s = True if element["codSeguridad"] == codigoTarjeta else False
            t = True if element["nombTarjeta"] == nombreTarjeta else False
            u = True if element["apellTarjeta"] == apellidoTarjeta else False

            if p and q and r and s and t and u:
                passed = True

        return passed  
    
    def verificarCaducidad(fechaVenci):
        passed = False
        fechaActual = datetime.datetime.now()
        fechaV = datetime.datetime.strptime(fechaVenci, "%m/%Y")

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