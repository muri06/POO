class Distancia:
    def __init__(self, km, h, m):
        self.km = km
        self.h = h
        self. m = m
    def calc_vmedia(self):
        self.h += self.m / 60
        return self.km / self.h
viagem = Distancia(50, 1, 30)
print(f'{viagem.calc_vmedia():.1f}')
