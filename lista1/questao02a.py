__author__ = 'anderson'
from random import randint

class Questao2a():
    def __init__(self):
        pass

    def getquestao(self):
        experimentos = 10000
        cont = 0

        for x in range(experimentos):
            dado1 = randint(1,6)
            dado2 = randint(1,6)
            if dado1 + dado2 >= 4:
                if (dado1 == 3 and dado2 != 3) or (dado2 == 3 and dado1 != 3):
                    cont += 1
                    print(dado1,dado2)

        #print("Probabilidade: %.4f" % (cont/experimentos))
        return {'questao 02a' : "%.4f" % (cont/experimentos)}