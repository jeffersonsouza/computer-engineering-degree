# Obtenha, usando requests ou urllib, a página HTML https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html
# dentro de seu programa em Python e faça:
#     a - Imprima o conteúdo referente apenas à tabela apresentada na página indicada.
#     b - Escreva um programa que obtenha do usuário uma sigla do estado da região
#     Centro-Oeste e apresenta suas informações correspondentes na tabela. O resultado
#     deve apresentar apenas o conteúdo, sem formatação. Ou seja, as tags não devem aparecer.
#     Não esqueça de checar se a sigla pertence à região.
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/AT/

import requests
from bs4 import BeautifulSoup

request = requests.get('https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html')
# a linha abaixo é para resolver o problema de encoding
request.encoding = request.apparent_encoding
bs = BeautifulSoup(request.text,"lxml")

tabela = bs.html.body.find('div', {'class': 'tabela'})

print(tabela.text)
