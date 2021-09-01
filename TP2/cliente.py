import base64 
class Cliente():
    def __init__(self,ids,usuario, nombre, apellido, contraseña, email):
        self.usuario=usuario
        self.nombre=nombre
        self.apellido=apellido
        self.contraseña=base64.b64encode(bytes(contraseña, 'utf-8'))
        self.email=email
        self.id_cliente=ids

    def get_usuario(self):
        return self.usuario
    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido
    def get_contraseña(self):
        return self.contraseña
    def get_email(self):
        return self.email
    def set_usuario(self,usuario):
        self.usuario=usuario
    def set_nombre(self,nombre):
        self.nombre=nombre
    def set_apellido(self,apellido):
        self.apellido=apellido
    def set_contraseña(self,contraseña):
        self.contraseña=base64.b64encode(bytes(contraseña, 'utf-8'))
    def set_email(self,email):
        self.email=email
    def get_id_cliente(self):
        return self.id_cliente
    def set_id_cliente(self,ids):
        self.id_cliente=ids
     
    
   
