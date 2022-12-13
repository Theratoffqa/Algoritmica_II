from entities.user import Usuario
import datetime
import json

file_path = "habitaciones_Registradas.json"
file_path2 = "clientes.json"


class Pago: 
    
    def __init__(self,nombre,apellido,numOperacion,concepto,fecha,monto,metpago):
        self._numOperacion = numOperacion
        self._concepto = concepto
        self._fecha = fecha
        self._monto = monto
        self._metpago = metpago
        #[tarjeta, PayPal]

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

