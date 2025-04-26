import random
from laptop import Laptop

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, costo=500, impuesto=10, almacenamiento=100, duracion_bateria=8):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria

    def realizar_diagnostico_sistema(self):
        resultado_sistema = super().realizar_diagnostico_sistema()
        resultado_sistema.update({
            "ALMACENAMIENTO": "OK" if self.almacenamiento >= 500 else "Aumentar el almacenamiento",
            "DURACION_BATERIA": "OK" if self.duracion_bateria >= 8 else "Aumentar la duración de la batería"
        })
        return resultado_sistema
    def verificar_conectividad_red(self):
        resultado = {
            "WIFI": "OK " if random.choice([True, False]) else "No disponible",
            "ACCESO_SERVIDORES": "OK " if random.choice([True, False]) else "No disponible",
            "LATENCIA": "OK " if random.choice([True, False]) else "No disponible"
        }
        return resultado


laptop_empresarial = Laptop_Business('Asus', 'Intel Core i7', 16, 1000, 15, 500, 12)
print(laptop_empresarial.realizar_diagnostico_sistema())
print(laptop_empresarial.verificar_conectividad_red())