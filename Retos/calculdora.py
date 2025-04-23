# Uso de inputs para capturar el valor del usuario
ancho = float(input('Ingrese el ancho del rectangulo: '))
altura = float(input('Ingrese el alto del rectangulo: '))

# Calculos
area = ancho * altura
perimetro = (ancho + altura) * 2
superficie = ancho * altura

# Salida del resultado
print(f'La area es: {area}')
print(f'La perimetro es: {perimetro}')
print(f'La superficie es: {superficie}')