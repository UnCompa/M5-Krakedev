from informacion import agregar_nombre, agregar_edad, obtener_nombre_pacientes, obtener_edad_pacientes, obtener_mayor, obtener_menor

cantidad_pacientes = int(input('¿Cuantos pacientes desea ingresar?: '))

for i in range(cantidad_pacientes):
  nombre_paciente = input('Nombre completo del paciente: ')
  nombre = nombre_paciente.split(' ')[0]
  apellido = nombre_paciente.split(' ')[1]
  edad_paciente = int(input('Año de nacimiento del paciente: '))
  agregar_nombre(nombre=nombre,apellido=apellido)
  agregar_edad(edad_paciente)

print("NOMBRES DE LOS PACIENTES----")  
print(obtener_nombre_pacientes())
print("EDADES DE LOS PACIENTES----")  
print(obtener_edad_pacientes())
print("PACIENTE MAYOR----")  
obtener_mayor()
print("PACIENTE MENOR----")  
obtener_menor()