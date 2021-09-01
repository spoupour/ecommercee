class Comprar():
    def __init__(self,cliente_id, codigo_producto,metodo_pago,detalles,fecha):
        self.cliente_id=cliente_id
        self.codigo_producto=codigo_producto
        self.metodo_pago=metodo_pago
        self.num_compra=0
        self.detalles=detalles
        self.fecha=fecha
    def get_cliente_id(self):
        return self.cliente_id
    def get_codigo_producto(self):
        return self.codigo_producto
    def get_metodo_pago(self):
        return self.metodo_pago
    def get_num_compra(self):
        return self.num_compra
    def get_detalles(self):
        return self.detalles
    def get_fecha(self):
        return self.fecha

    def set_cliente_id(self,cliente_id):
        self.cliente_id=id_cliente
    def set_codigo_producto(self,codigo_producto):
        self.codigo_producto=codigo_producto
    def set_metodo_pago(self,metodo_pago):
        self.metodo_pago=metodo_pago
    def set_num_compra(self,num_compra):
        self.num_compra=num_compra
    def set_detalles(self,detalles):
        self.detalles=detalles
    def set_fecha(self,fecha):
        self.fecha=fecha
         
         
         
    
