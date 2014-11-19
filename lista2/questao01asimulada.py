__author__ = 'andersonmarques'
from distribuicoes.distribuicoes_simulacao import Distribuicao

class Questao1aSim():
    def __init__(self):
        pass

    def getquestao(self):
        experimentos = 10000
        cont = 0

        distri = Distribuicao()
        for i in range(experimentos):
            resp = distri.binomial_simulada(3, 0.6)
            if resp == 2:
                cont += 1

        return {'questao 01a simulada' : "%.4f" % (cont/experimentos)}