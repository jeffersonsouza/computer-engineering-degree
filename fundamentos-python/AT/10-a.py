# Dentre os seguintes países nórdicos: Suécia, Dinamarca e Noruega,
# verifique: No século XXI (a partir de 2001), qual foi o maior
# medalhista de ouro, considerando apenas as seguintes modalidades:
#     - Curling
#     - Patinação no gelo (skating)
#     - Esqui (skiing)
#     - Hóquei sobre o gelo (ice hockey)
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/AT/

import pandas as pd

medalhas_olimpicas = pd.read_csv('https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv')

paises = ['NOR', 'SWE', 'FIN']

medalhas_olimpicas = medalhas_olimpicas.loc[
    (medalhas_olimpicas['NOC'] == 'NOR') |
    (medalhas_olimpicas['NOC'] == 'SWE') |
    (medalhas_olimpicas['NOC'] == 'FIN')
]

medalhas_olimpicas = medalhas_olimpicas.loc[(medalhas_olimpicas['Year'] > 2000) & (medalhas_olimpicas['Medal'] == 'Gold')]
medalhas_olimpicas = medalhas_olimpicas.loc[
    (medalhas_olimpicas['Sport'] == 'Skiing') |
    (medalhas_olimpicas['Sport'] == 'Curling') |
    (medalhas_olimpicas['Sport'] == 'Skating') |
    (medalhas_olimpicas['Sport'] == 'Ice Hockey')
]

medalhas_olimpicas = medalhas_olimpicas.groupby(['Medal']).count()

print(medalhas_olimpicas)
