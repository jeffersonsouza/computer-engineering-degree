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

paises = ['NOR', 'SWE', 'FIN']
modalidades = ['Skiing', 'Curling', 'Skating', 'Ice Hockey']

medalhas_olimpicas = pd.read_csv('https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv')
medalhas_olimpicas = medalhas_olimpicas\
    .query("NOC in @paises and Sport in @modalidades and Year > 2000 and Medal == 'Gold'")\
    .groupby(['NOC'], as_index=False)\
    .count()

medalhista = medalhas_olimpicas.sort_values(by=['Medal'], ascending=False).iloc[0]

print(f"O maior medalhista de ouro do século 21 nas modalidades Skiing, Curling, Skating, Ice Hockey foi: {medalhista['NOC']} com {medalhista['Medal']} medalhas")
