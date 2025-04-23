print(
    """
Elija una opcion
1. Añadir plato al menú.
2. Buscar en el menú.
3. Eliminar plato del menú.
4. Mostrar platos del menú
"""
)

platos = ["Papas con cuero", "Encebollado"]

opcion = int(input("Elija su opcion: "))

if opcion == 1:
    opcionPlato = input("Que plato va agregar?: ")
    platos.append(opcionPlato)
    print("Platos: ", platos)
elif opcion == 2:
    opcionIndex = input("Que plato quiere buscar: ")
    index = platos.index(opcionIndex)
    print('Plato encontado: ', platos[index])
elif opcion == 3:
    opcionIndex = input("Que plato quiere eliminar: ")
    index = platos.index(opcionIndex)
    platos.pop(index)
    print("Platos actuales", platos)
elif opcion == 4:
    print("Platos en el menu", platos)
