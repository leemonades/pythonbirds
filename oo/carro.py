class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def freiar(self):
        if self.velocidade == 1:
            self.velocidade = 0
        elif self.velocidade >= 2:
            self.velocidade -= 2

class Direcao:
    def __init__(self):
        self.valor = 'Norte'

    def girar_a_direita(self):
        if self.valor == 'Norte':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Norte'



    def girar_a_esquerda(self):
        if self.valor == 'Norte':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Norte'

class Carro:

    def __init__(self,motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        print(self.motor.velocidade)

    def acelerar(self):
        self.motor.acelerar()

    def freiar(self):
        self.motor.freiar()

    def calcular_direcao(self):
        print(self.direcao.valor)


    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

if __name__=='__main__':

    motor = Motor()
    direcao = Direcao()
    carro = Carro(motor, direcao)
    carro.calcular_direcao()
    carro.girar_a_direita()
    carro.calcular_direcao()
    carro.girar_a_direita()
    carro.calcular_direcao()
    carro.calcular_velocidade()
    carro.acelerar()
    carro.acelerar()
    carro.acelerar()
    carro.calcular_velocidade()
    carro.girar_a_esquerda()
    carro.calcular_direcao()
    carro.freiar()
    carro.calcular_velocidade()