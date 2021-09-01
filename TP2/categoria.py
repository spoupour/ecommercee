class Categoria():
    def __init__(self,codigos2, nombre_categoria, descripcion):
        self.nombre_categoria=nombre_categoria
        self.descripcion=descripcion
        self.codigo_categoria=codigos2

    def get_nombre_categoria(self):
        return self.nombre_categoria
    def set_nombre_categoria(self,nombre_categoria):
        self.nombre_categoria=nombre_categoria
    def get_descripcion(self):
        return self.descripcion
    def set_descripcion(self,descripcion):
        self.descripcion=descripcion
    def get_codigo_categoria(self):
        return self.codigo_categoria
    def set_codigo_categoria(self,codigos2):
        self.codigo_categoria=codigos2
