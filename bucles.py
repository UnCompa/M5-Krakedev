datos = []
cantidad = int(input("¿Cuántos datos desea ingresar? "))

for i in range(cantidad):
    dato = input('escriba el dato: ')

    if dato.isdigit():
        datos.append(dato)
    elif dato.isalpha():
        datos.append(dato)
    else:
        print(f"El dato '{dato}' no es válido. Ingrese un número o un texto.")
print(f'Sus datos son: {datos}')