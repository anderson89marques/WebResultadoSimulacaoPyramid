__author__ = 'anderson'
from distribuicoes.distribuicoes_simulacao import Distribuicao

class Questao04b():
    def __init__(self):
        pass

    def getquestao(self):
        dist = Distribuicao()
        resp = dist.poisson_analiticaB(3/3, 0, 0)
        return {'questao 04b' : "%.4f" % resp}