print(
'''
Elija su lugar de viaje
1. Ecuador
2. Colombia
3. Perú\n
'''
)

option = int(input('Opcion: '))

print(
'''
Elija la zona de viaje
1. Zona urbana
2. Zona rural
3. Zona perimetral\n
'''
)

zona = int(input('Opcion: '))


velocidad = int(input('Velocidad de viaje (Ej. 10): '))
print(velocidad)
if(option == 1):
  if(zona == 1):
    if(velocidad > 50):
      print('Exceso de velocidad')
    elif (velocidad < 10):
      print('Velocidad baja')
    else:
      print('Velocidad correcta 👍')
  if(zona == 2):
    if(velocidad > 70):
      print('Exceso de velocidad')
    elif(velocidad < 51):
      print('Velocidad baja')
    else:
      print('Velocidad correcta 👍')
  if(zona == 3):
    if(velocidad > 90):
      print('Exceso de velocidad')
    elif(velocidad < 81):
      print('Velocidad baja')
    else:
      print('Velocidad correcta 👍')
if(option == 2):
  if(zona == 1):
    if(velocidad > 30):
      print('Exceso de velocidad')
    elif(velocidad < 10):
      print('Velocidad baja')
    else:
      print('Velocidad correcta 👍')
  if(zona == 2):
    if(velocidad > 80):
      print('Exceso de velocidad')
    elif(velocidad < 31):
      print('Velocidad baja')
    else:
      print('Velocidad correcta 👍')
  if(zona == 3):
    if(velocidad > 100):
      print('Exceso de velocidad')
    elif(velocidad < 81):
      print('Velocidad baja')
    else:
      print('Velocidad correcta 👍')
if(option == 3):
  if(zona == 1):
    if(velocidad > 40):
      print('Exceso de velocidad')
    elif(velocidad < 10):
      print('Velocidad baja')
    else:
      print('Velocidad correcta 👍')
  if(zona == 2):
    if(velocidad > 60):
      print('Exceso de velocidad')
    elif(velocidad < 41):
      print('Velocidad baja')
    else:
      print('Velocidad correcta 👍')
  if(zona == 3):
    if(velocidad > 120):
      print('Exceso de velocidad')
    elif(velocidad < 61):
      print('Velocidad baja')
    else:
      print('Velocidad correcta 👍')