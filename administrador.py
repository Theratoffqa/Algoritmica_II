from user import Usuario
import json

class Administrador(Usuario):

    def __init__(self,usuario,contrasenia,nombre,apellido,correo, llaveMaestra):
        super().__init__(usuario,contrasenia,nombre,apellido,correo)
        self._llaveMaestra = llaveMaestra
       
    #def actualizarDatos(self):
        #editar solo la contraseña del admin
    #def registrarHab(self):
        #registrar una habitación desde 0
    #def actualizarDatosHab(self):
        #Actualizar los datos de la habitación
    
if __name__ == "__main__":        
        
        with open("admin_Datos.json", "r") as f:
            data = json.load(f)
        admin_buscar = str(input("Ingrese su usuario:")) 

        for admin in data:
            if admin["usuario"] == admin_buscar:
            
                admin["contrasenia"] = input("Ingrese su nueva contrasenia: ")
                
                admin= Administrador(admin["nombre"],admin["apellido"],admin["usuario"],admin["contrasenia"],admin["correo"],admin["llave_maestra"])
    
        data.append(admin)
        #for admin in data:
         #   print(admin)

        with open("admin_Datos.json", "w") as f:
            json.dump(data, f, indent=4)