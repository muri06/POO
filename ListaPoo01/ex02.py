class Disciplinas:
    def __init__(self, nome, n1, n2, n3, n4, nf):
        self.nome = nome
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.nf = nf
        self.media = ''
        
    def calc_media(self):
        
        self.media = (self.n1 * 2 + self.n2 * 2 + self.n3 * 3 + self.n4 * 3) / 10
        if self.media > 60:
            self.media = (self.media + self.nf) / 2
        return self.media

aluno1 = Disciplinas('POO', 100, 80, 80, 100, 60)

print(aluno1.calc_media())
