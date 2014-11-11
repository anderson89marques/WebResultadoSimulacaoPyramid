__author__ = 'andersonmarques'
from distribuicoes.distribuicoes_simulacao import Distribuicao
class Questao02aSim():
    def __init__(self):
        pass

    def getquestao(self):
        experimentos = 10000
        cont = 0

        distri = Distribuicao()
        for i in range(experimentos):
            r = distri.geometrica_simuladaGeral(4, 0.3)
            if r == 4:
                cont += 1
        return {'questao 02a Simulada' : "%.4f" % (cont/experimentos)}