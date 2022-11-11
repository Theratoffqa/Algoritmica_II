from user import *
from tarjeta import *
from habitacion import *
from administrador import *
import json

if __name__ == "__main__":
    menu="""
    ---------BIENVENIDOS AL HOTEL VIRUS PELUCHE----------

    1.- Iniciar Sesion
    2.- Registrarse
    Elija una opcion: """
    option = int(input(menu))
    if option == 1:
        user = input("      Usuario: ")
        password = input("      Contrasenia: ")
        usuarioEnSesion = Usuario.verify_session(user, password)

        while usuarioEnSesion == None:
            print("     No tenemos a ese usuario registrado, intentelo de nuevo")
            user = input("      Usuario: ")
            password = input("      Contrasenia: ")
            usuarioEnSesion = Usuario.verify_session(user, password)
            print(usuarioEnSesion)
        
        with open("usuarios.json", "r") as f:
            data = json.load(f)
        for element in data:
            if user == element["usuario"]:
                mensaje = element["correo"]
            else:
                with open("admin_Datos.json", "r") as f:
                    data = json.load(f)
                for element in data:
                    if user == element["usuario"]:
                        mensaje = element["correo"]

    
        verdad = str(mensaje.endswith("peluche.com"))

        if verdad =="True":
            
    
            llave_ingresada= input("Ingrese su llave maestra para acceder al menu:")
    
            with open("admin_Datos.json", "r") as f:
                data = json.load(f)

            for admin in data:
                if admin["llave_maestra"]==llave_ingresada:
                    
                    menu="""
                    1.- Registrar habitacion
                    2.- Actualizar datos de habitacion
                    3.- Actualizar contrasenia
                    4.- Buscar habitacion y mostrar datos
                    5.- Mostrar catalogo de habitaciones
                    Elija una opcion: """
                    option = int(input(menu))
                    if option == 1:
                        Administrador.registrarHab()

                    elif option == 2:
                        Administrador.actualizarDatos() 

                    elif option==3:
                        Administrador.actualizarContrasenia()

                    elif option==4:
                        Habitacion.buscarHabitacion()

                    elif option==5:
                        Habitacion.mostrarDatos()

                    else:
                        print("Opcion no valida")
            

        else:
            menu = """
            1.- Actualizar Datos
            2.- Comprar
            Elija una opcion: """

            op = int(input(menu))
            
            if op == 1:
                usuarioEnSesion.actualizarDatos()
            elif op == 2:
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


    elif option == 2:
        user = input("Ingrese nuevo usuario: ")
        password = input("Ingrese nueva contrasenia: ")
        name = input("Ingrese su nombre: ") 
        lastname = input("Ingrese su apellido: ")
        mail = input("Ingrese su correo: ")
        new_User = Usuario(user, password, name, lastname, mail)
        new_User.registrar()

    else:
        print("Opcion no valida")
