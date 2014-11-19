__author__ = 'anderson'
from distribuicoes.distribuicoes_simulacao import Distribuicao
class Questao04a():
    def __init__(self):
        pass

    def getquestao(self):
        dist = Distribuicao()
        resp = dist.poisson_analiticaB(3, 0, 2)
        return {'questao 04a' : "%.4f" % resp}