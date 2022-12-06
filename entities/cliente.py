from entities.user import Usuario
import json

class Cliente(Usuario):

    def __init__(self,usuario,contrasenia,nombre,apellido, correo, metPago, pago):
        super().__init__(usuario,contrasenia,nombre,apellido,correo)

        self._metPago = metPago
        self._pago = pago
            
    
    def registrarCliente(self):          
        usercliente = dict(usuario = self._usuario, contrasenia = self._contrasenia, nombre = self._nombre, apellido = self._apellido, correo = self._correo, metpago = self._metPago, pago = self._pago)

        with open("clientes.json", "r") as f:
            client = json.load(f)

        client.append(usercliente)

        with open("clientes.json", "w") as f:
            json.dump(client, f, indent=4)

        #for element in usuarios:
        #    if element["usuario"] == user:
        #        usuarios.append(usercliente)

                #element["metPago"] = self._metPago
                #try:
                #   element["registros"].append(self._pago)
                #except KeyError:
                #    element["registros"] = []
                #    element["registros"].append(self._pago)
        #with open("clientes.json", "r") as f:
        #    data = json.load(f)
        #data.append(usercliente)
      
            
    def actualizar(self, dato):
        with open("usuarios.json", "r") as f:
            usuarios = json.load(f)

        for element in usuarios:
            if element["usuario"] == self.__usuario:
                element[dato] = input("Ingrese actualiazación de su " + dato +": ")

        with open("usuarios.json", "w") as f:
            json.dump(usuarios, f, indent=4)

            
    def actualizarDatos(self):
        menu = """ACTUALIZAR
    1. Usuario
    2. Contraseña
    3. Nombre
    4. Apellido
    5. Correo
    6. Metodo de Pago Predeterminado
OPCION: """

        opcion = int(input(menu))

        while opcion > 5 and opcion <1:
            print("Elija una opción valida")
            opcion = int(input(menu))

        if opcion == 1:
            dato = "usuario"

        elif opcion == 2:  
            contraseniaActual = input("Ingrese contrasenia actual: ")    

            while self._contrasenia != contraseniaActual:
                print("Contrasenia incorrecta")
                contraseniaActual = input("Ingrese contrasenia actual: ")

            dato = "contrasenia"

        elif opcion == 3:
            dato = "nombre"
            
        elif opcion == 4:
            dato = "apellido"

        elif opcion == 5:
            dato = "correo"

        elif opcion == 6:
            dato = "metPago"

        self.actualizar(dato)