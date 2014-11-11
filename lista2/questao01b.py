__author__ = 'andersonmarques'
from distribuicoes.distribuicoes_simulacao import Distribuicao
class Questao1b():
    def __init__(self):
        pass

    def getquestao(self):
        distri = Distribuicao()
        prob = distri.binomialB(5, 0.6, 3)

        return {'questao 01b' : "%.4f" % prob}
