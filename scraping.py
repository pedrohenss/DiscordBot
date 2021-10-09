from typing import List, Any
import pandas as pd
import numpy as np
from requests_html import HTMLSession

session = HTMLSession()

requisicao = session.get('https://www.meutimao.com.br/tabela-de-classificacao/campeonato_brasileiro/')

nome_times = requisicao.html.find('.nome-comum')
points = requisicao.html.find('.pg')
tabela = []

for item in range (0, 20):
    tabela.append(nome_times[item].text + ' ' + points[item].text + '\n' )

tabela = (''.join(map(str,tabela)))

print (tabela)


