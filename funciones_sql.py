from funciones import *
import mysql.connector

def validar_usuario():
    """
  Esta es una descripción de valida_usuario.

  Esta función válida que el usuario y la contraseña recibidos se necuentren en el sistema, es decir, en la base de datos.
  Esta función retorna un True si el usuario y la contraseña se encuentran en la base de datos  y si estos coinciden con los entregados,
  y un False en caso contrario

  Devuelve:
  Un valor booleano(True/False).
  """
    conexion = mysql.connector.connect(
         host="localhost",  # El host de tu base de datos
         user="informatica1",    # El nombre de usuario de la base de datos
         password="bio123",  # La contraseña de la base de datos
         database="informatica1"  # El nombre de la base de datos
     )
    usuario = 'Juan'
    contraseña = '1234'
    cursor = conexion.cursor()
    consulta = "SELECT * FROM usuarios WHERE Usuarios = %s AND Password = %s"
    parametros = (usuario, contraseña)
    cursor.execute(consulta, parametros)
    resultado = cursor.fetchone()
    if resultado:
        print("Inicio de sesión exitoso.")
        cursor.close()
        conexion.close()
        return True
        # Aquí puedes continuar con el resto de tu código
    else:
        print("Usuario o contraseña incorrectos. Intente nuevamente.")
        validar_usuario()
pass

def ingresar_medicamento():
   """
   Esta es una descripción de ingresar_medicamento.

   Esta función permite ingresar los datos pedidos al usuario al esquema de medicamnetos en la base de datos.
   La función realiza una conexión con la base de datos y luego inserta los datos a esté esquema.
   """
   medicamento_insert="""INSERT INTO medicamentos(
    Nombre ,
    Lote ,
    Distribuidor ,
    Cantidad ,
    Fecha ,
    Precio
    )VALUES (%s, %s, %s, %s, %s, %s)"""
   valores=(nombre(), lote(), distribuidor(), cantidad(), fecha(), precio())
   cursor.execute(medicamento_insert,valores) 
   cnx.commit()
   pass
   
def actualizar_medicamento():
   """
  Esta es una descripción de actualizar_medicamento.

  Esta función permite actualizar los datos de un medicamento.
  La función pide un lote, que es el parámetro de busqueda del medicamento en la base de datos,
  luego imprime la informacion encontrada con ese parámetro y te muestra un menú para que se escoja el dato 
  que se va actualizar, al seleccionar una opción va a pedir el nuevo dato que se va a ingresar a la base de datos
  o da la opción de salir de esté menú.

  """
   while True:
      numero_lote = lote()
   # Consultar el medicamento basado en el número de lote
      consulta = "SELECT * FROM medicamentos WHERE lote = %s"
      cursor.execute(consulta, (numero_lote,))
      medicamento = cursor.fetchone()
      # Verificar si se encontró el medicamento
      if medicamento is not None:
         print("Medicamento encontrado:")
         print("Número de lote:", medicamento[0])
         print("Nombre de medicamento:", medicamento[1])
         print("Distribuidor:", medicamento[2])
         print("Cantidad en bodega:", medicamento[3])
         print("Fecha de llegada:", medicamento[4])
         print("Precio de venta:", medicamento[5])
         
         while True:
            menu_actualizacion=input('Seleccione el dato que desea actualizar:\n1.Lote\n2.Distribuidor\n3.Cantidad\n4.Fecha\n5.Precio\n6.Salir\n')
            if menu_actualizacion=='1':
               lote_nuevo=lote()
               consulta = "UPDATE medicamentos SET Lote = %s WHERE lote = %s"
               cursor.execute(consulta, (lote_nuevo,))
               conexion.commit()
            elif menu_actualizacion=='2':
               distribuidor_nuevo=distribuidor()
               consulta = "UPDATE medicamentos SET Distribuidor = %s WHERE lote = %s"
               cursor.execute(consulta, (distribuidor_nuevo,))
               conexion.commit()
            elif menu_actualizacion=='3':
               cantidad_nueva=cantidad()
               consulta = "UPDATE medicamentos SET Cantidad = %s WHERE lote = %s"
               cursor.execute(consulta, (cantidad_nueva,))
               conexion.commit()
            elif menu_actualizacion=='4':
               fecha_nueva=fecha()
               consulta = "UPDATE medicamentos SET Fecha = %s WHERE lote = %s"
               cursor.execute(consulta, (fecha_nueva,))
               conexion.commit()
            elif menu_actualizacion=='5':
               precio_nuevo=precio()
               consulta = "UPDATE medicamentos SET Precio = %s WHERE lote = %s"
               cursor.execute(consulta, (precio_nuevo,))
               conexion.commit()
            elif menu_actualizacion=='6':
               break
            else:
               print('Ingrese una opción válida')
               continue
      else:
         print("No se encontró ningún medicamento con ese número de lote.")
         continue
pass

def buscar_medicamento():
   """
   Esta es una descripción de buscar_medicamento.

   Esta función permite buscar un medicamento en el esquema de medicamentos en la base de datos.
   La función realiza una conexión con la base de datos y luego filtra los datos del esquema,
   para mostrar únicamente el medicamento relacionado con el parámetro, en caso de que no exista
   alertara al usuario de esto.
   """
   lote=lote()
    # Establecer la conexión con la base de datos
   conexion = mysql.connector.connect(
      host="localhost",  
      user="informatica1",    
      password="bio123",  
      database="informatica1"
   )
   cursor = conexion.cursor()
   consulta = "SELECT * FROM medicamentos WHERE lote = %s"
   cursor.execute(consulta, (lote,))
   medicamento = cursor.fetchone()
    # Verificar si se encontró el medicamento
   if medicamento:
      print("Medicamento encontrado:")
      print("Nombre del medicamento:", medicamento[0])
      print("Lote del medicamento:",medicamento[1])
      print("Distribuidor:", medicamento[2])
      print("Cantidad en bodega:", medicamento[3])
      print("Fecha de llegada:", medicamento[4])
      print("Precio de venta:", medicamento[5])
   else:
        print("No se encontró el medicamento con ese nombre.")

    # Cerrar el cursor y la conexión
   cursor.close()
   conexion.close()
   pass

def ver_medicamentos():
   """
   Esta es una descripción de ver_medicamentos.

   Esta función realiza una conexión con la base de datos, luego selecciona la 
   información que contenga el esquema de medicamentos y la muestra al usuario.

   """
   conexion = mysql.connector.connect(
         host="localhost",  # El host de tu base de datos
         user="informatica1",    # El nombre de usuario de la base de datos
         password="bio123",  # La contraseña de la base de datos
         database="informatica1"  # El nombre de la base de datos
    )
   cursor = conexion.cursor()
   sql = "SELECT * FROM medicamentos"
   cursor.execute(sql)
   results = cursor.fetchall()
   print(results)
   cursor.close()
   conexion.close()
   pass

def eliminar_medicamento():
   """
   Esta es una descripción de eliminar_medicamento.

   Esta función pide un parametro (lote) al usuario que es el utilizado para la busqueda
   en el esquema,realiza una conexión con la base de datos, luego selecciona la 
   información que contenga el parametro y la elimina del esquema de medicamentos.

   """
   lote=lote()
    # Establecer la conexión con la base de datos
   conexion = mysql.connector.connect(
         host="localhost",  
         user="informatica1",    
         password="bio123",  
         database="informatica1"
    )
   cursor = conexion.cursor()
   consulta = "DELETE FROM medicamentos WHERE lote = %s"
   cursor.execute(consulta, (lote,))
   conexion.commit()
   if cursor.rowcount > 0:
        print("El medicamento se eliminó correctamente.")
   else:
        print("No se encontró el medicamento con ese nombre.")
   cursor.close()
   conexion.close()
   pass

def ingresar_provedor():
   """
   Esta es una descripción de ingresar_provedor.

   Esta función permite ingresar los datos pedidos al usuario al esquema de provedores en la base de datos.
   La función realiza una conexión con la base de datos y luego inserta los datos a esté esquema.
   """
   provedor_insert="""INSERT INTO provedor(
    Nombre ,
    Apellido ,
    Codigo ,
    Id ,
    Entidad 
    )VALUES (%s, %s, %s, %s, %s)"""
   valores=(nombre_provedor(), apellido(), codigo(), identificacion(), entidad())
   cursor.execute(provedor_insert,valores) 
   cnx.commit()
   pass

def actualizar_provedor():
   """
   Esta es una descripción de actualizar_provedor.

   Esta función permite actualizar los datos de un provedor.
   La función pide un codigo, que es el parámetro de busqueda del provedor en la base de datos,
   luego imprime la informacion encontrada con ese parámetro y te muestra un menú para que se escoja el dato 
   que se va actualizar, al seleccionar una opción va a pedir el nuevo dato que se va a ingresar a la base de datos
   o da la opción de salir de esté menú.

    """
   while True:
      id=identificacion()
   # Consultar el provedor basado en el código
      consulta = "SELECT * FROM provedores WHERE id = %s"
      cursor.execute(consulta, (id,))
      provedor = cursor.fetchone()
      # Verificar si se encontró el provedor
      if provedor is not None:
         print("Provedor encontrado:")
         print("Nombre:",provedor[0])
         print("Apellido:", provedor[1])
         print("Codigo:", provedor[2])
         print("Identificación:", provedor[3])
         print("Entidad:", provedor[4])
         
         while True:
            menu_actualizacion=input('Seleccione el dato que desea actualizar:\n1.Nombre\n2.Apellido\n3.Codigo\n4.Identificacion\n5.Entidad\n6.Salir\n')
            if menu_actualizacion=='1':
               nombre_nuevo=nombre_provedor()
               consulta = "UPDATE provedores SET nombre = %s WHERE id = %s"
               cursor.execute(consulta, (nombre_nuevo,))
               conexion.commit()
            elif menu_actualizacion=='2':
               apellido_nuevo=apellido()
               consulta = "UPDATE provedores SET apellido = %s WHERE id = %s"
               cursor.execute(consulta, (apellido_nuevo,))
               conexion.commit()
            elif menu_actualizacion=='3':
               codigo_nuevo=codigo()
               consulta = "UPDATE provedores SET CODIGO = %s WHERE id = %s"
               cursor.execute(consulta, (codigo_nuevo,))
               conexion.commit()
            elif menu_actualizacion=='4':
               id_nueva=identificacion()
               consulta = "UPDATE provedores SET ID = %s WHERE id = %s"
               cursor.execute(consulta, (id_nueva,))
               conexion.commit()
            elif menu_actualizacion=='5':
               entidad_nuevo=entidad()
               consulta = "UPDATE provedores SET entidad = %s WHERE id = %s"
               cursor.execute(consulta, (entidad_nuevo,))
               conexion.commit()
            elif menu_actualizacion=='6':
               break
            else:
               print('Ingrese una opción válida')
               continue
      else:
         print("No se encontró ningún provedor con ese código.")
         continue
pass

def buscar_provedor():
   """
   Esta es una descripción de buscar_provedor.

   Esta función permite buscar un provedor en el esquema de provedores en la base de datos.
   La función realiza una conexión con la base de datos y luego filtra los datos del esquema,
   para mostrar únicamente el provedor relacionado con el parámetro, en caso de que no exista
   alertara al usuario de esto.
   """
   codigo=codigo()
    # Establecer la conexión con la base de datos
   conexion = mysql.connector.connect(
      host="localhost",  
      user="informatica1",    
      password="bio123",  
      database="informatica1"
   )
   cursor = conexion.cursor()
   consulta = "SELECT * FROM provedores WHERE codigo = %s"
   cursor.execute(consulta, (lote,))
   provedor = cursor.fetchone()
    # Verificar si se encontró el provedor
   if provedor:
      print("Provedor encontrado:")
      print("Nombre del provedor:", provedor[1])
      print("Apellido:", provedor[2])
      print("Codigo:", provedor[3])
      print("Identificacion:", provedor[4])
      print("Entidad:", provedor[5])
   else:
        print("No se encontró el provedor con ese codigo.")

    # Cerrar el cursor y la conexión
   cursor.close()
   conexion.close()
   pass

def ver_provedores():
   """
   Esta es una descripción de ver_provedores.

   Esta función realiza una conexión con la base de datos, luego selecciona la 
   información que contenga el esquema de provedores y la muestra al usuario.

   """
   conexion = mysql.connector.connect(
         host="localhost",  # El host de tu base de datos
         user="informatica1",    # El nombre de usuario de la base de datos
         password="bio123",  # La contraseña de la base de datos
         database="informatica1"  # El nombre de la base de datos
    )
   cursor = conexion.cursor()
   sql = "SELECT * FROM provedores"
   cursor.execute(sql)
   provedores = cursor.fetchall()
   provedores
   pass

def eliminar_provedor():
   """
   Esta es una descripción de eliminar_provedor.

   Esta función pide un parametro (codigo) al usuario que es el utilizado para la busqueda
   en el esquema,realiza una conexión con la base de datos, luego selecciona la 
   información que contenga el parametro y la elimina del esquema de provedores.

   """
   codigo=codigo()
    # Establecer la conexión con la base de datos
   conexion = mysql.connector.connect(
      host="localhost",  
      user="informatica1",    
      password="bio123",  
      database="informatica1"
    )
   cursor = conexion.cursor()
   consulta = "DELETE FROM provedores WHERE codigo = %s"
   cursor.execute(consulta, (codigo,))
   conexion.commit()
   if cursor.rowcount > 0:
        print("El provedor se eliminó correctamente.")
   else:
        print("No se encontró el provedor con ese codigo.")
   cursor.close()
   conexion.close()
   pass

def ingresar_ubicacion():
   """
   Esta es una descripción de ingresar_ubicación.

   Esta función permite ingresar los datos pedidos al usuario al esquema de ubicaciones en la base de datos.
   La función realiza una conexión con la base de datos y luego inserta los datos a esté esquema.
   """
   ubicacion_insert="""INSERT INTO ubicacion(
    Codigo ,
    Nombre ,
    Telefono 
    )VALUES (%s, %s, %s)"""
   valores=(codigo(), nombre_ubicacion(), telefono())
   cursor.execute(ubicacion_insert,valores) 
   cnx.commit()
   pass

def actualizar_ubicacion():
   """
    Esta es una descripción de actualizar_ubicacion.

    Esta función permite actualizar los datos de una ubicación.
    La función pide un código, que es el parámetro de busqueda de la ubicación en la base de datos,
    luego imprime la informacion encontrada con ese parámetro y te muestra un menú para que se escoja el dato 
    que se va actualizar, al seleccionar una opción va a pedir el nuevo dato que se va a ingresar a la base de datos
    o da la opción de salir de esté menú.

    """
   while True:
      codigo=codigo()
   # Consultar el medicamento basado en el número de lote
      consulta = "SELECT * FROM ubicaciones WHERE codigo = %s"
      cursor.execute(consulta, (codigo,))
      ubicacion = cursor.fetchone()
      # Verificar si se encontró el medicamento
      if ubicacion is not None:
         print("Ubicación encontrada:")
         print("Codigo:", ubicacion[0])
         print("Nombre:",ubicacion[1])
         print("Telefono:", ubicacion[2])
         while True:
            menu_actualizacion=input('Seleccione el dato que desea actualizar:\n1.Codigo\n2.Nombre\n3.Telefono\n4.Salir\n')
            if menu_actualizacion=='1':
               codigo_nuevo=codigo()
               consulta = "UPDATE ubicaciones SET CODIGO = %s WHERE codigo = %s"
               cursor.execute(consulta, (codigo_nuevo,))
               conexion.commit()
            elif menu_actualizacion=='2':
               nombre_nuevo=nombre_ubicacion()
               consulta = "UPDATE ubicaciones SET nombre = %s WHERE codigo = %s"
               cursor.execute(consulta, (nombre_nuevo,))
               conexion.commit()            
            elif menu_actualizacion=='3':
               tel_nuevo=telefono()
               consulta = "UPDATE ubicaciones SET telefono = %s WHERE codigo = %s"
               cursor.execute(consulta, (tel_nuevo,))
               conexion.commit()
            elif menu_actualizacion=='4':
               break
            else:
               print('Ingrese una opción válida')
               continue
      else:
         print("No se encontró ninguna ubicación con ese código.")
         continue
pass

def buscar_ubicacion():
   """
   Esta es una descripción de buscar_ubicacion.

   Esta función permite buscar una ubicación en el esquema de ubicaciones en la base de datos.
   La función realiza una conexión con la base de datos y luego filtra los datos del esquema,
   para mostrar únicamente la ubicación relacionada con el parámetro, en caso de que no exista
   alertara al usuario de esto.
   """
   codigo=codigo()
    # Establecer la conexión con la base de datos
   conexion = mysql.connector.connect(
      host="localhost",  
      user="informatica1",    
      password="bio123",  
      database="informatica1"
   )
   cursor = conexion.cursor()
   consulta = "SELECT * FROM ubicaciones WHERE codigo = %s"
   cursor.execute(consulta, (codigo,))
   ubicacion = cursor.fetchone()
    # Verificar si se encontró la ubicacion
   if ubicacion:
      print("Ubicación encontrada:")
      print("Código:", ubicacion[0])
      print("Nombre:", ubicacion[1])
      print("Teléfono:", ubicacion[2])
   else:
        print("No se encontró la ubicación con ese código.")
    # Cerrar el cursor y la conexión
   cursor.close()
   conexion.close()
   pass

def ver_ubicaciones():
   """
   Esta es una descripción de ver_ubicaciones.

   Esta función realiza una conexión con la base de datos, luego selecciona la 
   información que contenga el esquema de ubicaciones y la muestra al usuario.

   """
   conexion = mysql.connector.connect(
         host="localhost",  # El host de tu base de datos
         user="informatica1",    # El nombre de usuario de la base de datos
         password="bio123",  # La contraseña de la base de datos
         database="informatica1"  # El nombre de la base de datos
    )
   cursor = conexion.cursor()
   sql = "SELECT * FROM ubicaciones"
   cursor.execute(sql)
   ubicaciones= cursor.fetchall()
   ubicaciones
   pass
def eliminar_ubicacion():
   """
   Esta es una descripción de eliminar_ubicacion.

   Esta función pide un parametro (codigo) al usuario que es el utilizado para la busqueda
   en el esquema,realiza una conexión con la base de datos, luego selecciona la 
   información que contenga el parametro y la elimina del esquema de ubicaciones.

   """
   codigo=codigo()
    # Establecer la conexión con la base de datos
   conexion = mysql.connector.connect(
      host="localhost",  
      user="informatica1",    
      password="bio123",  
      database="informatica1"
    )
   cursor = conexion.cursor()
   consulta = "DELETE FROM ubicaciones WHERE codigo = %s"
   cursor.execute(consulta, (codigo,))
   conexion.commit()
   if cursor.rowcount > 0:
        print("La ubicación se eliminó correctamente.")
   else:
        print("No se encontró la ubicación con ese código.")
   cursor.close()
   conexion.close()
   pass