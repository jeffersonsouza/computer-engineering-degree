# Dentre os seguintes países nórdicos: Suécia, Dinamarca e Noruega,
# verifique: No século XXI (a partir de 2001), qual foi o maior
# medalhista de ouro, considerando apenas as seguintes modalidades:
#     - Curling
#     - Patinação no gelo (skating)
#     - Esqui (skiing)
#     - Hóquei sobre o gelo (ice hockey)
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/AT/

import requests, re
from collections import Counter
from bs4 import BeautifulSoup

request = requests.get('http://brasil.pyladies.com/about')
# a linha abaixo é para resolver o problema de encoding
request.encoding = request.apparent_encoding
bs = BeautifulSoup(request.text,"lxml")

total_ladies = 0
total_palavras = 0
palavras = []

for elemento in bs.html.body.article.find_all('div'):
    total_ladies += elemento.text.lower().count('ladies')
    for palavra in elemento.text.split():
        palavra = re.sub('\W+', '', palavra)
        palavras.append(palavra.lower())

total_palavras = len(palavras)
palavras_dict = dict(Counter(palavras))

print('Total de palavras no corpo da página:', total_palavras)

for palavra, counter in palavras_dict.items():
    if(counter == 1):
        print(f"A palavra '{palavra}' foi apareceu somente uma vez na página")

print("\n", 'Total de vezes que a palavra "ladies" apareceu na página:', total_ladies)
