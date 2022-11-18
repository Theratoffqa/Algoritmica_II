from entities.user import *
from entities.tarjeta import *
from entities.habitacion import *
from entities.administrador import *
from entities.cliente import *
from entities.paypal import *

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
                Habitacion.mostrarDatos()
                print("*Se elige uno*")

                menuPago = """
                Seleccione el metodo de pago:
                1.- Tarjeta VISA/Mastercard
                2.- PayPal
                Elija una opcion: """

                opSelec = int(input(menuPago))
                
                if opSelec == 1:
                    metPago = "Tarjeta"
                    print("Ingresar los datos de la tarjeta:")
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

                    tarjetaIngresada = Tarjeta(numeroTarjeta,fechaCaducidadTarjeta,codigoTarjeta,nombreTarjeta,apellidoTarjeta,emisorTarjeta)

                    if tarjetaIngresada.verificar():
                        print("Tarjeta valida")

                        if tarjetaIngresada.verificarBloqueo() == False:
                            print("Tarjeta operativa")

                            if tarjetaIngresada.verificarCaducidad():
                                print("Tarjeta vigente")

                                print("*Paga*")

                            else:
                                print("Tarjeta vencida")

                        else:
                            print("Tarjeta bloqueada")

                    else:
                        print("Tarjeta no valida, por favor ingres bien los datos")
                
                elif opSelec == 2:
                    metPago = "PayPal"
                    primeravalidacion = PayPal.verificar()
                    segundavalidacion = PayPal.verificarCaducidad(PayPal, primeravalidacion)
                    terceravalidacion = PayPal.verificarBloqueo(PayPal, primeravalidacion)

                    if segundavalidacion  != False and terceravalidacion !=False:
                        print("*** Pago exitoso =) ***")

                pago = "ejemplopago001" 
                nuevo_cliente = Cliente(usuarioEnSesion._usuario, usuarioEnSesion._contrasenia, usuarioEnSesion._nombre, usuarioEnSesion._apellido, usuarioEnSesion._correo, metPago, pago)
                nuevo_cliente.registrarCliente()   


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
