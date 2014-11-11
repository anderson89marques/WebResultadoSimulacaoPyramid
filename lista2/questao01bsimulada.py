__author__ = 'andersonmarques'
from distribuicoes.distribuicoes_simulacao import Distribuicao
class Questao1bSim():
    def __init__(self):
        pass

    def getquestao(self):
        experimentos = 10000
        cont = 0

        distri = Distribuicao()
        for i in range(experimentos):
            resp = distri.binomial_simulada(5, 0.6)
            if resp >= 3:
                cont += 1
        return {'questao 01b simulada' : "%.4f" % (cont/experimentos)}