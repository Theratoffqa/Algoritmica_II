from werkzeug.security import check_password_hash
import json

class Pago: 
    
    def __init__(self,numOperacion,concepto,fecha,monto, metPago, cuenta):
        self._numOperacion = numOperacion
        self._concepto = concepto
        self._fecha = fecha
        self._monto = monto
        self._metPago = [metPago, cuenta]


    def pagar(self):
        monto_suficiente = True

        if "Tarjeta" in self._metPago[0]:
            key = "numTarjeta"
            file_path = "tarjetas.json"
        else:
            key = "correoPayPal"
            file_path = "cuentasPayPal.json"

        with open(file_path, "r") as f:
            met_pago = json.load(f)

        for element in met_pago:    
            if check_password_hash(element[key],str(self._metPago[1])):
                if element["monto"] > self._monto:
                    element["monto"] = element["monto"] - self._monto
                else:
                    monto_suficiente = False

        with open(file_path, "w") as f:
            json.dump(met_pago, f, indent=4)

        return monto_suficiente


    def registrarTransaccion(self):
        #numero de operacion
        if self._monto > 0:
            n = n + 1
        numOperacion = n


        #fecha actual
        fechaActual = datetime.datetime.now()

        #concepto de pago
        with open(file_path,"r") as f:
            habitaciones = json.load(f)
            for element in habitaciones:
                if self._concepto == element["tipoHabitacion"]:
                    conceptoPago = element["tipoHabitacion"]
        
        #metodo de pago
        with open(file_path2, "r") as f:
            metPagoClientes = json.load(f)
            for element in metPagoClientes:
                if self._metpago == element["metpago"]:
                    metPago = element["metpago"]
        
        RegistroPago = dict(nombre = self._nombre,apellido = self._apellido, numOperacion = self._numOperacion,concepto = self._concepto,fechaActual = self._fecha,monto = self._monto,metpago= self._metpago)
        with open(file_path3, "r") as f:
            data = json.load(f)
        data.append(RegistroPago)
        with open(file_path3, "w") as f:
            json.dump(data, f, indent=4)

