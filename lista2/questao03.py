__author__ = 'anderson'
from random import randint

class Questao03():
    def __init__(self):
        pass

    def getquestao(self):
        experimentos = 10000
        cont = 0

        for x in range(experimentos):
            dado1 = randint(1, 6)
            dado2 = randint(1, 6)
            if dado1 + dado2 > 6:
                if dado1 == 5 or dado2 == 5:
                    cont += 1
        return {'questao 03' : "%.4f" % (cont/experimentos)}
