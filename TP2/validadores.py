from validate_email import validate_email
from dba import Database

db=Database()

class Validador():
    def __init__(self):
        pass    
    def validar_registracion(self,datos):
        datosFinales = {}
        errores = {}
        
        for x,y in datos.items():
            datosFinales[x]=y.strip()
        
        if datosFinales["nombre"]=="":
            errores["nombre"]="Hubo error en el nombre porque esta vacio"
        
        if len(datosFinales["contraseña"])< 6:
            errores["contraseña"]='la pass debe tener mas de 6 caracteres'
        elif datosFinales["contraseña"]=="":
            errores["contraseña"]='Hubo error en la contraseña porque esta vacia'
        elif not any(char.isupper() for char in datosFinales["contraseña"]):
            errores["contraseña"]='Password debe tener una palabra mayuscula'
        elif not any(char.islower() for char in datosFinales["contraseña"]):
            errores["contraseña"]='Password debe tener minusculas'
        
         
        if datosFinales["cpassword"]=="":
            errores["cpassword"] = "Hubo error en la confirmacion de contraseña porque esta vacia"
        elif datosFinales["cpassword"] != datosFinales["contraseña"]:
            errores["cpassword"] = "La contraseña no verifica"
        
        if datosFinales["email"]=="":
            errores["email"] = "Hubo error en el email porque esta vacio"
        elif validate_email(datosFinales["email"])==False:
            errores["email"] = "El email no es un email"
        elif db.buscar_cliente(datosFinales["email"]) != None:
            errores["email"] = "El email ya esta en uso"
        
        return errores
    #validador de login
    def validar_login(self,email,contraseña):
        errores={}
        #busco al usuario en la bdd a ver si está registrado
        user= db.buscar_usuario(email)
        #si está registrado busca la contraseña y la desencripta
        if user!=None:
            contraa=db.buscar_contraseña(email)
            contra=db.clave_desencriptada(contraa)
            contraseña=contraseña.encode()
        if user==None:
            errores["user"]="ese mail no está registrado en la base de datos"
        if email is None:
            errores["email"] = "Hubo error en el email porque esta vacio"
        elif validate_email(email)==False:
            errores["email"] = "El email no es un email"
        
        if contraseña is None:
            errores["contraseña"]="Dejaste la password vacia"
        if user != None and contraseña != None:
            if contra != contraseña:
                errores["contraseña"]="Las Password no coincide"
            else:
                print('Ok!')
                
        return errores
    def validar_compra(self,datos):
        datosFinales = {}
        errores={}
        for x,y in datos.items():
            if y==str:
                datosFinales[x]=y.strip()
            elif y!=str:
                datosFinales[x]=y

        codigo=datosFinales['codigo_producto']
        if db.buscar_codproducto(codigo)==None:
            errores['codigo_producto']="el codigo del producto que ingresaste es incorrecto."
        if "metodo_pago"== "":
            errores["metodo_pago"]="Ingrese un método de pago"
        elif db.buscar_codproducto(codigo)!=None:
            stock=db.ver_stock(codigo)
            stock=[stock]
            stocke=(stock[0][0])
            if stocke==0:
                errores['stock']="No hay stock, disculpe las molestias, avisaremos al vendedor que reponga este producto"
            if stocke!=0:
                db.cambiar_stock(stocke,codigo)
        
                
        return errores
    def validar_contraseña(self,pal2,ecommerce1):
        errores={}
        id=ecommerce1.get_id_cliente()
        contraseña=ecommerce1.get_contraseña()
        if pal2!=None or pal2!="":
            if db.traer_contra(id)==None:
                if contraseña!=pal2:
                    errores["contraseña"]="Las Password no coinciden"
            elif db.traer_contra(id)!=None:
                contraa=db.traer_contra(id)
                contraa=[contraa]
                contra=(contraa[0][0])
        #paso la contraseña a bytes, porque me la trae como string de la bdd
                contra=contra.encode()
                if contra != pal2:
                    errores["contraseña"]="Las Password no coinciden"
                else:
                    print('Ok!')
        if pal2 is None:
            errores["contraseña"]="Dejaste la password vacia"
        
        return errores
    def validar_email(self,email):
        errores={}
        if email is None:
            errores["email"] = "Hubo error en el email porque esta vacio"
        elif validate_email(email)==False:
            errores["email"] = "El email no es un email"
        elif db.buscar_cliente(email):
            errores["email"] = "El email ya está en uso"

        return errores
    def validar_categoria(self,datos):
        datosFinales = {}
        errores = {}
        cat=db.cod_categoria("nombre_categoria")
        for x,y in datos.items():
            if y==str:
                datosFinales[x]=y.strip()
            elif y!=str:
                datosFinales[x]=y
        
        if datosFinales["nombre_categoria"]=="":
            errores["nombre_categoria"]="Hubo error en el nombre de la categoria porque esta vacio"
        if cat!=[]:
            errores["nombre categoria"]="La categoria ya está ingresada en la bdd"
        if datosFinales["descripcion"]=="":
            errores["nombre_categoria"]="Hubo error en la descripción porque está vacia "
        
        return errores
        


    def validar_mail(self,email):
        errores={}
        user= db.buscar_usuario(email)
        if user==None:
            errores["user"]="ese mail no está registrado en la base de datos"
        if email is None:
            errores["email"] = "Hubo error en el email porque esta vacio"
        elif validate_email(email)==False:
            errores["email"] = "El email no es un email"
        return errores
    def validar_marca(self,datos):
        datosFinales = {}
        errores = {}
        for x,y in datos.items():
            if y==str:
                datosFinales[x]=y.strip()
            elif y!=str:
                datosFinales[x]=y
        #corrobora que el nombre de la marca no esté vacio
        if datosFinales["nombre_marca"] is None:
            errores["nombre_marca"]="Hubo error en el nombre porque está vacio"
        #corrobora que el nombre de la marca sea string
        if datosFinales["nombre_marca"].isdigit()==True:
            errores["nombre_marca"]="Hubo error en el nombre, no puede ser un número su marca, debe ser un string "
        return errores
    def validar_venta(self,datos,cat):
        datosFinales = {}
        errores = {}
        for x,y in datos.items():
            if y==str:
                datosFinales[x]=y.strip()
            elif y!=str:
                datosFinales[x]=y
        #errores de datos vacios
        if datosFinales["nombre_producto"]=="":
            errores["nombre_producto"]="Hubo error en el nombre del producto porque está vacio"
        if datosFinales["precio"]=="":
            errores["precio"]="Hubo error en precio porque está vacio"
        if datosFinales["detalles"]=="":
            errores["detalles"]="Hubo error en los detalles porque está vacio"
        if datosFinales["stock"]=="":
            errores["stock"]="Hubo error en el stock porque está vacio"
        #errores de mal tipeo y diferenciación entre string y enteros
        if datosFinales["nombre_producto"].isdigit()==True:
            errores["nombre_producto"]="Hubo error en el nombre dedl producto, no puede ser un número, debe ser un string "
        if datosFinales["precio"].isdigit()==False:
            errores["precio"]="Hubo error en el precio, debe ingresarlo con números"
        if datosFinales["stock"].isdigit()==False:
            errores["stock"]="Hubo error en el stock, no puede ser un string, debe ser un número entero. "
        return errores
    #validadores de actualización de datos del producto
    def validar_stock(self,stock):
        errores={}
        if stock=="":
            errores["stock"]="Hubo error en el stock porque está vacio"
        if stock.isdigit()==False:
            errores["stock"]="Hubo error en el stock, no puede ser un string, debe ser un número entero. "
        return errores 
    def validar_precio(self,precio):
        errores={}
        if precio.isdigit()==False:
            errores["precio"]="Hubo error en el precio, no puede ser un string, debe ser un número entero. "
        if precio=="":
            errores["precio"]="Hubo error en el precio porque está vacio"
        return errores 
    #validadores de actualización de datos del usuario
    def validar_usuario(self,usuario):
        errores={}
        if usuario.isdigit()==True:
            errores["usuario"]="Hubo error en el nombre de usuario, no puede ser un numero, debe ser un string. "
        if usuario=="":
            errores["usuario"]="Hubo error en el usuario porque está vacio"
        return errores
    def validar_nombre(self,nombre):
        errores={}
        if nombre.isdigit()==True:
            errores["nombre"]="Hubo error en el nombre, no puede ser un numero, debe ser un string. "
        if nombre=="":
            errores["nombre"]="Hubo error en el nombre porque está vacio"
        return errores
    def validar_apellido(self,apellido):
        errores={}
        if apellido.isdigit()==True:
            errores["apellido"]="Hubo error en el apellido, no puede ser un numero, debe ser un string. "
        if apellido=="":
            errores["apellido"]="Hubo error en el apellido porque está vacio"
        return errores
validador=Validador()
