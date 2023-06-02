import string 
from datetime import datetime

def validacion_num(x):
  """
  Esta es una descripción de valida_num.

  Esta función válida que la información dada por el usuario sea de caracter numérico.
  A la función se le ingresa un valor str y devuelve un valor booleano, True si el caracter es numérico y
  False si es un caracter diferente

  Parámetros:
  - x: el dato ingresado por el ususario.

  Devuelve:
  Un valor booleano(True/False).
  """
  try:
    int(x)
    return True
  except ValueError:
    return False
pass
def validacion_alphanum_caracter(p):
  """
  Esta es una descripción de valida_alphanum_caracter.

  Esta función válida que la información dada por el usuario sea de caracter alfanumérico.
  A la función se le ingresa un valor str y devuelve un valor booleano, True si el caracter es alfanumérico y
  False si es un caracter diferente

  Parámetros:
  - x: el dato ingresado por el ususario.

  Devuelve:
  Un valor booleano(True/False).
  """
  abc=string.ascii_letters+'0123456789-#'
  for letra in p:
    if letra in abc:
      continue
    else:
      return False
  return True
pass
def validar_fecha(fecha):
  """
  Esta es una descripción de validar_fecha.

  Esta función le pide la fecha  en la que se ingreso el medicamento al usuario y válida que se encuentre en el formato
  correcto,devuelve un valor booleano True si el dato ingresado está en el formato correcto o False si es un formato diferente.

  Devuelve:
  Un valor booleano (True/False).
  """
  try:
    fecha=datetime.strptime(fecha,"%Y-%m-%d")
    return True
  except ValueError:
    return False
pass
   
def validacion_alpha(nombre):
  """
  Esta es una descripción de valida_alpha.

  Esta función válida que la información dada por el usuario sea de caracter alfabético.
  A la función se le ingresa un valor str y devuelve un valor booleano, True si el caracter es alfabético y
  False si es un caracter diferente.

  Parámetros:
  - x: el dato ingresado por el ususario.

  Devuelve:
  Un valor booleano(True/False).
  """
  for i in nombre:
    try:
      int(i)
      print('Ingrese un caracter valido')
      return False
    except ValueError:
      pass
  return True
pass

def nombre():
  """
  Esta es una descripción de nombre.

  Esta función le pide el nombre del medicamento al usuario y válida que se encuentre en el formato
  correcto, devuelve el dato ingresado si esta en el formato correcto o una advertencia si no es
  correcto.

  Devuelve:
  un valor str.
  """
  while True:
      nombre_med=input('Ingrese el nombre del medicamento:\n')
      if validacion_alpha(nombre_med)==True:
          return nombre_med
      else:
          print('Ingrese el nombre en el formato válido')
          continue
pass
      
def lote():
  """
  Esta es una descripción de lote.

  Esta función le pide el lote del medicamento al usuario y válida que se encuentre en el formato
  correcto, devuelve el dato ingresado si esta en el formato correcto o una advertencia si no es
  correcto.

  Devuelve:
  un valor str.
  """
  while True:
    lote=input('Ingrese el lote del medicamento:\n')
    if validacion_alphanum_caracter(lote):
      return lote
    else:
      print("Ingrese el lote en el formato correcto")
      continue
pass

def distribuidor():
  """
  Esta es una descripción de distribuidor.

  Esta función le pide el distribuidor del medicamento al usuario y válida que se encuentre en el formato
  correcto, devuelve el dato ingresado si esta en el formato correcto o una advertencia si no es
  correcto.

  Devuelve:
  Un valor str.
  """
  while True:
    distribuidor=input('Ingrese el distribuidor del medicamento:\n')
    if validacion_alpha(distribuidor)==True:
        return distribuidor
    else:
        print('Ingrese el distribubidor en el formato válido')
        continue
pass

def cantidad():
  """
  Esta es una descripción de cantidad.

  Esta función le pide la cantidad de medicamento que se va a ingresar al usuario y válida que esté dato se
  encuentre en el formato correcto, devuelve el dato ingresado si esta en el formato correcto o una advertencia si no es
  correcto.

  Devuelve:
  Un valor str.
  """
  while True:
    cantidad=input('Ingrese la cantidad de medicamento:\n')
    if validacion_num(cantidad)==True:
        return cantidad
    else:
        print('Ingrese la cantidad en un formato coreccto')
        continue
pass
def fecha():
  while True:
    fecha_llegada=input('Ingrese la fecha en la que llega el medicamento(Formato AAAA-MM-DD):\n')
    if validar_fecha(fecha_llegada)==True:
        return fecha_llegada
    else:
        print('Ingrese la fecha en el formato correcto')
        continue
pass

def precio():
  """
  Esta es una descripción de precio.

  Esta función le pide el precio de venta del medicamento al usuario y válida que se encuentre en el formato
  correcto, devuelve el dato ingresado si esta en el formato correcto o una advertencia si no es
  correcto.

  Devuelve:
  Un valor str.
  """
  while True:
    precio=input('Ingrese el valor por unidad del medicamento:\n')
    if validacion_num(precio)==True:
      return precio
    else:
      print('Ingrese el precio en el formato correcto')
      continue
pass
def nombre_provedor():
  """
  Esta es una descripción de nombre_provedor.

  Esta función le pide el nombre del provedor al usuario y válida que se encuentre en el formato
  correcto, devuelve el dato ingresado si esta en el formato correcto o una advertencia si no es
  correcto.

  Devuelve:
  Un valor str.
  """
  while True:
      nombre=input('Ingrese su nombre:\n')
      if validacion_alpha(nombre)==True:
          return nombre
      else:
          print('Ingrese el nombre en el formato válido')
          continue
pass

def apellido():
  """
  Esta es una descripción de apellido.

  Esta función le pide el apellido del provedor al usuario y válida que se encuentre en el formato
  correcto, devuelve el dato ingresado si esta en el formato correcto o una advertencia si no es
  correcto.

  Devuelve:
  Un valor str.
  """
  while True:
      apellido=input('Ingrese su apellido:\n')
      if validacion_alpha(apellido)==True:
          return apellido
      else:
          print('Ingrese el apellido en el formato válido')
          continue
pass

def identificacion():
  """
  Esta es una descripción de identificacion.

  Esta función le pide la identificación del provedor al usuario y válida que se encuentre en el formato
  correcto, devuelve el dato ingresado si esta en el formato correcto o una advertencia si no es
  correcto.

  Devuelve:
  Un valor str.
  """
  while True:
    id=input("Ingrese su identificación en formato numérico(sin puntos, comas o espacios): ")
    if validacion_num(id)==True:
       return id
    else:
      print("Ingrese la identificaicón en el formato correcto")
      continue
pass

def codigo():
  """
  Esta es una descripción de codigo.

  Esta función le pide el codigo del provedor al usuario y válida que se encuentre en el formato
  correcto, devuelve el dato ingresado si esta en el formato correcto o una advertencia si no es
  correcto.

  Devuelve:
  Un valor str.
  """
  while True:
    codigo=input("Ingrese el codigo en el formato alfanumérico: ")
    if validacion_alphanum_caracter(codigo)==True:
      return codigo
    else:
      print("Ingrese en el formato correcto")
      continue
pass

def entidad():
  """
  Esta es una descripción de entidad.

  Esta función le pide la entidad a la que pertenece el provedor al usuario y válida que se encuentre en el formato
  correcto, devuelve el dato ingresado si esta en el formato correcto o una advertencia si no es
  correcto.

  Devuelve:
  Un valor str.
  """
  while True:
    entidad=input('Ingrese la entidad a la que peretenece:\n')
    if validacion_alpha(entidad)==True:
      return entidad
    else:
      print('Ingrese la entidad en el formato válido')
      continue
pass

def nombre_ubicacion():
  """
  Esta es una descripción de nombre_ubicacion.

  Esta función le pide el nombre de la ubicacion al usuario y válida que se encuentre en el formato
  correcto, devuelve el dato ingresado si esta en el formato correcto o una advertencia si no es
  correcto.

  Devuelve:
  Un valor str.
  """
  while True:
    nom_ubicacion=input('Ingrese la ubicacion:\n')
    if validacion_alphanum_caracter(nom_ubicacion):
      return nom_ubicacion
    else:
      print("Ingrese la ubicacion en el formato correcto")
      continue
pass

def telefono():
  """
  Esta es una descripción de telefono.

  Esta función le pide el número de telefono del provedor al usuario y válida que se encuentre en el formato
  correcto, devuelve el dato ingresado si esta en el formato correcto o una advertencia si no es
  correcto.

  Devuelve:
  Un valor str.
  """
  while True:
    telefono=input('Ingrese un número de teléfono:\n')
    if validacion_num(telefono)==True:
      return telefono
    else:
      print('Ingrese el número de teléfono en el formato correcto')
      continue
pass