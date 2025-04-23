# Crear clase de auto
class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = 0
    
    def mostrar_información(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
    
    def actualizar_kilometraje(self, kilometraje):
        if kilometraje >= self.kilometraje:
            self.kilometraje = kilometraje
        else:
            print("El kilometraje no puede ser menor.")
    
    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
        else:
            print("La cantidad de kilómetros debe ser positiva.")
    
    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo")
        elif self.kilometraje <= 100000:
            print("Ya estoy usado")
        else:
            print("¡Ya déjame descansar por favor!")

# Crear un auto
mi_auto = Auto("Toyota", "Corolla", 2022)

# Mostrar información inicial
print("Información inicial del auto-----------:")
mi_auto.mostrar_información()
print(f"Kilometraje actual: {mi_auto.kilometraje} km")

# Verificar estado inicial
print("Estado inicial del auto-----------:")
mi_auto.estado_auto()

# Actualizar kilometraje
print("Actualizando kilometraje a 15000 km-----------:")
mi_auto.actualizar_kilometraje(15000)
print(f"Kilometraje actualizado: {mi_auto.kilometraje} km")
mi_auto.estado_auto()

# Intentar reducir el kilometraje
print("Intentando reducir el kilometraje a 10000 km-----------:")
mi_auto.actualizar_kilometraje(10000)
print(f"Kilometraje actual: {mi_auto.kilometraje} km")

# Realizar un viaje
print("Realizando un viaje de 10000 km-----------:")
mi_auto.realizar_viaje(10000)
print(f"Kilometraje después del viaje: {mi_auto.kilometraje} km")
mi_auto.estado_auto()

# Intentar realizar un viaje con kilómetros negativos
print("Intentando realizar un viaje con -5000 km------------:")
mi_auto.realizar_viaje(-5000)
print(f"Kilometraje actual: {mi_auto.kilometraje} km")

# Realizar otro viaje para superar los 100000 km
print("Realizando un viaje de 80000 km-----------:")
mi_auto.realizar_viaje(80000)
print(f"Kilometraje después del viaje: {mi_auto.kilometraje} km")
mi_auto.estado_auto()