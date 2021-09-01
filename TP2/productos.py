from categoria import Categoria
from marca import Marca
class Productos():
    def __init__ (self, codigos, nombre_producto, precio, codigo_categoria,codigo_marca,detalles,stock,id_cliente):
        self.prod_codigo=0
        self.nombre_producto=nombre_producto
        self.precio=precio
        self.codigo_categoria=codigo_categoria
        self.codigo_marca=codigo_marca
        self.detalles=detalles
        self.stock=stock
        self.id_cliente=id_cliente
    
    def get_codigo_categoria(self):
        return self.codigo_categoria
    
    def get_nombre_producto(self):
        return self.nombre_producto
    
    def get_precio(self):
        return self.precio
    def get_prod_codigo(self):
        return self.prod_codigo
    def get_codigo_marca(self):
        return self.codigo_marca
    def get_detalles(self):
        return self.detalles
    def get_stock(self):
        return self.stock
    def get_id_cliente(self):
        return self.id_cliente
    def set_prod_codigo(self,prod_codigo):
        self.prod_codigo=codigos
    def set_nombre_producto(self,nombre_producto):
        self.nombre_producto=nombre_producto
    def set_precio(self,precio):
        self.precio=precio
    def set_codigo_categoria(self,codigo_categoria):
        self.codigo_categoria=codigo_categoria
    def set_codigo_marca(self,codigo_marca):
        self.codigo_marca=codigo_marca
    def set_detalles(self,detalles):
        self.detalles=detalles
    def set_stock(self,stock):
        self.stock=stock
    def set_id_cliente(self,id_cliente):
        self.id_cliente=id_cliente
            
           


