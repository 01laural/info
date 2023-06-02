from funciones import *
from funciones_sql import *
import mysql.connector



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
          
ingreso = False
while True:
  if ingreso == False :
    menu=input('Seleccione una opción:\n1.Ingresar al sistema\n2.Salir\n')
  if menu=='1':
        if ingreso == False :
            ingreso = validar_usuario()
        print(menu_principal)
        x = int(input("Seleccione la opción del menú que desea utilizar: "))
        if x == 1:
            mostrarmenu = True
            while mostrarmenu:
                print(menu_medicamentos)
                y = int(input("Ingrese el menú de mecicamento que desea utilizar: "))
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
                    ji = 0
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
                    ji = 0
                elif z == 4:
                    ver_provedores()
                elif z == 5:
                    ji = 0
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
                elif w == 4:
                    ver_ubicaciones()

                elif w == 6:
                    mostrarmenu3 = False
                    break
                else:
                    print("ERROR! el menu no esta disponible, ingrese otro")
                    continue
        elif x == 4:
            break 
        else:
            print("ERROR! el menu no esta disponible, ingrese otro")
  elif menu=='2':
      break
  else:
      print('Ingrese una opción válida')
      continue