from entities.user import Usuario
import json

file_path = "clientes.json"

class Cliente(Usuario):

    def __init__(self,usuario,contrasenia,nombre,apellido, correo, metPago, pago):
        super().__init__(usuario,contrasenia,nombre,apellido,correo)

        self._metPago = metPago
        self._pago = pago
            
    
    def registrar(self):          

        with open(file_path, "r") as f:
            client = json.load(f)

        registrado = False

        for element in client:    
            if element["usuario"] == self._usuario:
                registrado = True
                element["metpago"] = self._metPago
                element["pago"].append(self._pago)

        if registrado == False:
            file_path2 = "usuarios.json"

            with open(file_path2, "r") as f:
                usuarios = json.load(f)

            for element in usuarios:    
                if element["usuario"] == self._usuario:
                    usuarios.remove(element)

            with open(file_path2, "w") as f:
                json.dump(usuarios, f, indent=4)
            

            usercliente = dict(usuario = self._usuario, contrasenia = self._contrasenia, nombre = self._nombre, apellido = self._apellido, correo = self._correo, metpago = self._metPago, pago = [])
            usercliente["pago"].append(self._pago)
            client.append(usercliente)

        with open(file_path, "w") as f:
            json.dump(client, f, indent=4)

            
    def actualizar(self, dato):
        with open(file_path, "r") as f:
            usuarios = json.load(f)

        for element in usuarios:
            if element["usuario"] == self.__usuario:
                element[dato] = input("Ingrese actualiazación de su " + dato +": ")

        with open(file_path, "w") as f:
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