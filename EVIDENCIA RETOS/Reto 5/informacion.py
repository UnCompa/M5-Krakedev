nombre_pacientes = []
edad_pacientes = []
anio_actual = 2025

def agregar_nombre(nombre, apellido):
  paciente = f"{nombre} {apellido}"
  nombre_pacientes.append(paciente)
  
def agregar_edad(edad):
  edad_actual = anio_actual - edad
  edad_pacientes.append(edad_actual)
  
def obtener_nombre_pacientes():
  return nombre_pacientes

def obtener_edad_pacientes():
  return edad_pacientes

def obtener_mayor():
  pacientes_edad = obtener_edad_pacientes()
  paciente_initcial = pacientes_edad[0]
  position = 0
  for i, edad in enumerate(pacientes_edad):
    paciente_eval = edad
    if(paciente_initcial > paciente_eval):
      continue
    else:
      position = i
      paciente_initcial = edad
  pacientes_nombre = nombre_pacientes
  print(f'{pacientes_nombre[position]} con la edad de {paciente_initcial} años es mayor a los demás pacientes.')
    

def obtener_menor():
  pacientes_edad = obtener_edad_pacientes()
  paciente_initcial = pacientes_edad[0]
  position_mayor = 0
  for i, edad in enumerate(pacientes_edad):
    paciente_eval = edad
    if(paciente_initcial < paciente_eval):
      continue
    else:
      position_mayor = i
      paciente_initcial = edad
  pacientes_nombre = nombre_pacientes
  print(f'{pacientes_nombre[position_mayor]} con la edad de {paciente_initcial} años es menor a los demás pacientes.')
