from user import *
from tarjeta import *
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
        if Usuario.verify_session(user, password):
            print("*Se muestran los hoteles*")
            print("*Se elige uno*")
            print("Ingresar los datos:")
            nombreTarjeta = input("Nombre: ")
            apellidoTarjeta = input("Apellido: ")
            numeroTarjeta = int(input("Tarjeta: "))

            while len(str(numeroTarjeta)) != 16:
                print("El numero de tarjeta debe contener 16 digitos")
                numeroTarjeta = int(input("Tarjeta: "))

            codigoTarjeta = int(input("Codigo de seguridad (CVV): "))

            while len(str(codigoTarjeta)) != 3:
                print("El codigo de verificación debe contener 3 digitos")
                codigoTarjeta = int(input("Tarjeta: "))

            emisorTarjeta = input("Emisor: ")
            fechaCaducidadTarjeta = input("Fecha Caducidad: ")

            if Tarjeta.verificarTarjeta(emisorTarjeta,numeroTarjeta,fechaCaducidadTarjeta,codigoTarjeta,nombreTarjeta,apellidoTarjeta):
                print("Tarjeta valida")

                if Tarjeta.verificarBloqueo(numeroTarjeta) == False:
                    print("Tarjeta operativa")

                    if Tarjeta.verificarCaducidad(fechaCaducidadTarjeta):
                        print("Tarjeta vigente")

                        print("*Paga*")

                    else:
                        print("Tarjeta vencida")

                else:
                    print("Tarjeta bloqueada")

            else:
                print("Tarjeta no valida, por favor ingres bien los datos")
        else:
            print("No tenemos registrado ese usuario, inténtelo nuevamente")

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
