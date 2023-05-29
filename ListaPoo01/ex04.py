class Sessao:

    def __init__(self):
        self.dia = 0
        self.horario = 0
        self.inteiro = 0
        self.meia = 0

    def criar_sessao(self):
        self.dia = input('Dia da semana da sessão: ')
        self.horario = int(input('Horário da sessão: '))

    def calc_ingresso(self):

        if self.dia == 'segunda' or self.dia == 'terça' or self.dia == 'quinta':
            self.inteiro = 16
            self.meia = self.inteiro/2
            if 17 <= self.horario >= 0:
                self.inteiro += self.inteiro * 0.5
                self.meia += self.inteiro * 0.5

            elif self.dia == 'quarta':
                self.meia = 8
                self.inteiro = self.meia

            elif self.dia == 'sexta' or self.dia == 'sabado' or self.dia == 'domingo':
                self.inteiro = 20
                self.meia = self.inteiro / 2
                if 17 <= self.horario >= 0:
                    self.inteiro += self.inteiro * 0.5
                    self.meia += self.inteiro * 0.5
            return [self.inteiro, self.meia]

sessao = Sessao()
sessao.criar_sessao()
valores_ingresso = sessao.calc_ingresso()
print(f'Valor do ingresso inteiro: {valores_ingresso[0]}')
print(f'Valor da meia: {valores_ingresso[1]}')
