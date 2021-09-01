class Alerta():
    def __init__(self,codigos,fecha,codigo_prod,cliente_id):
        self.codigo_alerta=0
        self.fecha=fecha
        self.codigo_prod=codigo_prod
        self.cliente_id=cliente_id
    #getters
    def get_codigo_alerta(self):
        return self.codigo_alerta
    def get_fecha(self):
        return self.fecha
    def get_codigo_prod(self):
        return self.codigo_prod
    def get_cliente_id(self):
        return self.cliente_id
    #setters
    def set_codigo_alerta(self,codigos):
        self.codigo_alerta=codigos
    def set_codigo_prod(self,codigo_prod):
        self.codigo_prod=codigo_prod
    def set_fecha(self,fecha):
        self.fecha=fecha 
    def set_cliente_id(self,cliente_id):
        self.cliente_id=cliente_id