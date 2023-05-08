import math
class Circulo:
  def __init__(self):
    self.raio = 0
  def calc_area(self):
    return math.pi * self.raio ** 2

x = Circulo()
x.raio = float(input())
print(x.calc_area())
