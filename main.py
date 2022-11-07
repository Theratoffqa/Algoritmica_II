from user import *
import json

if __name__ == "__main__":
    menu="""
1.- Iniciar Sesion
2.- Registrarse
Elija una opcion: """
    option = int(input(menu))
    if option == 1:
        user = input("Usuario: ")
        password = input("Contrasenia: ")
        Usuario.verify_session(user, password)

    elif option == 2:
        user = input("Ingrese nuevo usuario: ")
        password = input("Ingrese nueva contrasenia: ")
        name = input("Ingrese su nombre: ") 
        lastname = input("Ingrese su apellido: ")
        mail = input("Ingrese su correo: ")
        new_User = Usuario(user, password, name, lastname, mail)
        #usuarios_Registrados.append(new_User)
        usern = dict(usuario = new_User._usuario, contrasenia = new_User._contrasenia, nombre = new_User._nombre, apellido = new_User._apellido, correo = new_User._correo)
        
        with open("usuarios.json", "r") as f:
            data = json.load(f)

        data.append(usern)

        with open("usuarios.json", "w") as f:
            json.dump(data, f, indent=4)

    else:
        print("Opcion no valida")
