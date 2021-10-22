from requests_html import HTMLSession

## Scraping Tabela Ligue 1

session = HTMLSession()
requisicao = session.get('https://www.goal.com/br/ligue-1/tabela-de-classifica%C3%A7%C3%A3o/dm5ka0os1e3dxcp3vh05kmp33')

nome_times = requisicao.html.find('.widget-match-standings__team--full-name')
points = requisicao.html.find('.widget-match-standings__pts')
tabela = []

for item in range(0, 20):
    tabela.append(points[item + 1].text + ' - ' + nome_times[item].text + ' ' + '\n' )

tabela = (''.join(map(str,tabela)))
print(tabela)