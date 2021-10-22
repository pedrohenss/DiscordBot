from requests_html import HTMLSession

## Scraping Tabela Brasileirão

session = HTMLSession()
requisicao = session.get('https://www.goal.com/br/brasileir%C3%A3o-s%C3%A9rie-a/tabela-de-classifica%C3%A7%C3%A3o/scf9p4y91yjvqvg5jndxzhxj')

nome_times = requisicao.html.find('.widget-match-standings__team--full-name')
points = requisicao.html.find('.widget-match-standings__pts')
tabela = []

for item in range(0, 20):
    tabela.append(points[item + 1].text + ' - ' + nome_times[item].text + ' ' + '\n' )

tabela = (''.join(map(str,tabela)))
print(tabela)