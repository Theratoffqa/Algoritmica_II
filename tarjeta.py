import datetime
import json

class Tarjeta:

    def _init_(self,numTarjeta,fechCaducidad,codSeguridad,nomTarjeta,apellTarjeta,emisorTarjeta):
        self._emisor = emisorTarjeta
        self._numTarjeta = numTarjeta
        self._fechCaducidad = fechCaducidad
        self._codSeguridad = codSeguridad
        self._nombTarjeta = nomTarjeta
        self._apellTarjeta = apellTarjeta

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



if __name__ == "__main__":
    menu="""Ingresar tarjeta"""

    nombreTarjeta = input("Nombre: ")
    apellidoTarjeta = input("Apellido: ")
    numeroTarjeta = int(input("Tarjeta: "))

    while len(str(numeroTarjeta)) != 16:
        print("El numero de tarjeta debe contener 16 digitos")
        numeroTarjeta = int(input("Tarjeta: "))

    codigoTarjeta = int(input("Codigo de seguridad (CVV): "))

    while len(str(codigoTarjeta)) != 3:
        print("El codigo de verificación debe contener 3 digitos")
        codigoTarjeta = int(input("Tarjeta: "))

    emisorTarjeta = input("Emisor: ")
    fechaCaducidadTarjeta = input("Fecha Caducidad: ")

    if Tarjeta.verificarTarjeta(emisorTarjeta,numeroTarjeta,fechaCaducidadTarjeta,codigoTarjeta,nombreTarjeta,apellidoTarjeta):
        print("Tarjeta valida")

        if Tarjeta.verificarBloqueo(numeroTarjeta) == False:
            print("Tarjeta operativa")

            if Tarjeta.verificarCaducidad(fechaCaducidadTarjeta):
                print("Tarjeta vigente")

            else:
                print("Tarjeta vencida")

        else:
            print("Tarjeta bloqueada")

    else:
        print("Tarjeta no valida, por favor ingres bien los datos")