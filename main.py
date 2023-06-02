from funciones import *
from funciones_sql import *
import mysql.connector
SERVER = '127.0.0.1'
USER = 'informatica1'
PASSWD = 'bio123'
DB = 'informatica1'
cnx = mysql.connector.connect(user=USER , password=PASSWD , host=SERVER , database=DB, port='3306')
cursor = cnx.cursor()
privilegios="GRANT ALL ON *.* TO 'informatica1'@'127.0.0.1';"
try:
  cursor.execute(privilegios)
  cnx.commit()
  print('Los privilegios se han cambiado')
except mysql.connector.Error as err:
  print('Error al cambiar los privilegios')

usuarios ='''CREATE TABLE usuarios(
   USER CHAR(20) NOT NULL,
   PASSWORD CHAR(20) NOT NULL
)'''
cursor.execute(usuarios)
usuario="""INSERT INTO medicamentos(
    USER ,
    PASSWORD ,
    )VALUES (%s, %s)"""
valores=()
cursor.execute(ususario,valores) 
cnx.commit()
medicamentos ='''CREATE TABLE medicamentos(
   NOMBRE CHAR(20) NOT NULL,
   LOTE CHAR(20)NOT NULL,
   DISTRIBUIDOR CHAR(20)NOT NULL,
   CANTIDAD INT NOT NULL,
   FECHA CHAR(10) NOT NULL,
   PRECIO INT NOT NULL
)'''
cursor.execute(medicamentos)
provedores='''CREATE TABLE provedor(
   NOMBRE CHAR(20) NOT NULL,
   APELLIDO CHAR(20) NOT NULL,
   CODIGO INT NOT NULL,
   ID INT NOT NULL,
   ENTIDAD CHAR(20) NOT NULL,
)'''
cursor.execute(provedores)
ubicaciones ='''CREATE TABLE ubicacion(
   CODIGO CHAR(20) NOT NULL,
   NOMBRE_UBICACION CHAR(20),
   TELEFONO INT,
)'''
cursor.execute(ubicaciones)

menu_principal= ("""
            1.medicamentos
            2.proveedores 
            3.ubicaciones provedores
            4.salir
                """)
menu_medicamentos= ("""
         1.Ingresar un nuevo medicamento. 
         2.Actualizar la información de un medicamento (No. lote)
         3.Buscar un medicamento. (No. lote)
         4.Ver la información de todos los medicamentos almacenados.
         5.Eliminar un medicamento. (No. lote)
         6.Volver al menú principal 
          """)
menu_provedor= ("""
         1.Ingresar un nuevo provedor. 
         2.Actualizar la información de un provedor. (id)
         3.Buscar un provedor. (id)
         4.Ver la información de todos los provedores almacenados.
         5.Eliminar un provedor. (id)
         6.Volver al menú principal 
          """)
menu_ubicacion = ("""
         1.Ingresar una nueva ubicación. 
         2.Actualizar la información de una ubicación.
         3.Buscar una ubicación. 
         4.Ver la información de todas las ubicaciones almacenados.
         5.Eliminar una ubicación. 
         6.Volver al menú principal 
          """)

while True:
  menu=input('Seleccione una opción:\n1.Ingresar al sistema\n2.Salir\n')
  if menu=='1':
    consulta = "SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s"
    parametros = (usuario, contraseña)
    cursor.execute(consulta, parametros)
    resultado = cursor.fetchone()
    if resultado:
        print("Inicio de sesión exitoso.")
        print(menu_principal)
        x = input("Seleccione la opción del menú que desea utilizar: ")
        if x == 1:
            mostrarmenu = True
            while mostrarmenu:
                print(menu_medicamentos)
                y = input("Ingrese el menú de mecicamento que desea utilizar: ")
                if y == 1:
                    ingresar_medicamento()
                elif y == 2:
                    menu_actualizacion=input('Seleccione el dato que desea actualizar:1.Lote\n2.Distribuidor\n3.Cantidad\n4.Fecha\n5.Precio\n6.Salir\n')
                    if menu_actualizacion=='1':
                        if buscar_lote():
                            sql='UPDATE medicamentos SET nombre=%s WHERE lote=%s'
                            nombre_med=nombre()
                            val=(nombre_med,lote())
                            cursor.execute(sql,val)
                            cnx.commit()

                elif y == 3:
                    buscar_medicamento=buscar_lote()
                elif y == 4:
                    ver_medicamentos()
                elif y == 5:

                elif y == 6:
                    mostrarmenu = False
                    break
                else:
                    print("ERROR! el menu no esta disponible, ingrese otro")
                    continue
        elif x == 2:
            mostrarmenu2 = True
            while mostrarmenu2:
                print(menu_provedor)
                z = input("ingrese el menu de provedores que desea utilizar: ")
                if z == 1:
                    ingresar_provedor()
                elif z == 2:
                    menu_actualizacion=input('Seleccione el dato que desea actualizar:1.Código\n2.Distribuidor\n3.Cantidad\n4.Fecha\n5.Precio\n6.Salir\n')
                elif z == 3:  

                elif z == 4:
                    ver_provedores()
                elif z == 5:

                elif z == 6:
                    mostrarmenu2 = False
                    break
                else:
                    print("ERROR! el menu no esta disponible, ingrese otro")
                    continue
        elif x == 3: 
            mostrarmenu3 = True
            while mostrarmenu3 :
                print(menu_ubicacion)
                w = input("ingrese el menu de ubicacion que desea utilizar: ")
                if w == 1:
                    ingresar_ubicacion()
                elif w == 2:

                elif w == 3:  

                elif w == 4:
                    ver_ubicaciones()
                elif w == 5:

                elif w == 6:
                    mostrarmenu3 = False
                    break
                else:
                    print("ERROR! el menu no esta disponible, ingrese otro")
                    continue
        elif x == 4:
            conexion.close()
            break 
        else:
            print("ERROR! el menu no esta disponible, ingrese otro")
    else:
        print("Usuario o contraseña incorrectos. Intente nuevamente.")
        validar_usuario()
  elif menu=='2':
      conexion.close()
      break
  else:
      print('Ingrese una opción válida')
      continue