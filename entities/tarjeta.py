from entities.metodos import Metodo
import datetime
import json

file_path = "tarjetas.json"

class Tarjeta(Metodo):

    def __init__(self,numTarjeta,fechCaducidad,codSeguridad,nomTarjeta,apellTarjeta,emisorTarjeta):
        self.__emisor = emisorTarjeta
        self._numTarjeta = numTarjeta
        self.__fechCaducidad = fechCaducidad
        self.__codSeguridad = codSeguridad
        self.__nombTarjeta = nomTarjeta
        self.__apellTarjeta = apellTarjeta

    def verificar(self):
        passed = False

        with open(file_path, "r") as f:
            tarjetas = json.load(f)

        for element in tarjetas:
            p = True if element["emisor"] == self.__emisor else False
            q = True if element["numTarjeta"] == self._numTarjeta else False
            r = True if datetime.datetime.strptime(self.__fechCaducidad, "%m/%Y") == datetime.datetime.strptime(element["fechCaducidad"], "%m/%Y") else False
            s = True if element["codSeguridad"] == self.__codSeguridad else False
            t = True if element["nombTarjeta"] == self.__nombTarjeta else False
            u = True if element["apellTarjeta"] == self.__apellTarjeta else False

            if p and q and r and s and t and u:
                passed = True

        return passed  
    
    def verificarCaducidad(self):
        passed = False
        fechaActual = datetime.datetime.now()
        fechaV = datetime.datetime.strptime(self.__fechCaducidad, "%m/%Y")

        if fechaV > fechaActual:
            passed = True

        return passed
    
    def verificarBloqueo(self):
        passed = False

        with open("numerobloqueado.json", "r") as f:
            numerosBloqueados = json.load(f)

        for element in numerosBloqueados:

            if element["numero"] == self._numTarjeta:
                passed = True

        return passed        
            

#NumerosBloqueados = [0000000000000000]