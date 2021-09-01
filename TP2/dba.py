import mysql.connector
from db import dbconf, queries
from productos import *
from categoria import *
from marca import Marca
from metodo import *
from comprar import Comprar
from cliente import Cliente
from vender import Vender
from alerta import Alerta
import os
from datetime import datetime, date, timedelta
from base64 import encodebytes, decodebytes
import time
import random
class Database():
  
    def __init__(self):
        self.conexion = mysql.connector.connect(**dbconf)
        self.cursor = self.conexion.cursor()
    #CLIENTE
    def crear_cliente(self,Cliente):
        email=Cliente.get_email()
        if self.buscar_usuario(email)==None:
            val=(Cliente.get_usuario(),Cliente.get_nombre(),Cliente.get_apellido(),Cliente.get_contraseña(),Cliente.get_email())
            self.cursor.execute(queries['add_cliente'],val,)
            self.conexion.commit()
            Cliente.set_id_cliente(self.cursor.lastrowid)
            print("ok")
        else:
            print("el cliente que quieres agregar ya existe")
    def traer_usuario(self,Cliente):
        self.cursor.execute(queries['get_user'],(Cliente.get_id_cliente(),))
        reporte=self.cursor.fetchall()
        return reporte
    def traer_id2(self,email):
        self.cursor.execute(queries['get_user'],(email,))
        reporte=self.cursor.fetchall()
        return reporte
    def traer_id(self,usuario,Cliente):
        val=Cliente.get_usuario(usuario)
        self.cursor.execute(queries['consultar_id'],val,)
        reporte=self.cursor.fetchall()
        return reporte
    def traer_contra(self,id):
        self.cursor.execute(queries['get_contra'],(id,))
        reporte=self.cursor.fetchone()
        return reporte
    def buscar_cliente(self,email):
        self.cursor.execute(queries['get_user'],(email,))
        reporte=self.cursor.fetchone()
        return reporte
    def cliente_conid(self,id):
        self.cursor.execute(queries['cliente_conid'],(id,))
        reporte=self.cursor.fetchone()
        return reporte
    def traer_usuario(self,id):
        self.cursor.execute(queries['traer_usuario'],(id,))
        reporte=self.cursor.fetchone()
        return reporte
    def consultar_cliente(self,email):
        self.cursor.execute(queries['consultar_cliente'],(email,))
        reporte=self.cursor.fetchone()
        return reporte
    def buscar_usuario(self,email):
        self.cursor.execute(queries['get_usuario'],(email,))
        reporte=self.cursor.fetchone()
        if reporte != None:
            return Cliente(*reporte)
    def buscar_usuarioo(self,usuario):
        self.cursor.execute(queries['get_usuarioo'],(usuario,))
        reporte=self.cursor.fetchone()
        return reporte
    def buscar_contraseña(self,email):
        self.cursor.execute(queries['get_contraseña'],(email,))
        reporte=self.cursor.fetchone()
        return reporte
    def clave_desencriptada(self,contraa):
        contraa=[contraa]
        contra=(contraa[0][0])
        #lo desencripta(decodebytes) y lo pasa a bytes(encode).
        contra=decodebytes(contra.encode())
        return contra
    def login(self, email, contraseña):
        val.validar_mail(email)
        val.password_check(contraseña)
        if db.buscar_cliente(email)==None:
            print("El cliente no está en la base de datos")
        Cliente.check_password(contraseña)
    #updates de los datos del ciente
    def cambiar_usuario(self,usuario,id):
        val=(usuario,id)
        self.cursor.execute(queries['update_usuario'],val,)
        self.conexion.commit()
    def cambiar_nombre(self,nombre,id):
        val=(nombre,id)
        self.cursor.execute(queries['update_nombre'],val,)
        self.conexion.commit()
    def cambiar_apellido(self,apellido,id):
        val=(apellido,id)
        self.cursor.execute(queries['update_apellido'],val,)
        self.conexion.commit()
    def cambiar_contraseña(self,contraseña,id):
        val=(contraseña,id)
        self.cursor.execute(queries['update_contraseña'],val,)
        self.conexion.commit()
    def cambiar_email(self,email,id):
        val=(email,id)
        self.cursor.execute(queries['update_email'],val,)
        self.conexion.commit()
    #borrar usuario
    def borrar_usuario(self,id):
        self.cursor.execute(queries['borrar_usuario'],(id,))
        self.conexion.commit()
    #PRODUCTOS
    #trae codigo del producto
    def traer_producto(self,Producto):
        self.cursor.execute(queries['get_product'],(Producto.get_prod_codigo(),))
        reporte=self.cursor.fetchall()
        return reporte
    
    def traer_productos(self):
        self.cursor.execute(queries['nombre_producto'])
        reporte=self.cursor.fetchall()
        return reporte
    #trae todos los productos
    def todos_productos(self):
        self.cursor.execute(queries['todos_productos'])
        reporte=self.cursor.fetchall()
        return reporte
    def buscar_codproducto(self,cod):
        self.cursor.execute(queries['cod_producto'],(cod,))
        reporte=self.cursor.fetchone()
        return reporte
    def buscar_codproducto2(self,cod):
        self.cursor.execute(queries['cod_producto2'],(cod,))
        reporte=self.cursor.fetchone()
        return reporte
    def ver_stock(self,stock):
        self.cursor.execute(queries['ver_stock'],(stock,))
        reporte=self.cursor.fetchone()
        return reporte
    #updates del producto
    def cambiar_nom_prod(self,nombre,id):
        val=(nombre,id)
        self.cursor.execute(queries['update_nombre_prod'],val,)
        self.conexion.commit()
    def cambiar_precio(self,precio,id):
        val=(precio,id)
        self.cursor.execute(queries['update_precio'],val,)
        self.conexion.commit()
    def cambiar_detalles(self,detalles,id):
        val=(detalles,id)
        self.cursor.execute(queries['update_detalles'],val,)
        self.conexion.commit()
    #función para cambiar el stock cuando alguien compra el preoducto, le resta 1 (se hace automatico)
    def cambiar_stock(self,stocke,dato):
        stockes=stocke-1
        val=(stockes,int(dato))
        self.cursor.execute(queries['cambiar_stock'],val)
        self.conexion.commit()
    #función para updatear el stock cuando el vendedor ya vendió todo su stock y quiere reponerlo(lo hace el vendedor)
    def cambiar_stock2(self,stock,codigo):
        val=(stock, codigo)
        self.cursor.execute(queries['cambiar_stock'],val)
        self.conexion.commit()
    #función para cambiar el stock pero con el id del vendedor
    def cambiar_stock3(self,stock,id):
        val=(stock, id)
        self.cursor.execute(queries['cambiar_stock3'],val)
        self.conexion.commit()

    def borrar_producto(self,codigo):
        self.cursor.execute(queries['delete_producto'],(codigo,))
        self.conexion.commit()

    #borro el producto si el usuario elimina su cuenta
    def borrar_productoo(self,id):
        self.cursor.execute(queries['delete_prod'],(id,))
        self.conexion.commit()

    def todos_productos2(self,id):
        self.cursor.execute(queries['todos_productos2'],(id,))
        reporte=self.cursor.fetchall()
        return reporte
    #VENDER
    def vender (self,Productos):
        val=(Productos.get_prod_codigo(),Productos.get_nombre_producto(),Productos.get_precio(),Productos.get_codigo_categoria(),Productos.get_codigo_marca(),Productos.get_detalles(),Productos.get_stock(),Productos.get_id_cliente())
        self.cursor.execute(queries['add_producto'],val,)
        self.conexion.commit()
    #productos---categorias
    #crear categoria
    def crear_categoria(self,Categoria):
        if self.traer_categoria(Categoria)==[]:
            val=(Categoria.get_codigo_categoria(),Categoria.get_nombre_categoria(),Categoria.get_descripcion())
            self.cursor.execute(queries['add_categoria'],val,)
            self.conexion.commit()
            Categoria.set_codigo_categoria(self.cursor.lastrowid)
            print("Ok!")
            db.tiempito()
            return True
        else:
            print("la categoria que quieres agregar ya existe")
            db.tiempo()
            return False
    #trae el codigo de la categoria con un get nombre 
    def traer_categoria(self,Categoria):
        self.cursor.execute(queries['get_categoria'],(Categoria.get_nombre_categoria(),))
        reporte=self.cursor.fetchall()
        return reporte
    #trae todas las categorias
    def todas_categorias(self):
        self.cursor.execute(queries['todas_categorias'])
        reporte=self.cursor.fetchall()
        return reporte
    #trae el nombre de la categoria con el codigo que se ingresa
    def nom_categoria(self,codigo):
        self.cursor.execute(queries['nom_categoria'],(codigo,))
        reporte=self.cursor.fetchall()
        return reporte
    #trae el nombre de la categoria con un objeto categoria como parametr, hace un get codigo
    def nom_categoria2(self,cat):
        self.cursor.execute(queries['nom_categoria'],(cat.get_codigo_categoria(),))
        reporte=self.cursor.fetchall()
        return reporte
    #trae el codigo de categoria con el nombre
    def cod_categoria(self,nombre):
        self.cursor.execute(queries['cod_categoria'],(nombre,))
        reporte=self.cursor.fetchall()
        return reporte
    #MARCAS
    def traer_marca(self,nombre):
        self.cursor.execute(queries['traer_marca'],(nombre,))
        reporte=self.cursor.fetchone()
        return reporte
    #trae el codigo de la marca con un get nombre
    def traer_marca2(self,Marca):
        self.cursor.execute(queries['traer_marca'],(Marca.get_nombre_marca(),))
        reporte=self.cursor.fetchall()
        return reporte
    def traer_marca3(self,mar):
        self.cursor.execute(queries['traer_marca2'],(mar.get_codigo_marca(),))
        reporte=self.cursor.fetchall()
        return reporte
    def todas_marcas(self):
        self.cursor.execute(queries['todas_marcas'])
        reporte=self.cursor.fetchall()
        return reporte
    def cod_marca(self,codigo):
        self.cursor.execute(queries['traer_cod_marca'],(codigo,))
        reporte=self.cursor.fetchone()
        return reporte

    def crear_marca(self,Marca):
        if self.traer_marca2(Marca)==[]:
            val=(Marca.get_nombre_marca(),Marca.get_codigo_marca(),)
            self.cursor.execute(queries['add_marca'],val,)
            self.conexion.commit()
            Marca.set_codigo_marca(self.cursor.lastrowid)
            print("Ok!")
            db.tiempito()
            return True
        else:
            print("la marca que quieres agregar ya existe")
            db.tiempo()
            return False
    def buscar_codmarca(self,nombre):
        self.cursor.execute(queries['codigo_marca'],(nombre,))
        reporte=self.cursor.fetchone()
        return reporte
    #METODOS
    def crear_metodo(self,Metodo):
        val=(Metodo.get_numero(),Metodo.get_detalles())
        self.cursor.execute(queries['crear_metodo'],val,)
        self.conexion.commit()

    def traer_metodo(self,Metodo):
        self.cursor.execute(queries['traer_metodo'],(Metodo.get_numero(),))
        reporte=self.cursor.fetchall()
        return reporte 

    def traer_metodo2(self):
        self.cursor.execute(queries['traer_metodo2'])
        reporte=self.cursor.fetchone()
        return reporte
    #ALERTAS
    #función para borrar la alerta de la base de datos luego de que el vendedor updeateó el producto
    def borrar_alerta(self,codigo):
        self.cursor.execute(queries['borrar_alerta'],(codigo,))
        self.conexion.commit()

    def crear_alerta(self,Alerta):
        val=(Alerta.get_codigo_alerta(),Alerta.get_fecha(),Alerta.get_codigo_prod(),Alerta.get_cliente_id())
        self.cursor.execute(queries['alertando'],val,)
        self.conexion.commit()
    
    def alerta(self,id):
        self.cursor.execute(queries['alerta'],(id,))
        reporte=self.cursor.fetchall()
        return reporte

    def alertando(self,codigo,id):
        now = datetime.now()
        new_date = now + timedelta(days=2)
        alertaa=Alerta(0,new_date,codigo,id)
        return db.crear_alerta(alertaa)
    
    def traer_alerta(self,id):
        self.cursor.execute(queries['traer_alerta'],(id,))
        reporte=self.cursor.fetchone()
        return reporte
    
    def traer_fecha(self,codigo):
        self.cursor.execute(queries['traer_fecha'],(codigo,))
        reporte=self.cursor.fetchone()
        if reporte!=None:
            time =reporte[0]
            return time

    def codigo(self,id):
        self.cursor.execute(queries['codigo'],(id,))
        reporte=self.cursor.fetchone()
        if reporte!=None:
            return reporte
    #COMPRAR
    def comprar(self,Comprar):
        val=(Comprar.get_cliente_id(),Comprar.get_codigo_producto(),Comprar.get_metodo_pago(),Comprar.get_detalles(),Comprar.get_fecha(),)
        self.cursor.execute(queries['comprar'],val,)
        self.conexion.commit()
    def todas_compras(self,id):
        self.cursor.execute(queries['todas_compras'],(id,))
        reporte=self.cursor.fetchall()
        return reporte
    def ver_compras(self,id):
        self.cursor.execute(queries['compras'],(id,))
        reporte=self.cursor.fetchall()
        return reporte

    #borrar compra
    def borrar_compra(self,id):
        self.cursor.execute(queries['borrar_comprar'],(id,))
        self.conexion.commit()
    #traigo compra
    def traer_compra(self,id):
        self.cursor.execute(queries['get_comprar'],(id,))
        reporte=self.cursor.fetchall()
        return reporte

    #EXTRAS
    #función limpiar pantalla
    def limpiar_pantalla(self):
        limpiar=os.system('cls')
        return limpiar
    #funcion tiempo 4seg
    def tiempo(self):
        return time.sleep(4)
    #funcion tiempo 2 seg
    def tiempito(self):
        return time.sleep(2)
    #función para generar un código random para poder pagar el producto por rapipago, pagofacil
    def random(self):
        a=random.choice("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
        b=random.choice("abcdefghijklmnñopqrstuvwxyz")
        c=random.choice("1234567890")
        d=random.choice("!#$*")
        e=random.choice("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
        f=random.choice("1234567890")
        ultima=(a+b+c+d+e+f)
        return ultima





    
db=Database()
