from user import Usuario

class Administrador(Usuario):

    def __init__(self,usuario,contrasenia,nombre,apellido,correo, llaveMaestra):
        super().__init__(usuario,contrasenia,nombre,apellido,correo)
        self._llaveMaestra = llaveMaestra
       
        

    def actualizarCatalogo(self):
        pass