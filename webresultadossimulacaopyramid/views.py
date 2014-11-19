from pyramid.view import view_config
from lista1.questao01 import *
from lista1.questao02a import *
from lista1.questao02b import *
from lista1.questao03 import *
from lista1.questao04porformula import *
from lista1.questao04simulada import *
from lista1.questao05 import *
from lista1.questao06 import *
from lista1.questao07 import *
from lista1.questao08 import *
from lista1.questao09 import *
from lista1.questao10 import *

from lista2.questao01a import *
from lista2.questao01asimulada import *
from lista2.questao01b import *
from lista2.questao01bsimulada import *
from lista2.questao02a import *
from lista2.questao02asimulada import *
from lista2.questao02b import *
from lista2.questao02bsimulada import *
from lista2.questao03 import *
from lista2.questao04a import *
from lista2.questao4abin import *
from lista2.questao4b import *
from lista2.questao4bbin import *
from lista2.questao5 import *
from lista2.questao06a import *
from lista2.questao06b import *
from lista2.questao07 import *

#@view_config(route_name='home', renderer='templates/mytemplate.pt')
#não está sendo usada
def my_view(request):
    return {'project': 'WebResultadosSimulacaoPyramid'}

class SimulacaoViews:
    def __init__(self,request):
        self.request = request

    @view_config(route_name='home', renderer='templates/home.pt')
    def home(self):
        return {"nome" : 'ok'}

    @view_config(route_name='teste', renderer='templates/teste.pt')
    def meu_teste(self):
        return {'nome' : 'Anderson'}


    @view_config(route_name='ajaxteste', renderer='json')
    def resposta_ajax(self):
        print(self.request.params['nome'])

        r = self.gerar_lista(self.request.params['nome'])
        return {'lista': r}

    def gerar_lista(self, nome_lista):
        d = {'lista 1': {1:Questao1, 2:Questao2a, 3:Questao2b, 4:Questao3, 5:Questao4Form, 6:Questao4Sim, 7:Questao5,
             8:Questao6, 9:Questao7, 10:Questao8, 11:Questao9, 12: Questao10},

             'lista 2' : {1:Questao1a, 2:Questao1aSim, 3:Questao1b, 4:Questao1bSim, 5:Questao02a, 6:Questao02aSim, 7:Questao02b,
             8:Questao02bSim, 9:Questao03, 10: Questao04a, 11: Questao04aBin, 12: Questao04b, 13: Questao04bBin, 14: Questao05,
             15: Questao06a, 16: Questao06b, 17: Questao7},

             'lista Final' : {1:Questao1a, 2:Questao2a, 3:Questao1, 4:Questao2b, 5:Questao1bSim, 6:Questao4Sim, 7:Questao5,
             8:Questao6, 9:Questao7}}

        op = d[nome_lista]
        r = []

        for x, y in op.items():
            q = y()
            r.append(q.getquestao())
        return r