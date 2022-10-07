
class Usuario:

    def __init__(self,usuario,contrasenia,nombre,apellido,correo):
        self._usuario = usuario
        self._contrasenia = contrasenia
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo

    def verify_session(given_User, given_Password):
        encontrado = False
        for element in usuarios_Registrados:
            if given_User == element.user and given_Password == element.password:
                encontrado = True
                return encontrado


class Cliente(Usuario):

    def __init__(self,usuario,contrasenia,nombre,apellido,correo, tarjeta):
        super().__init__(usuario,contrasenia,nombre,apellido,correo)
        
        self._tarjeta = tarjeta
        
    
    def registrarCliente(self):
        pass
    

    def actualizarDatos(self):
        pass

    
class Administrador(Usuario):

    def __init__(self,usuario,contrasenia,nombre,apellido,correo, llaveMaestra):
        super().__init__(usuario,contrasenia,nombre,apellido,correo)
        self._llaveMaestra = llaveMaestra
       
        

    def actualizarCatalogo(self):
        pass



usuarios_Registrados = [
    Usuario("JoseQC35","hola123","Jose","Quispe","jose.quispe35@unmsm.edu.pe")
]


if __name__ == "__main__":
    menu="""
1.- Iniciar Sesion
2.- Registrarse
Elija una opcion: """
    option = int(input(menu))
    if option == 1:
        user = input("Usuario: ")
        password = input("Contrasenia: ")
        if Usuario.verify_session(user, password):
            print("Hola " + str(user))
        else:
            print("No tenemos registrado ese usuario")

    elif option == 2:
        user = input("Ingrese nuevo usuario: ")
        password = input("Ingrese nueva contrasenia: ")
        name = input("Ingrese su nombre: ")
        lastname = input("Ingrese su apellido: ")
        mail = input("Ingrese su correo: ")
        new_User = Usuario(user, password, name, lastname, mail)
        usuarios_Registrados.append(new_User)

    else:
        print("Opcion no valida")


