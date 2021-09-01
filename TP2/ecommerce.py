import getpass
from init import *
from cliente import Cliente
import base64
from comprar import Comprar
from productos import Productos
from marca import Marca
from datetime import datetime, date, timedelta
from categoria import Categoria

def login():
    xd=True
    while xd==True:
        db.limpiar_pantalla()
        print("------PRESIONE X PARA CANCELAR-------")
        print("Si olvidó su contraseña presione 1, sino presione 2")
        rsp=input("---> ")
        db.limpiar_pantalla()
        if rsp=="1":
            recuperar=recuperar_contraseña()
            xd=False
        elif rsp=="2":
            xd=False
        elif rsp=="x" or rsp=="X":
            return None 
        else:
            print("Ingrese una opción correcta")
            db.tiempo()
            
    i=False
    while not i==True:
        db.limpiar_pantalla()
        print("----PRESIONE X PARA CANCELAR----")
        print("LOGIN")
        mail= input("Ingrese su mail: \n")
        if mail=="x" or mail=="X":
            i=True
            return None
        print("----PRESIONE X PARA CANCELAR----")
        password=getpass.getpass('Password:\n')
        if password=="x" or password=="X":
            i=True
            return None
        errores=validador.validar_login(mail,password)
        if not errores:
            print("Se logeo de manera correcta")
            db.tiempito()
            db.limpiar_pantalla()
            i=True
            return db.buscar_usuario(mail)
        else:
            for x in errores.values():
                print(x)
            db.tiempo()
#registro al cliente
def registracion_cliente():
    db.limpiar_pantalla()
    i=False
    while not i==True:
        db.limpiar_pantalla()
        print("----PRESIONE X PARA CANCELAR----")
        datos={}
        usuariooo=input("Escriba su usuario:")
        if usuariooo=="x" or usuariooo=="X":
            i=True
            return None
        datos["usuario"]=usuariooo
        datos["nombre"]=input("Escriba su nombre:")
        if datos["nombre"]=="x" or datos["nombre"]=="X":
            i=True
            return None 
        datos["apellido"]=input("Escriba su apellido:")
        if datos["apellido"]=="x" or datos["apellido"]=="X":
            i=True
            return None 
        datos["contraseña"]=getpass.getpass('Password:')
        if datos["contraseña"]=="x" or datos["contraseña"]=="X":
            i=True
            return None 
        datos["cpassword"]=getpass.getpass('Confirmacion de Password:')
        if datos["cpassword"]=="x" or datos["cpassword"]=="X":
            i=True
            return None
        datos["email"]=input("Escriba su email:")
        if datos["email"]=="x" or datos["email"]=="X":
            i=True
            return None
        errores=validador.validar_registracion(datos)
        if not errores:
            datos["ids"]=0
            del datos["cpassword"]
            user=db.crear_cliente(Cliente(**datos))
            del datos["ids"]
            #guardo los datos en la variable user2 para poder realizar acciones con el usuario recién creado
            datos["ids"]=db.traer_id2(datos["email"])[0][0]
            user2=Cliente(**datos)
            print("Su usuario fue creado con éxito!")
            db.tiempo()
            db.limpiar_pantalla()
            i=True
            return user2
                
        else:
            for x in errores.values():
                print(x)
                db.tiempito()
            db.tiempo()
def Menu():
    db.limpiar_pantalla()
    print("*******************************************************************************************")
    print("*Bienvenida/o, en PULPA vas a poder comprar y vender una variedad de productos increibles!*")
    print("*******************************************************************************************")
    db.tiempito()
    u=True
    while u==True:
        #login
        print("Si ya tenés una cuenta marca 1, sino registrate gratis con la opcion 2!")
        opcion=input("--->")
        db.limpiar_pantalla()
        if opcion=="1":
            u=False
            ecommerce1=login()
            if ecommerce1!=None:
                id=ecommerce1.get_id_cliente()
                if db.alerta(id)!=[]:
                    alerta=alerta_stock(ecommerce1)
        #registro cliente
        elif opcion=="2":
            ecommerce1=registracion_cliente()
            u=False
        elif opcion!='1' and opcion!='2':
            u=True
            print("Por favor ingrese una opción correcta.")
            db.tiempo()
            db.limpiar_pantalla()

    if ecommerce1!=None:       
        ñ=True
        while ñ==True:
            db.limpiar_pantalla()
            id=ecommerce1.get_id_cliente()
            print("¿Qué desea realizar?")
            print("[0]Opciones de mi perfil")
            print("[1]Comprar un producto")
            print("[2]Vender un producto")
            print("[x]Cerrar sesión")
            opcion2=input("---> ")
            if opcion2=="0":
                ñ=opciones(ecommerce1)
            elif opcion2=="1":
                comprandoo=comprando(id)
            elif opcion2=="2":
                vendiendoo=vendiendo(id)
            elif opcion2=="x":
                print("¡Hasta la próxima!")
                db.tiempo()
                db.limpiar_pantalla()
                ñ=False
            else:
                print("Por favor ingrese una opción correcta")
                db.tiempo()
                db.limpiar_pantalla()

        
#función para vender un producto    
def comprando(id):
    datos={}
    i=False
    while not i==True:
        datos["cliente_id"]=id
        db.limpiar_pantalla()
        print("Estos son los productos que están disponibles")
        for x in db.todos_productos():
            for y in x:
                print(y,end="")
            print("\n")
        if db.todos_productos()==[]:
            print("Disculpe, no hay productos disponibles")
        print("-----PRESIONE X PARA VOLVER ATRÁS------")
        datos["codigo_producto"]=input("Escriba el codigo del producto que desea comprar:")
        if datos["codigo_producto"]=="x" or datos["codigo_producto"]=="X":
            i=True
        else:
            sss=True
            while sss==True:
                datos["metodo_pago"]=input("Escriba el metodo de pago que desea utilizar [1] Efectivo [2]Tarjeta\n")
                if datos["metodo_pago"]=="1":
                    datos["detalles"]=db.random()
                    sss=False
                elif datos["metodo_pago"]=="2":
                    for mdo in db.traer_metodo2():
                        print(mdo, end="")
                    print("\n")
                    datos["detalles"]=input("Ingrese los datos pedidos: ")
                    sss=False
                else:
                    print("Por favor ingrese una opción correcta")
                    db.tiempo()
                    db.limpiar_pantalla()
            datos["fecha"]=datetime.now()
            errores=validador.validar_compra(datos)
            if not errores:
                compra=db.comprar(Comprar(**datos))
                i==True
                print("Su compra se realizó con éxito!")
                if datos["metodo_pago"]=="1":
                    print("Su código para pagar su producto por rapipago/pago facil es:")
                    print(datos["detalles"])
                    print("Igualmente, puede consultarlo desde el menú.")
                    db.tiempo()
                    db.tiempo()
                    db.tiempo()
                    db.tiempo()
                    i=True
                    return compra
                return compra
            else:
                for wer in errores.values():
                    print(wer)
                db.tiempo()
#función para vender un producto
def vendiendo(id):
    pf=True
    fll=False
    while pf==True:
        db.limpiar_pantalla()
        print("RECUERDE QUE SOLO PUEDE TENER UN PRODUCTO A LA VENTA A LA VEZ")  
        print("Si desea vender un producto presione 0")
        print("Si desea volver atrás presione x")
        espu=input("---> ")
        if espu=="0":
            if db.todos_productos2(id)!=[]:
                db.limpiar_pantalla()
                print("**************************************************")
                print("***LO SENTIMOS, YA TIENE UN PRODUCTO A LA VENTA***")
                print("**************************************************")
                db.tiempito()
                print("si quiere, puede borrar su producto desde")
                print("opciones de mi perfil-->ver/editar mi producto en venta")
                input()
                pf=False
            else:
                evb=True
                while evb==True:
                    db.limpiar_pantalla()
                    datos={}
                    datos["codigos"]=0
                    print("----PRESIONE X PARA CANCELAR LA VENTA------")
                    rta=input("Ingrese el nombre de su producto: ")
                    if rta=="x" or rta=="X":
                        evb=False
                    else:
                        datos["nombre_producto"]=rta
                        db.limpiar_pantalla()
                        print("----PRESIONE X PARA CANCELAR LA VENTA------")
                        precio=input("Escriba el precio de su producto: ")
                        if precio=="x" or precio=="X":
                            evb=False
                        else:
                            datos["precio"]=precio
                            db.limpiar_pantalla() 
                            print("Estas son las categorias disponibles: ")
                            for x in db.todas_categorias():
                                    for y in x:
                                        print(y,end="")
                                    print("\n")
                            org=True
                            while org==True:
                                print("----PRESIONE X PARA CANCELAR LA COMPRA------")
                                print("A continuación, presione 0 para ingresar la categoria de su producto")
                                print("O si desea agregar una categoria nueva presione 1")
                                respu=input("> ")
                                db.limpiar_pantalla()
                                if respu=="0":
                                    for xd in db.todas_categorias():
                                            for t in xd:
                                                print(t,end="")
                                            print("\n")
                                    print("----PRESIONE X PARA CANCELAR------")
                                    hola=input("Ingrese el codigo de la categoria de su producto:")
                                    if hola=="x" or hola=="X":
                                        org=False
                                        evb=False
                                    else:
                                        cat=Categoria(hola,"","")
                                        if db.nom_categoria2(cat)==[]:
                                            print("La categoria ingresada no existe.")
                                            db.tiempo()
                                        else:
                                            codi=cat.get_codigo_categoria()
                                            datos["codigo_categoria"]=codi
                                            fll=True
                                            evb=False
                                            org=False
                                elif respu=="1":
                                    we=True

                                    while we==True:
                                        #AGREGAR UNA NUEVA CATEGORIA
                                        db.limpiar_pantalla()
                                        print("¿Está seguro que desea agregar una nueva categoria?")
                                        print("[1]SI")
                                        print("[X]Volver atrás")
                                        aaa=input("--> ")
                                        if aaa=="1":
                                            #EL USUARIO INGRESA DATOS Y SE VALIDA PARA CREAR LA CATEGORIA
                                            db.limpiar_pantalla()
                                            categoria={}
                                            categoria["codigos2"]=0
                                            print("----PRESIONE X PARA VOLVER ATRÁS------")
                                            cate=input("Ingrese el nombre de su categoria: ")
                                            if cate=="x" or cate =="X":
                                                we=False
                                                evb=False
                                            else:
                                                categoria["nombre_categoria"]=cate
                                                db.limpiar_pantalla()
                                                print("----PRESIONE X PARA VOLVER ATRÁS------")
                                                categoria["descripcion"]=input("Ingrese la descripción de su categoria: ")
                                                errores=validador.validar_categoria(categoria)
                                                if not errores:
                                                    cat=Categoria(**categoria)
                                                    if db.crear_categoria(cat)==True:
                                                        print("Su categoria fue creada con éxito!")
                                                        we=False
                                                    elif db.crear_categoria(cat)==False:
                                                        we=True
                                                    for arr in db.todas_categorias():
                                                        for ar in arr:
                                                            print(ar,end="")
                                                        print("\n")
                                                    print("----PRESIONE X PARA CANCELAR LA COMPRA------")
                                                    datos["codigo_categoria"]=input("Ingrese el código de su categoria: ")
                                                    fll=True
                                                    evb=False
                                                    db.limpiar_pantalla()
                                                    we=False
                                                    org=False
                                                else:
                                                    for lñ in errores.values():
                                                        print(lñ)
                                                    db.tiempo()
                                        elif aaa=="x":
                                            db.limpiar_pantalla()
                                            we=False
                                        else:
                                            print("Por favor ingrese una opción correcta.")
                                            db.tiempo
                                            db.limpiar_pantalla()
                                elif respu=="x" or respu=="X":
                                    evb=False
                                else:
                                    print("Por favor ingrese una opción correcta.")
                                    db.tiempo()
                                    db.limpiar_pantalla()
                if fll==True:
                    print("Ingrese el nombre de la marca que pertenece a su producto: ")
                    print("Estas son las marcas disponibles: ")
                    db.tiempo()
                    xs=True
                    while xs==True:
                        db.limpiar_pantalla()
                        for kk in db.todas_marcas():
                                for qq in kk:
                                    print(qq,end="")
                                print("\n")
                        print("---PRESIONE X PARA CANCELAR----")
                        print("A continuación, presione 0 para ingresar la marca de su producto")
                        print("O si desea agregar una marca nueva presione 1")
                        respuesta=input("> ")
                        #funcion para agregar una marca nueva
                        if respuesta=="1":
                            marca={}
                            marca["nombre_marca"]=input("Ingrese el nombre de la marca: ")
                            marca["codigos"]=0
                            errores=validador.validar_marca(marca)
                            if not errores:
                                mar=(Marca(**marca))
                                if db.crear_marca(mar)==True:
                                    print("Su marca fue creada con éxito!")
                                elif db.crear_marca(mar)==False:
                                    xs=False
                                print("su marca fue creada con exito, ahora puede agregarsela a su producto")
                            else:
                                for fz in errores.values():
                                    print(fz)

                        elif respuesta=="0":
                            xs=False
                        elif respuesta=="x" or respuesta=="X":
                            xs=False
                            evb=False
                            pf=False
                        else:
                            print("Por favor ingrese una opción correcta")
                            db.tiempo()
                    juu=True
                    while juu==True:
                        print("\nA continuacion escriba el código de la marca para poder poner en venta su producto")
                        db.limpiar_pantalla()
                        for og in db.todas_marcas():
                                    for dz in og:
                                        print(dz,end="")
                                    print("\n")
                        holi=input("Ingrese el codigo de la marca de su producto:")
                        mar=Marca("",holi)
                        if db.traer_marca3(mar)==[]:
                            print("La marca ingresada no existe.")
                            db.tiempo()
                        else:
                            codig=mar.get_codigo_marca()
                            datos["codigo_marca"]=codig
                            juu=False
                    datos["detalles"]=input("Detalles de su producto:")
                    datos["stock"]=input("Stock de su producto: ")
                    datos["id_cliente"]=id
                    errores=validador.validar_venta(datos,cat)
                    if not errores:
                        db.vender(Productos(**datos))
                        print("Su producto ya está a la venta!")
                        db.tiempo()
                        pf=False
                    else:
                        for oh in errores.values():
                            print(oh)
                        db.tiempo()
        elif espu=="x":
            db.limpiar_pantalla()
            pf=False
        else:
            print("Por favor ingrese una opción correcta.")
            db.tiempito()
            db.limpiar_pantalla()
def alerta_stock(ecommerce1):
    id=ecommerce1.get_id_cliente()
    codigoo=db.codigo(id)
    codigoo=[codigoo]
    codigo=(codigoo[0][0])
    ahora = datetime.now()
    #verifica si el cliente tiene su producto a la venta que ya no tenga stock, e imprime 
    alertaa=db.alerta(id)
    #busca la fecha en la que fue creada la alerta
    fecha=db.traer_fecha(codigo)
    #si la fecha que trae es distinta a none significa que ya tiene la alerta creada en la base de datos
    if fecha!=None:
        #comprueba que la fecha actual sea MAYOR O IGUAL a la ingresada en la alerta de la base
        #si lo es borra el producto
        if ahora>=fecha:
            db.limpiar_pantalla()
            db.borrar_producto(codigo)
            print("SU PRODUCTO FUE BORRADO DEL SISTEMA POR FALTA DE STOCK")
            print("recuerde que puede agregar un producto desde el menú")
            input()
        #si la fecha de alerta de la bdd es menor que la fecha actual, muestra cuantos dias le queda para updatearlo
        #le da la opción de updatearlo ahora
        if ahora<fecha:
            dr=True
            while dr==True:
                restante=fecha-ahora
                db.limpiar_pantalla()
                print("LE QUEDAN : ",restante)
                print("para updatear el stock de su producto")
                print("¿Desea hacerlo ahora? oprima 1")
                print("Sino, presione 2")
                respuesta=input()
                if respuesta=="1":
                    db.limpiar_pantalla()
                    fo=True
                    while fo==True:
                        print("-----PRESIONE X PARA CANCELAR-----")
                        stock=input("Ingrese el nuevo stock de su producto: ")
                        if stock=="x" or stock=="X":
                            fo=False
                        else:
                            errores=validador.validar_stock(stock)
                            if not errores:
                                db.cambiar_stock2(stock,codigo)
                                print("Su stock fue modificado con éxtio!")
                                dr=False
                            else:
                                for x in errores.values():
                                    print(x)
                                db.tiempo()

                elif respuesta=="2":
                    dr=False
                else:
                    print("Por favor ingrese una opción correcta")
                    db.tiempo()


        #si la función db.alerta devuelve algo distinto a none significa que tiene su producto sin stock
        #entonces entra en el if
    if alertaa != None and fecha==None:
        for x in alertaa:
            for y in x:
                print(y)
        #cartel de alerta cuando el stock de su producto es 0
        print("¿Desea agregar stock a su producto?")
        print("**************************************************************************")
        print("  ▓ALERTA ▓ si no agrega stock ahora, su producto será borrado del sistema,")
        print("en dos días a partir de hoy: ",ahora)
        respuesta=input("Ingrese 1 para cambiar el stock, si no quiere hacerlo ahora, ingrese 2: ")
        if respuesta=="1":
            stock=input("Ingrese el nuevo stock de su producto: ")
            db.cambiar_stock2(stock,codigo)
        elif respuesta=="2":
            db.alertando(codigo,id)
#opciones del cliente
def opciones(ecommerce1):
    print(ecommerce1)
    id=ecommerce1.get_id_cliente()
    db.limpiar_pantalla()
    usuario=db.traer_usuario(id)
    for ml in usuario:
            print("Hola ",ml)
    print("Espero que te encuentres bien")
    db.tiempo()
    c=True
    while c==True:
        db.limpiar_pantalla()
        print("-----------------------------------------------------------------")
        print("¿Qué opcion desea realizar? ")
        print("[0]Cambios en los datos de mi perfil (eliminar/actualizarlos).")
        print("[1]Ver mis productos comprados.")
        print("[2]Ver/editar/borrar mi producto en venta.")
        print("[3]Ver información del usuario")
        print("[x]Volver al menú principal")
        respuestaa=input("---> ")
        if respuestaa=="0":
            qw=True
            while qw==True:
                db.limpiar_pantalla()
                print("¿Qué desea realizar?")
                print("[0]Actualizar datos.")
                print("[1]Borrar datos.")
                print("[x]Volver atrás")
                respuesta=input("---> ")
                if respuesta=="0":
                    hk=True
                    while hk==True:
                        db.limpiar_pantalla()
                        print("¿Qué desea actualizar?")
                        print("[0]Nombre de usuario")
                        print("[1]Su nombre")
                        print("[2]Su apellido")
                        print("[3]Su contraseña")
                        print("[4]Su email")
                        print("[x]Volver atrás")
                        opcion=input("---> ")
                        if opcion=="0":
                            db.limpiar_pantalla()
                            print("------PRESIONE x PARA CANCELAR------")
                            print("Ingrese su nuevo nombre de usuario: ")
                            usuario=input("---> ")
                            db.limpiar_pantalla()
                            if usuario=="x" or usuario=="X":
                                hk=True
                            else:
                                errores=validador.validar_usuario(usuario)
                                if not errores:
                                    db.cambiar_usuario(usuario,id)
                                    print("Su usuario fue modificado con éxito!")
                                    db.tiempo()
                                    db.limpiar_pantalla()
                                    hk=True
                                else:
                                    for xa in errores.values():
                                            print(xa)
                                    db.tiempo()

                        elif opcion=="1":
                            db.limpiar_pantalla()
                            print("------PRESIONE x PARA CANCELAR------")
                            print("Ingrese su nuevo nombre: ")
                            nombre=input("---> ")
                            db.limpiar_pantalla()
                            if nombre=="x" or nombre=="X":
                                hk=True
                            else:
                                errores=validador.validar_nombre(nombre)
                                if not errores:
                                    db.cambiar_nombre(nombre,id)
                                    print("Su nombre fue modificado con éxito!")
                                    hk=True
                                    db.tiempo()
                                    db.limpiar_pantalla()
                                else:
                                    for krr in errores.values():
                                            print(krr)
                                    db.tiempo()
                        elif opcion=="2":
                            db.limpiar_pantalla()
                            print("------PRESIONE x PARA CANCELAR------")
                            print("Ingrese su nuevo apellido: ")
                            apellido=input("---> ")
                            db.limpiar_pantalla()
                            if apellido=="x"or apellido=="X":
                                hk=True
                            else:
                                errores=validador.validar_apellido(apellido)
                                if not errores:
                                    db.cambiar_apellido(apellido,id)
                                    print("Su apellido fue modificado con éxito!")
                                    db.tiempo()
                                    db.limpiar_pantalla()
                                else:
                                    for gth in errores.values():
                                            print(gth)
                                    db.tiempo()


                        elif opcion=="3":
                            o=True
                            while o==True:
                                db.limpiar_pantalla()
                                print("------PRESIONE x PARA CANCELAR------")
                                print("Ingrese su contraseña anterior: ")
                                pal=getpass.getpass('Password:\n')
                                db.limpiar_pantalla()
                                if pal=="x" or pal=="X":
                                    o=False
                                else:
                                    pal2=base64.b64encode(bytes(pal, 'utf-8'))
                                    errores=validador.validar_contraseña(pal2,ecommerce1)
                                    if not errores:
                                        print("Ingrese su nueva contraseña:")
                                        password3=getpass.getpass('Password:\n')
                                        password4=base64.b64encode(bytes(password3, 'utf-8'))
                                        db.cambiar_contraseña(password4,id)
                                        print("Su contraseña fue modificada con éxito!")
                                        db.tiempo()
                                        o=False
                                    else:
                                        for h in errores.values():
                                            print(h)
                                        db.tiempo()
                                        db.limpiar_pantalla()
                        elif opcion=="4":
                            w=True
                            while w==True:
                                db.limpiar_pantalla()
                                print("------PRESIONE x PARA CANCELAR------")
                                print("Ingrese su nuevo mail: ")
                                mail=input("---> ")
                                if mail=="x" or mail=="X":
                                    w=False
                                else:
                                    errores=validador.validar_email(mail)
                                    if not errores:
                                        db.cambiar_email(mail,id)
                                        print("Su mail fue modificado con éxito!")
                                        db.tiempo()
                                        db.limpiar_pantalla()
                                        w=False
                                    else:
                                        for z in errores.values():
                                            print(z)
                                        db.tiempo()
                                        db.limpiar_pantalla()
                        elif opcion=="x":
                            hk=False
                            db.limpiar_pantalla()
                        else:
                            print("Por favor ingrese una opción correcta")
                            db.tiempito()
                            db.limpiar_pantalla()
                elif respuesta=="1":
                    ty=True
                    while ty==True:
                        db.limpiar_pantalla()
                        print("¿Qué desea realizar?")
                        print("[0]Borrar su usuario")
                        print("[x]Volver atrás")
                        answ=input("---> ")
                        if answ=="0":
                            er=True
                            while er==True:
                                db.limpiar_pantalla()
                                print("¿Está seguro que desea borrar su usuario?")
                                print("Todos sus datos se borrarán")
                                print("Si tiene productos a la venta desaparecerán del sistema")
                                print("Presione 1 para borrar su usuario, de lo contrario presione x para volver atrás")
                                answ2=input("---> ")
                                if answ2=="1":
                                    for jhjh in db.traer_compra(id):
                                        if db.traer_compra(id)!=None:
                                            for ghh in db.traer_compra(id):
                                                db.borrar_compra(id)
                                    if db.todos_productos2(id)!=[]:
                                        db.borrar_productoo(id)
                                    print("Ingrese su contraseña para borrar su cuenta")
                                    paw=input("Password: ")
                                    paw2=base64.b64encode(bytes(paw, 'utf-8'))
                                    errores=validador.validar_contraseña(paw2,ecommerce1)
                                    if not errores:
                                            db.borrar_usuario(id)
                                            print("Su usuario fue borrado")
                                            db.tiempo()
                                            db.limpiar_pantalla()
                                            er=False
                                            ty=False
                                            qw=False
                                            c=False
                                            ñ=False
                                            u=False
                                            return False           
                                    else:
                                        for xas in errores.values():
                                            print(xas)
                                        db.tiempo()
                                        db.limpiar_pantalla()

                                elif answ2=="x" or answ2=="X":
                                    er=False
                                else:
                                    print("Por favor ingrese una opción correcta")
                                    db.tiempo()   
                        elif answ=="x":
                            ty=False
                            db.limpiar_pantalla()     
                        else:
                            print("Por favor ingrese una opción correcta")
                            db.tiempo()

                elif respuesta=="x":
                    qw=False
                    db.limpiar_pantalla()
                else:
                    print("Por favor ingrese una opción correcta")
                    db.tiempito()
                    db.limpiar_pantalla()
        elif respuestaa=="1":
            db.limpiar_pantalla()
            if db.todas_compras(id)==[]:
                print("No compró ningún producto")
                db.tiempo()
                db.limpiar_pantalla()
            elif db.todas_compras(id)!=[]:
                db.limpiar_pantalla()
                print("------PRESIONE x PARA DEJAR DE VER SUS PRODUCTOS------")
                print("Estos son los productos que compró")
                print("\n")
                for oo in db.ver_compras(id):
                            for xq in oo:
                                print(xq,end="")
                            print("\n")
                for mq in db.todas_compras(id):
                    for mm in mq:
                        if db.buscar_codproducto2(mm)!=None:
                            print("DATOS DEL PRODUCTO")
                            for jup in db.buscar_codproducto2(mm):
                                print(jup)
                        else:
                            print("Disculpe, no se pueden obtener detalles del producto porque ya no está en la base de datos.")
                input("->")      
        elif respuestaa=="2":
            gh=True
            while gh==True:
                db.limpiar_pantalla()
                print("¿Qué desea realizar?")
                print("[0]Ver mi producto en venta.")
                print("[1]Editar mi producto en venta")
                print("[2]Borrar mi producto en venta")
                print("[x]Volver atrás")
                respu=input("---> ")
                if respu=="0":
                    if db.todos_productos2(id)==[]:
                        print("No tiene productos en venta")
                        db.tiempo()
                    elif db.todos_productos2(id)!=[]:
                        db.limpiar_pantalla()
                        print("------PRESIONE x PARA DEJAR DE VER SUS PRODUCTOS------")
                        print("Su producto en venta: ")
                        for yee in db.todos_productos2(id):
                            for yuu in yee:
                                print(yuu,end="")
                            print("\n")
                        input()
                elif respu=="1":
                    gt=True
                    while gt==True:
                        if db.todos_productos2(id)==[]:
                            print("No tiene producto en venta")
                            db.tiempo()
                            gt=False
                        elif db.todos_productos2(id)!=[]:
                            db.limpiar_pantalla()
                            print("¿Qué desea actualizar?")
                            print("[0]Precio de su producto")
                            print("[1]Detalles de su producto")
                            print("[2]Stock de su producto")
                            print("[x]Volver atrás")
                            apw=input("---> ")
                            if apw=="0":
                                db.limpiar_pantalla()
                                print("-------PRESIONE X PARA CANCELAR-------")
                                precio=input("Ingrese el nuevo precio de su producto---> ")
                                if precio=="x" or precio=="X":
                                    gt=True
                                else:
                                    errores=validador.validar_precio(precio)
                                    if not errores:
                                        db.cambiar_precio(precio,id)
                                        print("Su precio fue cambiado con éxito!")
                                        db.tiempo()
                                        gt=True
                                    else:
                                        for zaz in errores.values():
                                            print(zaz)
                                        db.tiempo()

                            elif apw=="1":
                                db.limpiar_pantalla()
                                print("-------PRESIONE X PARA CANCELAR-------")
                                detalless=input("Ingrese los nuevos detalles de su producto---> ")
                                if detalless=="x" or detalless=="X":
                                    gt=True
                                else:
                                    db.cambiar_detalles(detalless,id)
                                    print("Sus detalles fueron cambiados con éxito!")
                                    db.tiempo()
                            elif apw=="2":
                                db.limpiar_pantalla()
                                print("-------PRESIONE X PARA CANCELAR-------")
                                sth=input("Ingrese el nuevo stock de su producto---> ")
                                if sth=="x" or sth=="X":
                                    gt=True
                                else:
                                    errores=validador.validar_stock(sth)
                                    if not errores:
                                        db.cambiar_stock3(sth,id)
                                        print("Su stock fue cambiado con éxito!")
                                        input()
                                        gt=True
                                    else:
                                        for zoz in errores.values():
                                            print(zoz)
                                        db.tiempo()
                            elif apw=="x":
                                gt=False
                            else:
                                print("Por favor ingrese una opción correcta")
                                db.tiempo()
                                db.limpiar_pantalla()
                elif respu=="2":
                    up=True
                    while up==True:
                        db.limpiar_pantalla()
                        print("¿Seguro que desea borrar su producto?")
                        print("[1]Si")
                        print("[x]Volver atrás")
                        aver=input("---> ")
                        if aver=="1":
                            if db.todos_productos2(id)==[]:
                                print("No tiene productos en venta")
                                input()
                                up=False
                            elif db.todos_productos2(id)!=[]:
                                db.borrar_productoo(id)
                                print("Su producto fue borrado")
                                db.tiempo()
                                up=False
                        elif aver=="x":
                            up=False
                        else:
                            print("Ingrese una opción correcta")
                            db.tiempo()
                            db.limpiar_pantalla()
                elif respu=="x":
                    gh=False

                else:
                    print("Por favor ingrese una opción correcta")
                    db.tiempo()
                    db.limpiar_pantalla()
        elif respuestaa=="3":
            db.limpiar_pantalla()
            print("----PRESIONE X PARA VOLVER ATRÁS-----")
            for rpp in db.cliente_conid(id):
                    print(rpp,end="")
            print("\n")
            input()
            c=False
            return True               
        elif respuestaa=="x":
            c=False
            ñ=True
            return ñ
        
        else:
            print("Por favor ingrese una opción correcta")
            db.tiempito()
            db.limpiar_pantalla()
#función para recuperar la contraseña cuando el cliente inicia sesión        
def recuperar_contraseña():
    fr=True
    while fr==True:
        db.limpiar_pantalla()
        print("RECUPERAR CONTRASEÑA")
        print("[0]Recuperar su contraseña")
        print("[x]Volver atrás")
        rsp=input("---> ")
        if rsp=="0":
            jñ=True
            while jñ==True:
                db.limpiar_pantalla()
                print("Por favor ingrese su mail")
                eemail=input("---> ")
                errores=validador.validar_mail(eemail)
                if not errores:
                    contrkk=db.buscar_contraseña(eemail)
                    contrka=db.clave_desencriptada(contrkk)
                    contrk=contrka.decode("utf-8")
                    print("Su contraseña es: ",contrk)
                    db.tiempo()
                    jñ=False
                else:
                    for mh in errores.values():
                        print(mh)
                        db.tiempito()
        elif rsp=="x":
            fr=False
        else:
            print("Por favor ingrese una opción correcta")
            db.tiempito()
            db.limpiar_pantalla()

ok=True
while ok==True:
    menu=Menu()

