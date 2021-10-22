from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

## Scraping de Jogos ao Vivo

options = Options()
options.add_argument('--headless')

driver = webdriver.Firefox(options=options)

driver.get('https://www.flashscore.com.br')

time.sleep(5)

tab_aovivo = driver.find_element_by_css_selector('div.tabs__tab:nth-child(2)')
tab_aovivo.click()
div_mae = driver.find_element_by_xpath('//*[@id="live-table"]')
html_content = div_mae.get_attribute('outerHTML')
soup = BeautifulSoup(html_content, 'html.parser')


home_teams = soup.find_all ('div', class_='event__participant--home')
away_teams = soup.find_all ('div', class_='event__participant--away')
home_score = soup.find_all ('div', class_='event__score--home')
away_score = soup.find_all ('div', class_='event__score--away')

jogos_ao_vivo = []
tamanho_lista = len(home_teams)

for item in range(tamanho_lista):
    jogos_ao_vivo.append(home_teams[item].get_text() + ' ' + home_score[item].get_text() + ' x ' + away_score[item].get_text() + ' ' + away_teams[item].get_text() + ' ' + '\n' )

jogos_ao_vivo = (''.join(map(str,jogos_ao_vivo)))    
print(jogos_ao_vivo) 

