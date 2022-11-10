from user import Usuario

class Cliente(Usuario):

    def __init__(self,usuario,contrasenia,nombre,apellido,correo):
        super().__init__(usuario,contrasenia,nombre,apellido,correo)
            
    
    def registrarCliente(self):
        
        pass
    

    def actualizarDatos(self):
        pass