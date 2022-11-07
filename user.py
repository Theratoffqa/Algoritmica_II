import json

class Usuario:

    def __init__(self,usuario,contrasenia,nombre,apellido,correo):
        self._usuario = usuario
        self._contrasenia = contrasenia
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo

    def verify_session(given_User, given_Password):
        # for element in usuarios_Registrados:
        #     if given_User == element._usuario and given_Password == element._contrasenia:
        #         print("Bienvenido " + str(element._nombre))
        #     else:
        #         print("No tenemos registrado ese usuario, inténtelo nuevamente")
        #         Usuario.verify_session(given_User, given_Password)

        encontrado = False
        with open("usuarios.json", "r") as f:
            usuario = json.load(f)

        for element in usuario:
            if element["usuario"] == given_User and element["contrasenia"] == given_Password:
                print("Bienvenido, " + element["nombre"])
                encontrado = True
        
        if encontrado == False:
            print("No tenemos registrado ese usuario, inténtelo nuevamente")

# usuarios_Registrados = [
#     Usuario("JoseQC35","hola123","Jose","Quispe","jose.quispe35@unmsm.edu.pe")
# ]