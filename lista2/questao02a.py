__author__ = 'andersonmarques'
from distribuicoes.distribuicoes_simulacao import Distribuicao
class Questao02a():
    def __init__(self):
        pass

    def getquestao(self):
        distri = Distribuicao()
        prob = distri.geometrica(4, 0.3)
        return {'questao 02a' : "%.4f" % prob}
