import json

class Usuario:

    def __init__(self,usuario,contrasenia,nombre,apellido,correo):
        self.usuario = usuario
        self.contrasenia = contrasenia
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo


    def verify_session(given_User, given_Password):
        with open("usuarios.json", "r") as f:
            usuario = json.load(f)

        for element in usuario:
            if element["usuario"] == given_User and element["contrasenia"] == given_Password:
                print("Bienvenido, " + element["nombre"])
                return Usuario(element["usuario"],element["contrasenia"],element["nombre"],element["apellido"],element["correo"])
            
            else:
                with open("admin_Datos.json", "r") as f:
                    usuario = json.load(f)

                for element in usuario:
                    if element["usuario"] == given_User and element["contrasenia"] == given_Password:
                        print("Bienvenido, " + element["nombre"])
                        return Usuario(element["usuario"],element["contrasenia"],element["nombre"],element["apellido"],element["correo"])



    def registrar(self):
        usern = dict(usuario = self.__usuario, contrasenia = self.__contrasenia, nombre = self.__nombre, apellido = self.__apellido, correo = self.__correo)
        
        with open("usuarios.json", "r") as f:
            data = json.load(f)

        data.append(usern)

        with open("usuarios.json", "w") as f:
            json.dump(data, f, indent=4)


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
OPCION: """

        opcion = int(input(menu))

        while opcion > 5 or opcion <1:
            print("Elija una opción valida")
            opcion = int(input(menu))

        if opcion == 1:
            dato = "usuario"

        elif opcion == 2:  
            contraseniaActual = input("Ingrese contrasenia actual: ")    

            while self.__contrasenia != contraseniaActual:
                print("Contrasenia incorrecta")
                contraseniaActual = input("Ingrese contrasenia actual: ")

            dato = "contrasenia"

        elif opcion == 3:
            dato = "nombre"
            
        elif opcion == 4:
            dato = "apellido"

        elif opcion == 5:
            dato = "correo"

        self.actualizar(dato)