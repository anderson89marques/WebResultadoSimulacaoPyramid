__author__ = 'anderson'
import random

class Questao1():
    def __init__(self):
        pass

    def getquestao(self):
        urna = ["vermelha","vermelha","vermelha","vermelha","vermelha","preta","preta"]
        EXPERIMENTOS = 10000
        CONT = 0.0

        for x in range(EXPERIMENTOS):
            ficha1,ficha2 = "",""
            cpy_urna = urna.copy()

            #escolhendo as fichas
            ficha1 = random.choice(cpy_urna)
            cpy_urna.remove(ficha1)
            ficha2 = random.choice(cpy_urna)
            #fim escolhendo fichas

            if ficha1 == ficha2:
                CONT += 1
        #print("Probabilidade: %.4f" % (CONT/EXPERIMENTOS))

        return {'questao 01' : "%.4f" % (CONT/EXPERIMENTOS)}
