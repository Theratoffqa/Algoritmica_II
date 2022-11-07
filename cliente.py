from user import Usuario

class Cliente(Usuario):

    def __init__(self,usuario,contrasenia,nombre,apellido,correo, tarjeta):
        super().__init__(usuario,contrasenia,nombre,apellido,correo)
        
        self._tarjeta = tarjeta
        
    
    def registrarCliente(self):
        pass
    

    def actualizarDatos(self):
        pass