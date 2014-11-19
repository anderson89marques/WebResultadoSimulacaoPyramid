__author__ = 'andersonmarques'
from distribuicoes.distribuicoes_simulacao import Distribuicao
class Questao02b():
    def __init__(self):
        pass

    def getquestao(self):
        distri = Distribuicao()
        prob = distri.geometricaB(5, 0.3)
        return {'questao 02b' : "%.4f" % prob}
