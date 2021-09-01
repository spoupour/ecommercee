dbconf = {
    'host':'localhost',
    'database':'e-commerce',
    'user':'root',
    'password':''
 }
queries={
    #cliente
    'add_cliente':'INSERT INTO clientes (usuario, nombre, apellido, contraseña, email) VALUES (%s, %s, %s, %s, %s)',
    'get_user':'SELECT cliente_id FROM clientes WHERE email= %s',
    'get_usuario':'SELECT * FROM clientes WHERE email= %s',
    'get_usuarioo':'SELECT cliente_id FROM clientes WHERE usuario= %s',
    'get_contraseña':'SELECT contraseña FROM clientes WHERE email=%s',
    'get_contra':'SELECT contraseña FROM clientes WHERE cliente_id=%s',
    'traer_usuario':'SELECT usuario FROM clientes WHERE cliente_id=%s',
    'consultar_cliente': 'SELECT contraseña FROM clientes WHERE email=%s',
    'cliente_conid':'SELECT "||SU ID: ", cliente_id, "||Su nombre de usuario: ",usuario, "||Su nombre: ", nombre, "||Su apellido: ",apellido, "||Su email: ", email FROM clientes WHERE cliente_id=%s',
    #productos
    'add_producto':'INSERT INTO productos (codigo, nombre_producto, precio, codigo_categoria, nombre_marca, detalles,stock,vendedor) VALUES (%s, %s, %s, %s, %s, %s,%s,%s)',
    'get_product':'SELECT codigo FROM productos WHERE nombre_producto= %s',
    'todos_productos':'SELECT " ||codigo: ", codigo ," ||nombre: " , nombre_producto , "|| precio: $", precio , "|| Marca: ", nombre_marca ,"|| Detalles: ", detalles FROM productos',
    'todos_productos2':'SELECT " ||codigo: ", codigo ," ||nombre: " , nombre_producto , "|| precio: $", precio , "|| Marca: ", nombre_marca ,"|| Detalles: ", detalles FROM productos WHERE vendedor=%s',
    'ver_stock':'SELECT stock FROM productos WHERE codigo=%s',
    'cod_producto': 'SELECT * from productos WHERE codigo=%s',
    'cod_producto2': 'SELECT "||Codigo: ",codigo, "||Nombre del producto: ", nombre_producto, "||Precio: ",precio, "||Codigo de categoria: ", codigo_categoria, "||Codigo_marca: ", nombre_marca, "||Detalles: ", detalles from productos WHERE codigo=%s',
    'delete_producto':'DELETE FROM productos WHERE codigo=%s',
    'delete_prod':'DELETE FROM productos WHERE vendedor=%s',
    #categorias
    'add_categoria':'INSERT INTO categoria (codigo_categoria,nombre_categoria,descripcion) VALUES (%s, %s, %s)',
    'get_categoria': 'SELECT codigo_categoria FROM categoria WHERE nombre_categoria= %s',
    'nom_categoria': 'SELECT nombre_categoria FROM categoria WHERE codigo_categoria=%s',
    'cod_categoria': 'SELECT codigo_categoria FROM categoria WHERE nombre_categoria=%s',
    'todas_categorias':'SELECT "||CODIGO: ", codigo_categoria, " || Categoria: ", nombre_categoria, "|| Descripcion: ", descripcion FROM categoria',
    #marcas
    'add_marca': 'INSERT INTO marca(nombre_marca,codigo_marca) VALUES (%s,%s)',
    'traer_marca': 'SELECT codigo_marca FROM marca WHERE nombre_marca=%s',
    'traer_cod_marca':'SELECT * FROM marca WHERE codigo_marca=%s',
    'todas_marcas':'SELECT "||NOMBRE: ",nombre_marca, "||CODIGO: ", codigo_marca FROM marca',
    'codigo_marca': 'SELECT codigo_marca FROM marca WHERE nombre_marca=%s',
    'traer_marca2': 'SELECT nombre_marca FROM marca WHERE codigo_marca=%s',
    #metodos de pago
    'crear_metodo': 'INSERT INTO metodo_pago(numero,detalles) VALUES(%s,%s)',
    'traer_metodo': 'SELECT detalles FROM metodo_pago WHERE numero= (%s)',
    'traer_metodo2':'SELECT "RECUERDE INSERTAR TODOS ESTOS DATOS:",detalles, "DE LO CONTRARIO NO SE PODRA REALIZAR EL PAGO" FROM metodo_pago WHERE numero=2',
    #compras
    'comprar': 'INSERT INTO comprar(cliente_id,codigo_producto,metodo_pago,detalles,fecha_compra) VALUES (%s, %s, %s,%s,%s)',
    'borrar_comprar': 'DELETE FROM comprar WHERE cliente_id=%s',
    'get_comprar':'SELECT num_compra FROM comprar WHERE cliente_id=%s',
    'todas_compras':'SELECT codigo_producto FROM comprar WHERE cliente_id=%s',
    'compras':'SELECT "||COMPRÓ EL PRODUCTO: ",codigo_producto, "||METODO DE PAGO: ",metodo_pago, "||DETALLES: ", detalles,"||FECHA DE LA COMPRA: ",fecha_compra FROM comprar WHERE cliente_id=%s',
    #alertas
    'alerta': 'SELECT "No tiene stock en su: " , p.nombre_producto, "Con el código: ", p.codigo FROM productos p WHERE stock=0 and vendedor=%s',
    'codigo':'SELECT codigo FROM productos WHERE stock=0 and vendedor=%s',
    'alertando': 'INSERT INTO alerta(codigo_alerta,fecha_limite,codigo_producto,cliente_id) VALUES (%s, %s, %s, %s)',
    'borrar_alerta':'DELETE FROM alerta WHERE codigo_producto=%s',
    'traer_fecha': 'SELECT fecha_limite FROM alerta WHERE codigo_producto=%s',
    'traer_alerta': 'SELECT * FROM alerta WHERE cliente_id=%s',
    #updates cliente
    'update_usuario':'UPDATE clientes SET usuario=%s WHERE cliente_id=%s ',
    'update_nombre':'UPDATE clientes SET nombre=%s WHERE cliente_id=%s ',
    'update_apellido':'UPDATE clientes SET apellido=%s WHERE cliente_id=%s ',
    'update_contraseña':'UPDATE clientes SET contraseña=%s WHERE cliente_id=%s ',
    'update_email':'UPDATE clientes SET email=%s WHERE cliente_id=%s ',
    #updates producto
    'update_nombre_prod':'UPDATE productos SET nombre_producto=%s WHERE vendedor=%s',
    'update_precio': 'UPDATE productos SET precio=%s WHERE vendedor=%s',
    'update_detalles': 'UPDATE productos SET detalles=%s WHERE vendedor=%s',
    'cambiar_stock': 'UPDATE productos SET stock=%s WHERE codigo=%s ',
    'cambiar_stock3': 'UPDATE productos SET stock=%s WHERE vendedor=%s ',
    #borrar el usuario
    'borrar_usuario': "DELETE FROM clientes WHERE cliente_id=%s",


    
    }

