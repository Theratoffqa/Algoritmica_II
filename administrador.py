from user import Usuario
from habitacion import Habitacion
import json

class Administrador(Usuario):

    def __init__(self,usuario,contrasenia,nombre,apellido,correo, llaveMaestra):
        super().__init__(usuario,contrasenia,nombre,apellido,correo)
        self._llaveMaestra = llaveMaestra
       
    def actualizarDatos(self):
        
        admin_buscar = str(input("Ingrese su usuario:"))
        with open("admin_Datos.json", "r") as f:
            data = json.load(f)
        for admin in data:
            if admin["usuario"] == admin_buscar:
                admin_contrasenia = str(input("Ingrese su contrasenia actual:"))
                if admin_contrasenia==admin["contrasenia"]:

                    admin["contrasenia"] = input("Ingrese su nueva contrasenia: ")
                
                    admin= Administrador(admin["nombre"],admin["apellido"],admin["usuario"],admin["contrasenia"],admin["correo"],admin["llave_maestra"])
                else:
                    print("Contrasenia incorrecta")
                    
        with open("admin_Datos.json", "w") as f:
            json.dump(data, f, indent=4)


    def registrarHab(self):
        print("A continuacion, digite las caracteristicas de la nueva habitacion:")
        estado = input("Estado: ")
        precio = int(input("Precio: "))
        tipoHabitacion = input("Tipo de habitacion:")
        numHabitacion = int(input("Numero de habitacion:"))
        new_Room= Habitacion(estado,precio,tipoHabitacion,numHabitacion)
        roomn = dict(estado = new_Room._estado, precio = new_Room._precio,tipoHabitacion = new_Room._tipoHabitacion,numHabitacion = new_Room._numHabitacion)
        
        with open("habitaciones_Registradas.json", "r") as f:
            data = json.load(f)

        data.append(roomn)

        with open("habitaciones_Registradas.json", "w") as f:
            json.dump(data, f, indent=4)

    def actualizarDatosHab(self):
        with open("habitaciones_Registradas.json", "r") as f:
            data = json.load(f)
        habitacion_busqueda = int(input("Ingrese el numero de habitacion que desea editar:")) 

        for habitacion in data:
            if habitacion["numHabitacion"] == habitacion_busqueda:
                print("Habitacion ANTES:",habitacion)
                habitacion["estado"] = input("Estado: ")
                habitacion["precio"] = int(input("Precio: "))
                habitacion["tipoHabitacion"] = input("Tipo de habitacion:")
                habitacion["numHabitacion"] = int(input("Numero de habitacion:"))
                print("Habitacion DESPUES:",habitacion)
                habitacion= Habitacion(habitacion["estado"],habitacion["precio"],habitacion["tipoHabitacion"],habitacion["numHabitacion"])
    

        with open("habitaciones_Registradas.json", "w") as f:
            json.dump(data, f, indent=4)
    

if __name__ == "__main__":
    adminTemp = Administrador("","","","","","")
    #adminTemp = administrador que ingresa al menu (cambiar cuando se incorpore el admin)
    menu="""
    1.- Registrar habitacion
    2.- Actualizar datos de habitacion
    3.- Actualizar contrasenia
    Elija una opcion: """
    option = int(input(menu))
    if option == 1:
       adminTemp.registrarHab()

    elif option == 2:

       
       adminTemp.actualizarDatosHab() 
       
    elif option==3:
        adminTemp.actualizarDatos()
        
    else:
        print("Opcion no valida") 