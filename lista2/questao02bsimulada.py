__author__ = 'anderson'
from distribuicoes.distribuicoes_simulacao import Distribuicao
class Questao02bSim():
    def __init__(self):
        pass

    def getquestao(self):
        experimentos = 10000
        cont = 0
        dist = Distribuicao()

        for x in range(experimentos):
            r = dist.geometrica_simuladaGeral(5, 0.3)
            if r < 5:
                cont += 1

        return {'questao 02b Simulada' : "%.4f" % (cont/experimentos)}


