import random


class Laptop:
    def __init__(self, marca, procesador, memoria, costo = 500, impuesto = 10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto

    def valor_final():
        return self.costo + self.impuesto
    def realizar_diagnostico_sistema(self):
        resultado = {
            "MARCA": f"{self.marca}",
            "PROCESADOR": f"{self.procesador}",
            "MEMORIA": "OK" if self.memoria >= 8 else "Aumetar la ram",
            "BATERIA": "OK" if random.choice([True, False]) else "Cambiar bateria",
        }
        return resultado