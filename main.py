from user import *
import cliente, administrador

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
