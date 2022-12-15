from werkzeug.security import check_password_hash
import json
import datetime


class Pago:

    def __init__(self, numOperacion, concepto, fecha, monto, metPago, cuenta):
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
            if check_password_hash(element[key], str(self._metPago[1])):
                if element["monto"] > self._monto:
                    element["monto"] = element["monto"] - self._monto
                else:
                    monto_suficiente = False

        with open(file_path, "w") as f:
            json.dump(met_pago, f, indent=4)

        return monto_suficiente

    def numeroOperacion(monto):
        n = 0
        if monto > 0:
            y = n + 1
            n = y
        if y < 10:
            print("0000" + y)
        elif y >= 10 and y < 100:
            print("000" + y)
        elif y >= 100 and y < 1000:
            print("00" + y)
        elif y >= 1000 and y < 10000:
            print("0" + y)
        elif y >= 10000 and y < 100000:
            print(y)
        return y

    def conceptoOperacion(numHabitacion):
        with open("habitaciones_Registradas.json", "r") as f:
            habitaciones = json.load(f)
            for element in habitaciones:
                if numHabitacion == element["numHabitacion"]:
                    conceptoPago = element["tipoHabitacion"]
                    return conceptoPago

    def montoOperacion(numHabitacion):
        with open("habitaciones_Registradas.json", "r") as f:
            habitaciones = json.load(f)
            for element in habitaciones:
                if numHabitacion == element["numHabitacion"]:
                    montoOperacion = element["precio"]
                    return montoOperacion

    def fechaOperacion(self):
        self._fecha = print(datetime.datetime.now() + datetime.datetime.time())

    def registrarTransaccion(self):
        RegistroPago = dict(numOperacion = self._numOperacion, concepto = self._concepto, fechaActual = self._fecha, monto = self._monto, metpago= self._metPago)
        with open("pagos.json", "r") as f:
            data = json.load(f)
        data.append(RegistroPago)
        with open("pagos.json", "w") as f:
            json.dump(data, f, indent=4)
