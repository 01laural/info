import string 
from datetime import datetime

def validacion_num(x):
  """
  Esta es una descripción de valida_num.

  Esta función válida que la información dada por el usuario sea de caracter numérico.
  A la función se le ingresa un valor str y debe devolver un valor booleano, True si el caracter es numérico y
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
  abc=string.ascii_letters+'0123456789-#'
  for letra in p:
    if letra in abc:
      continue
    else:
      return False
  return True

def validar_fecha(fecha):
   try:
      fecha=datetime.strptime(fecha,"%Y-%m-%d")
      return True
   except ValueError:
      return False
   
def validacion_alpha(nombre):
  for i in nombre:
    try:
      int(i)
      print('Ingrese un caracter valido')
      return False
    except ValueError:
      pass
  return True

def nombre():
  while True:
      nombre_med=input('Ingrese el nombre del medicamento:\n')
      if validacion_alpha(nombre_med)==True:
          return nombre_med
      else:
          print('Ingrese el nombre en el formato válido')
          continue
      
def lote():
  while True:
    lote=input('Ingrese el lote del medicamento:\n')
    if validacion_alphanum_caracter(lote):
      return lote
    else:
      print("Ingrese el lote en el formato correcto")
      continue

def distribuidor():
  while True:
    distribuidor=input('Ingrese el distribuidor del medicamento:\n')
    if validacion_alpha(distribuidor)==True:
        return distribuidor
    else:
        print('Ingrese el distribubidor en el formato válido')
        continue

def cantidad():
  while True:
    cantidad=input('Ingrese la cantidad de medicamento:\n')
    if validacion_num(cantidad)==True:
        return cantidad
    else:
        print('Ingrese la cantidad en un formato coreccto')
        continue

def fecha():
  while True:
    fecha_llegada=input('Ingrese la fecha en la que llega el medicamento(Formato AAAA-MM-DD):\n')
    if validar_fecha(fecha_llegada)==True:
        return fecha_llegada
    else:
        print('Ingrese la fecha en el formato correcto')
        continue

def precio():
   while True:
    precio=input('Ingrese el valor por unidad del medicamento:\n')
    if validacion_num(precio)==True:
        return precio
    else:
        print('Ingrese el precio en el formato correcto')
        continue

def nombre_provedor():
  while True:
      nombre=input('Ingrese su nombre:\n')
      if validacion_alpha(nombre)==True:
          return nombre
      else:
          print('Ingrese el nombre en el formato válido')
          continue

def apellido():
  while True:
      apellido=input('Ingrese su apellido:\n')
      if validacion_alpha(apellido)==True:
          return apellido
      else:
          print('Ingrese el apellido en el formato válido')
          continue

def identificacion():
  while True:
    id=input("Ingrese su identificación en formato numérico(sin puntos, comas o espacios): ")
    if validacion_num(id)==True:
       return id
    else:
      print("Ingrese la identificaicón en el formato correcto")
      continue

def codigo():
    while True:
        codigo=input("Ingrese el codigo en el formato alfanumérico: ")
        if validacion_alphanum_caracter(codigo)==True:
           return codigo
        else:
            print("Ingrese en el formato correcto")
            continue

def entidad():
  while True:
    entidad=input('Ingrese la entidad a la que peretenece:\n')
    if validacion_alpha(entidad)==True:
        return entidad
    else:
        print('Ingrese la entidad en el formato válido')
        continue

def nombre_ubicacion():
  while True:
    nom_ubicacion=input('Ingrese la ubicacion:\n')
    if validacion_alphanum_caracter(nom_ubicacion):
      return nom_ubicacion
    else:
      print("Ingrese la ubicacion en el formato correcto")
      continue

def telefono():
   while True:
    telefono=input('Ingrese un número de teléfono:\n')
    if validacion_num(telefono)==True:
        return telefono
    else:
        print('Ingrese el número de teléfono en el formato correcto')
        continue

def mi_funcion(parametro1, parametro2):
    """
    Esta es una descripción de mi_funcion.

    Aquí puedes proporcionar más detalles sobre la función,
    incluyendo los parámetros que acepta y el valor que devuelve.

    Parámetros:
    - parametro1: Descripción del primer parámetro.
    - parametro2: Descripción del segundo parámetro.

    Devuelve:
    Una descripción del valor de retorno, si corresponde.
    """
    # Código de la función aquí
    pass