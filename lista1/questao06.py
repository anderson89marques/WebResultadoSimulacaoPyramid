__author__ = 'andersonmarques'
import random
class Questao6():
    def __init__(self):
        pass

    def getquestao(self):
        experimentos = 10000
        cont = 0

        for i in range(experimentos):
            x = random.randint(0,4)
            f = x**3
            if f >= 1 and f <= 20:
                cont += 1

        #print("Probabilidade: %.4f" % (cont/experimentos))
        return {'questao 06' : "%.4f" % (cont/experimentos)}