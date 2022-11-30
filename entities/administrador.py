from entities.user import Usuario
from entities.habitacion import *
import json

class Administrador(Usuario):

    def __init__(self,usuario,contrasenia,nombre,apellido,correo, llaveMaestra):
        super().__init__(usuario,contrasenia,nombre,apellido,correo)
        self._llaveMaestra = llaveMaestra
       
    def actualizarContrasenia():
        
        admin_buscar = str(input("Ingrese su usuario:"))
        with open("admin_Datos.json", "r") as f:
            data = json.load(f)
        for admin in data:
            if admin["usuario"] == admin_buscar:
                admin_contrasenia = str(input("Ingrese su contrasenia actual:"))
                if admin_contrasenia==admin["contrasenia"]:

                    admin["contrasenia"] = input("Ingrese su nueva contrasenia: ")
                
                else:
                    print("Contrasenia incorrecta")
                    
        with open("admin_Datos.json", "w") as f:
            json.dump(data, f, indent=4)


    def registrarHab():
        print("A continuacion, digite las caracteristicas de la nueva habitacion:")
        estado = input("Estado: ")
        precio = float(input("Precio: "))
        a = 1
        while(a == 1):
            tipoHabitacion = input("Tipo de habitacion:")
            if(tipoHabitacion == 'Simple' or tipoHabitacion == 'Matrimonial' or tipoHabitacion == 'Triple' or tipoHabitacion == 'Doble'):
                a = 0
                
        numHabitacion = int(input("Numero de habitacion:"))
        new_Room= Habitacion(estado,precio,tipoHabitacion,numHabitacion)
        roomn = dict(estado = new_Room.estado, precio = new_Room.precio,tipoHabitacion = new_Room.tipoHabitacion,numHabitacion = new_Room.numHabitacion)
        
        with open("habitaciones_Registradas.json", "r") as f:
            data = json.load(f)

        data.append(roomn)

        with open("habitaciones_Registradas.json", "w") as f:
            json.dump(data, f, indent=4)
   
    def actualizar(dato):

        with open("habitaciones_Registradas.json", "r") as f:
            habitacionTemp = json.load(f)
        habitacion_buscar = int(input("Ingrese el numero de habitacion a editar:"))

        for element in habitacionTemp:
            if element["numHabitacion"] == habitacion_buscar:
                if dato == 'precio': 
                    element[dato] = float(input("Ingrese actualiazación de su " + dato +": "))
                else:
                    element[dato] = str(input("Ingrese actualiazación de su " + dato +": "))   
        with open("habitaciones_Registradas.json", "w") as f:
            json.dump(habitacionTemp, f, indent=4)

    def actualizarDatos():
        menu = """ACTUALIZAR
        1. Estado
        2. Precio
        3. Tipo de Habitacion
        OPCION: """

        opcion = int(input(menu))

        while opcion > 3 or opcion <1:
            print("Elija una opción valida")
            opcion = int(input(menu))

        if opcion == 1:
            dato = "estado"

        elif opcion == 2:  
            
            dato = "precio"

        elif opcion == 3:
            dato = "tipoHabitacion"
            
        Administrador.actualizar(dato)
