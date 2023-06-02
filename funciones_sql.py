from funciones import *
def validar_usuario():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    cursor = conexion.cursor()
    consulta = "SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s"
    parametros = (usuario, contraseña)
    cursor.execute(consulta, parametros)
    resultado = cursor.fetchone()
    if resultado:
        print("Inicio de sesión exitoso.")
        # Aquí puedes continuar con el resto de tu código
    else:
        print("Usuario o contraseña incorrectos. Intente nuevamente.")
        validar_usuario()
validar_usuario()

def ingresar_medicamento():
   medicamento_insert="""INSERT INTO medicamentos(
    NOMBRE ,
    LOTE ,
    DISTRIBUIDOR ,
    CANTIDAD ,
    FECHA ,
    PRECIO
    )VALUES (%s, %s, %s, %s, %s, %s)"""
   valores=(nombre(), lote(), distribuidor(), cantidad(), fecha(), precio())
   cursor.execute(medicamento_insert,valores) 
   cnx.commit()

def ingresar_provedor():
   provedor_insert="""INSERT INTO provedor(
    NOMBRE ,
    APELLIDO ,
    CODIGO ,
    ID ,
    ENTIDAD 
    )VALUES (%s, %s, %s, %s, %s)"""
   valores=(nombre_provedor(), apellido(), codigo(), identificacion(), entidad())
   cursor.execute(provedor_insert,valores) 
   cnx.commit()

def ingresar_ubicacion():
   ubicacion_insert="""INSERT INTO ubicacion(
    CODIGO ,
    NOMBRE ,
    TELEFONO 
    )VALUES (%s, %s, %s)"""
   valores=(codigo(), nombre_ubicacion(), telefono())
   cursor.execute(ubicacion_insert,valores) 
   cnx.commit()

def buscar_lote():
   lote=lote()
   sql='SELECT lote FROM medicamentos WHERE lote=%s'
   cursor.execute(sql,lote)
   resultado=cursor.fechone()
   if lote == resultado[1]:
      return lote
   else:
      print('El lote no se encuentra en la base de datos')
      return False
def actualizar_nombre_medicamento(lote):
   sql='UPDATE medicamentos SET nombre=%s WHERE lote=%s'
   nombre_med=nombre()
   val=(nombre_med,lote())
   cursor.execute(sql,val)
   cnx.commit()

def buscar_medicamento():
   lote=lote()
   sql='SELECT * FROM medicamento WHERE lote=%s'
   cursor.execute(sql,lote())

def ver_medicamentos():
   sql = "SELECT * FROM medicamentos"
   cursor.execute(sql)
   results = cursor.fetchall()
   results

def ver_provedores():
   sql = "SELECT * FROM provedores"
   cursor.execute(sql)
   provedores = cursor.fetchall()
   provedores

def ver_ubicaciones():
   sql = "SELECT * FROM ubicaciones"
   cursor.execute(sql)
   ubicaciones = cursor.fetchall()
   ubicaciones

def actualizar_medicamento():
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
         menu_actualizacion=input('Seleccione el dato que desea actualizar:1.Lote\n2.Distribuidor\n3.Cantidad\n4.Fecha\n5.Precio\n6.Salir\n')
         if menu_actualizacion=='1':
            lote_nuevo=lote()
            consulta = "UPDATE medicamentos SET lote = %s WHERE lote = %s"
            cursor.execute(consulta, (lote_nuevo,))
            conexion.commit()
         elif menu_actualizacion=='2':
            distribuidor_nuevo=distribuidor()
            consulta = "UPDATE medicamentos SET distribuidor = %s WHERE lote = %s"
            cursor.execute(consulta, (distribuidor_nuevo,))
            conexion.commit()
         elif menu_actualizacion=='3':
            cantidad_nueva=cantidad()
            consulta = "UPDATE medicamentos SET cantidad = %s WHERE lote = %s"
            cursor.execute(consulta, (cantidad_nueva,))
            conexion.commit()
         elif menu_actualizacion=='4':
            fecha_nueva=fecha()
            consulta = "UPDATE medicamentos SET fecha = %s WHERE lote = %s"
            cursor.execute(consulta, (fecha_nueva,))
            conexion.commit()
         elif menu_actualizacion=='5':
            precio_nuevo=precio()
            consulta = "UPDATE medicamentos SET precio = %s WHERE lote = %s"
            cursor.execute(consulta, (precio_nuevo,))
            conexion.commit()
         elif menu_actualizacion=='6':
            break
         else:
            print('Ingrese una opción válida')
            continue
   else:
      print("No se encontró ningún medicamento con ese número de lote.")
