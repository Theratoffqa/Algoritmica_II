from entities.metodos import *
import json

class PayPal(Metodo):

    def __init__(self,correoPayPal,contraseniaPayPal,estado):
        self.__correoPayPal = correoPayPal
        self.__contraseniaPayPal = contraseniaPayPal
        self.__estado = estado

    def verificar(): #verificar correo y contrasenia
        print('----------------------PAYPAL----------------------')
        verificado = True
        while verificado == True:
            correoPayPal = str(input("Ingrese su correo:"))
            contraseniaPayPal = str(input("Ingrese su contrasenia:"))
            
            with open("cuentasPayPal.json", "r") as f:
                usuarioPayPal = json.load(f)
            for element in usuarioPayPal:
                if element["correoPayPal"] == correoPayPal and element["contraseniaPayPal"] == contraseniaPayPal:
                    verificado = False
                    
                    return correoPayPal

            if verificado == True:
                print("***Error.Ingrese nuevamente los datos:***")
                return correoPayPal
           
    def verificarCaducidad(self,correoPayPal): #verificar si la cuenta está desactivada 
        
        with open("cuentasPayPal.json", "r") as f:
            usuarioPaypal = json.load(f)
        for element in usuarioPaypal:
            if element["correoPayPal"] == correoPayPal:
                if element["estado"] == "inactiva":
                    print("***Su cuenta se encuentra inactiva.***")
                    return False
    
    def verificarBloqueo(self,correoPayPal): #verificar banneada
        with open("cuentasSuspendidas.json", "r") as f:
            usuarioPaypal = json.load(f)
        for element in usuarioPaypal:
            if element["correoPayPal"] == correoPayPal:
                print("***Cuenta bloqueada. Use otra cuenta.***") 
                return False


        
