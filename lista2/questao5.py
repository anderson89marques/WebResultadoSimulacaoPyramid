__author__ = 'anderson'
from distribuicoes.distribuicoes_simulacao import Distribuicao

class Questao05():
    def __init__(self):
        pass

    def getquestao(self):
        dist = Distribuicao()
        resp = 0
        n = 100
        M = 10
        for x in range(6, 10):
            resp += dist.hipergeometrica(M, x, n-M, M-x)
        return {'questao 05' : "%.4f" % resp}