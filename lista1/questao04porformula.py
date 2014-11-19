__author__ = 'anderson'
from distribuicoes.distribuicoes_simulacao import Distribuicao
class Questao4Form():
    def __init__(self):
        pass

    def getquestao(self):
        distri = Distribuicao()

        r = distri.hipergeometrica(10, 3, 9, 4)
        #print("Probabilidade: %.4f" % (r))
        return {'questao 04 analítica' : "%.4f" % r}