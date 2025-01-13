Este programa calcula el área de diferentes figuras geométricas:
* Cuadrado
* Rectángulo
* Círculo
"""

import math

class FiguraGeometrica:
    def calcular_area(self):
        pass  # Método abstracto, será implementado en las subclases

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

# Ejemplo de uso
cuadrado1 = Cuadrado(5)
rectangulo1 = Rectangulo(4, 6)
circulo1 = Circulo(3)

print("Área del cuadrado:", cuadrado1.calcular_area())
print("Área del rectángulo:", rectangulo1.calcular_area())
print("Área del círculo:", circulo1.calcular_area())
