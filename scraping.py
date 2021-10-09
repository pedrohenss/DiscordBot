from typing import List, Any
import pandas as pd
import numpy as np
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from selenium import webdriver
import time


## Comando Tabela Brasileirão

session = HTMLSession()
requisicao = session.get('https://www.meutimao.com.br/tabela-de-classificacao/campeonato_brasileiro/')

nome_times = requisicao.html.find('.nome-comum')
points = requisicao.html.find('.pg')
tabela = []

for item in range (0, 20):
    tabela.append(nome_times[item].text + ' - ' + points[item].text + ' ' + '\n' )
tabela = (''.join(map(str,tabela)))


## Comandos

driver = webdriver.Firefox()

driver.get ('https://www.flashscore.com.br')

time.sleep(5)

tab_aovivo = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[1]/div[2]/div[5]/div/div[1]/div[1]/div[2]')
tab_aovivo.click()

div_mae = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[1]/div[2]/div[5]/div/section/div/div')

html_content = div_mae.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')


#event__participant--home
#event__participant--away
#event__score--home
#event__score--away

home_teams = soup.find_all ('div', class_='event__participant--home')
away_teams = soup.find_all ('div', class_='event__participant--away')
home_score = soup.find_all ('div', class_='event__score--home')
away_score = soup.find_all ('div', class_='event__score--away')

tamanho_lista = len(home_teams)
indice = 0

for item in range (tamanho_lista):
    print(home_teams[indice].get_text(), ' ', home_score[indice].get_text(), 'x', away_score[indice].get_text(), ' ', away_teams[indice].get_text())
    indice += 1
