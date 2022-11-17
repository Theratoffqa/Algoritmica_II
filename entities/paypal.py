from metodos import *
#import datetime
import json

class PayPal(Metodo):

    def __init__(self,correoPayPal,contraseniaPayPal):
        self.__correoPayPal = correoPayPal
        self.__contraseniaPayPal = contraseniaPayPal
        

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
                    
                    return True

            if verificado == True:
                print("***Error.Ingrese nuevamente los datos:***")

           
    def verificarCaducidad(self): #verificar si la cuenta está desactivada 
        pass
    
    def verificarBloqueo(self): #verificar banneada
        pass 

if __name__ == "__main__":

    primeravalidacion = PayPal.verificar()
