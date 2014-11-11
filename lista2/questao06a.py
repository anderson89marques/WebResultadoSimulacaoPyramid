__author__ = 'anderson'
from  random import random

class Questao06a():
    def __init__(self):
        pass

    def getquestao(self):
        experimentos = 100000
        cont = 0
        pPecaA = 1/1000
        pPecaB = 1/500
        pPecaC = 1/200

        for x in range(experimentos):#lotes
            for i in range(100):#embalagens
                if random() <= pPecaA or random() <= pPecaB or random() <= pPecaC:
                    cont += 1
                    break

        return {'questao 06a' : "%.4f" % (cont/experimentos)}
