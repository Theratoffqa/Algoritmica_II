from user import Usuario
import json

class Cliente(Usuario):

    def __init__(self,usuario,contrasenia,nombre,apellido, correo, metPago, pago):
        super().__init__(usuario,contrasenia,nombre,apellido,correo)

        self._metPago = metPago
        self._pago = pago
            
    
    def registrarCliente(self):
        with open("usuarios.json", "r") as f:
            usuarios = json.load(f)

        for element in usuarios:
            if element["usuario"] == self._usuario:
                element["metPago"] = self._metPago
                try:
                    element["registros"].append(self._pago)
                except KeyError:
                    element["registros"] = []
                    element["registros"].append(self._pago)
        
        with open("usuarios.json", "w") as f:
            json.dump(usuarios, f, indent=4)
         

    def actualizarDatos(self, dato):
        with open("usuarios.json", "r") as f:
            usuarios = json.load(f)

        for element in usuarios:
            if element["usuario"] == self._usuario:
                element[dato] = input("Ingrese actuliazación de su " + dato +": ")

        with open("usuarios.json", "w") as f:
            json.dump(usuarios, f, indent=4)

if __name__ == "__main__":

    newClient = Cliente("JoxSam35","hola123","Jose","Quispe","joxsam@gmail.com", "4009423705981980", "Pago001")

    newClient.registrarCliente()

    menu=""" ACTUALIZAR:
1. Usuario
2. Contraseña
3. Nombre
4. Apellido
5. Correo
6. Metodo de pago Predeterminado
        """
    opcion = int(input(menu))

    while opcion > 6 and opcion <1:
        print("Elija una opción valida")
        opcion = int(input(menu))
        
    if opcion == 1:
        dato = "usuario"
    elif opcion == 2:
        dato = "contrasenia"
    elif opcion == 3:
        dato = "nombre"
    elif opcion == 4:
        dato = "apellido"
    elif opcion == 5:
        dato = "correo"
    elif opcion == 6:
        dato = "metPago"

    newClient.actualizarDatos(dato)