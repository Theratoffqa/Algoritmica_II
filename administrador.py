from user import Usuario
import json

class Administrador(Usuario):

    def __init__(self,usuario,contrasenia,nombre,apellido,correo, llaveMaestra):
        super().__init__(usuario,contrasenia,nombre,apellido,correo)
        self._contrasenia = contrasenia
       
    def actualizarDatos(user,contr):
        with open("usuarios.json", "r") as f:
            usuario = json.load(f)
        if element["usuario"] == user and element["contrasenia"] == contr: 
            Contra_actual = input("Contraseña actual : ")
            if Contra_actual == contr:
                Nuevo_correo = input("Nuevo correo: ")
                for element in usuario:
                    element["correo"] = Nuevo_correo
            else: 
                print("Contraseña no coincide")