# Obtenha, usando requests ou urllib, dentro de seu programa em Python, o csv do link:
# https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv
# Obtenha, dentre os jogos do gênero de ação (Action), tiro (Shooter) e plataforma (Platform):
#   - Quais são as três marcas que mais publicaram jogos dos três gêneros combinados? Indique também o total de jogos de cada marca.
#   - Quais são as três marcas que mais venderam os três gêneros combinados? Indique também o total de vendas de cada marca.
#   - Qual é a marca com mais publicações em cada um dos gêneros nos últimos dez anos no Japão? Indique também o número total de jogos dela.
#   - Qual foi a marca que mais vendeu em cada um desses gêneros nos últimos dez anos, no Japão? Indique também o total de vendas dela.
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/AT/

import pandas as pd

generos = ['Action', 'Shooter', 'Platform']

jogos = pd.read_csv('https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv')
jogos = jogos.query("Genre in @generos")

# Questão A
publicacoes = jogos.groupby(['Publisher'], as_index=False)['User_Score']\
    .count()

publicacoes = publicacoes.sort_values(by=['User_Score'], ascending=False).iloc[0:3]
publicacoes = publicacoes.rename(columns={'User_Score': 'Releases'})

print('###########################################################')
print('Questão A - As marcas abaixo são o Top 3 de lançamentos:')
print('###########################################################')

for index, row in publicacoes.iterrows():
    print(f"A produtora {row['Publisher']} está no top de publicações com {row['Releases']} jogos publicados.")

# Questão B
print("\n", '###########################################################')
print('Questão B - As marcas abaixo são as que mais venderam no mundo todo:')
print('###########################################################')
vendas_globais = jogos.groupby(['Publisher'], as_index=False)['Global_Sales'].sum()
vendas_globais = vendas_globais.sort_values(by=['Global_Sales'], ascending=False).iloc[0:3]

for index, row in vendas_globais.iterrows():
    print(f"A produtora {row['Publisher']} está no top de vendas globais com {round(row['Global_Sales'], 2)} em vendas.")

# Questão C
print("\n", '###########################################################')
print('Questão C - As marcas abaixo são as que mais lançaram jogos no japão na última década:')
print('###########################################################')
jogos_jp = jogos.query("JP_Sales > 0 and Year_of_Release >= 2010")
publicacoes_jp = jogos_jp.groupby(['Genre', 'Publisher'], as_index=False)['User_Score'].count()
publicacoes_jp = publicacoes_jp.sort_values(by=['User_Score'], ascending=False)
publicacoes_jp = publicacoes_jp.rename(columns={'User_Score': 'Releases'})
for genre in generos:
    item = publicacoes_jp.query("Genre == @genre").iloc[0]
    print(f"A produtora {item['Publisher']} publicou {item['Releases']} jogos do genero '{item['Genre']}' nos últimos 10 anos")

# Questão D
print("\n", '###########################################################')
print('Questão D - As marcas abaixo são as que mais venderam jogos no japão na última década:')
print('###########################################################')
vendas_jp = jogos_jp.groupby(['Genre', 'Publisher'], as_index=False)['JP_Sales'].sum()
vendas_jp = vendas_jp.sort_values(by=['JP_Sales'], ascending=False)

for genre in generos:
    item = vendas_jp.query("Genre == @genre").iloc[0]
    print(f"A produtora {item['Publisher']} vendeu {round(item['JP_Sales'], 2)} em jogos do genero '{item['Genre']}' nos últimos 10 anos")
