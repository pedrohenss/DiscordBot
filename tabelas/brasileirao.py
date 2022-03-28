from requests_html import HTMLSession

## Scraping Tabela Brasileirão

session = HTMLSession()
requisicao = session.get('https://www.eurosport.com/football/brazilian-serie-a/standing.shtml')

nome_times = requisicao.html.find('.text')
points = requisicao.html.find('.standing-table__cell-value--main')
tabela = []

for item in range(0, 20):
    tabela.append(points[item].text + ' - ' + nome_times[item].text + ' ' + '\n' )

tabela = (''.join(map(str,tabela)))
print(tabela)
