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
    @classmethod
    def create_toyota_new(cls):
        return cls("Toyota", "Corolla", 2022)

    @staticmethod
    def comparar_kilometraje(auto1, auto2):
        if(auto1.kilometraje == auto2.kilometraje):
          print("Tienen el mismo kilometraje")
        else:
          print("No tienen el mismo kilometraje")
        return;
    @staticmethod
    def mostrar_mayor_kilometraje(auto1, auto2):
        if(auto1.kilometraje > auto2.kilometraje):
            print(f"El auto 1 tiene más kilometraje: {auto1.kilometraje} km")
        else:
            print(f"El auto 2 tiene más kilometraje: {auto2.kilometraje} km")
        return;
    @classmethod
    def crear_auto_clasico(cls, marca, modelo):
        año = 2022 - 30
        return cls(marca, modelo, año)


# Crear auto toyota
auto_toyota = Auto.create_toyota_new()
print(auto_toyota.__dict__)

# Comparar kilometraje
auto1 = Auto.create_toyota_new()
auto2 = Auto("Mercedes", "Benz", 2023)
auto2.actualizar_kilometraje(1000)
Auto.comparar_kilometraje(auto1, auto2)

# Mostrar mayor kilometraje
Auto.mostrar_mayor_kilometraje(auto1, auto2)

# Crear auto clasico
auto_clasico = Auto.crear_auto_clasico("Toyota", "Corolla")

print(auto_clasico.__dict__)