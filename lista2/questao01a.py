__author__ = 'andersonmarques'
from distribuicoes.distribuicoes_simulacao import Distribuicao
class Questao1a():
    def __init__(self):
        pass

    def getquestao(self):
        distri = Distribuicao()
        prob = distri.binomialA(3, 0.6, 2)

        return {'questao 01a' : "%.4f" % prob}
