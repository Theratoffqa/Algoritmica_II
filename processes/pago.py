from werkzeug.security import check_password_hash
import uuid
import json
import datetime


class Pago: 
    
    def __init__(self,concepto,monto, metPago, cuenta):
        self._numOperacion = str(uuid.uuid4())
        self._concepto = concepto
        self._fecha = datetime.datetime.now() + datetime.datetime.time()
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
            if check_password_hash(element[key], str(self._metPago[1])):
                if element["monto"] > self._monto:
                    element["monto"] = element["monto"] - self._monto
                else:
                    monto_suficiente = False

        with open(file_path, "w") as f:
            json.dump(met_pago, f, indent=4)

        return monto_suficiente
    

    def registrarTransaccion(self):     
        RegistroPago = dict(numOperacion = self._numOperacion, concepto = self._concepto,fechaActual = self._fecha,monto = self._monto,metpago= self._metPago)

        with open("pagos.json", "r") as f:
            data = json.load(f)

        data.append(RegistroPago)

        with open("pagos.json", "w") as f:
            json.dump(data, f, indent=4)