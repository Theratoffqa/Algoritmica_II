class Pago: 
    
    def __init__(self,numOperacion,concepto,dni,fecha,monto):
        self._numOperacion = numOperacion
        self._concepto = concepto
        self._dni = dni 
        self._fecha = fecha
        self._monto = monto


    def registrarTransaccion(self):
        pass