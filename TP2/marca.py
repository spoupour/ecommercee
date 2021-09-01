class Marca():
    def __init__(self,nombre_marca,codigos):
        self.nombre_marca=nombre_marca
        self.codigo_marca=codigos
    def get_nombre_marca(self):
        return self.nombre_marca
    def get_codigo_marca(self):
        return self.codigo_marca
    def set_codigo_marca(self,codigos):
        self.codigo_marca=codigos
    def set_nombre_marca(self,nombre_marca):
        self.nombre_marca=nombre_marca
