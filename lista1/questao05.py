__author__ = 'anderson'
import random
class Questao5():
    def __init__(self):
        pass

    def getquestao(self):
        urna0 = ["v", "v", "p"] #urna 1
        urna1 = ["v", "v", "v", "v", "v", "p", "p"] #urna 2
        urna2 = ["p", "p", "p", "p", "p", "v"] #urna 3
        urnas = [urna0, urna1, urna2]
        experimentos = 10000
        cont = 0

        for x in range(experimentos):
            r = random.randint(0, 2)

            #pegando a urna
            urna = urnas[r]
            cor = random.choice(urna)
            if cor == "v" and r == 2:
                cont += 1

        #print("Probabilidade: %.4f" % (cont/experimentos))
        return {'questao 05' : "%.4f" % (cont/experimentos)}