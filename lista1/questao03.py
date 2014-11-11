__author__ = 'anderson'
from distribuicoes.distribuicoes_simulacao import Distribuicao
class Questao3():
    def __init__(self):
        pass

    def getquestao(self):
        distri = Distribuicao()

        r = distri.combinacao(10, 3) * distri.combinacao(9, 4)
        #print("Probabilidade: %.4f" % (r))
        return {'questao 03' : "%.4f" % r}
