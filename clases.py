class Usuario:

    def __init__(self,usuario,contrasenia,nombre,apellido,correo):
        self._usuario = usuario
        self._contrasenia = contrasenia
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo

    def iniciarSesion(self):
        pass

    def verificarSesion(self):
        pass


class Cliente(Usuario):

    def __init__(self,tarjeta):
        
        self._tarjeta = tarjeta
        
    
    def registrarCliente(self):
        pass
    

    def actualizarDatos(self):
        pass

    
class Administrador(Usuario):

    def __init__(self,llaveMaestra):
        self._llaveMaestra = llaveMaestra
       
        

    def actualizarCatalogo(self):
        pass
    

class Pago: 
    
    def __init__(self,numOperacion,concepto,dni,fecha,monto):
        self._numOperacion = numOperacion
        self._concepto = concepto
        self._dni = dni 
        self._fecha = fecha
        self._monto = monto


    def registrarTransaccion(self):
        pass



class Reserva:
    
    def __init__(self,codReserva,fechaEnt,fechaSal,numDias,cantPersonas): 
        self._codReserva = codReserva
        self._fechaEnt = fechaEnt
        self._fechaSal = fechaSal
        self._numDias = numDias
        self._cantPersonas = cantPersonas

        
    def reservar(self):
        pass


    def cambiarEstado(self):
        pass


    def mostrarReserva(self):
        pass

    def verificarEstadoHabitacion(self):
        pass
    

class Habitacion:
    
    def __init__(self,estado,precio,tipoHabitacion,numHabitacion): 
        self._estado = estado
        self._precio = precio
        self._tipoHabitacion = tipoHabitacion
        self._numHabitacion = numHabitacion

    def mostrarDatos(self):
        pass


