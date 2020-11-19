from collections import namedtuple

# Escreva um programa em Python que leia nomes de alunos e suas alturas em metros
# até que um nome de aluno seja o código de saída “Sair”. O programa deve possuir uma
# função que indica todos os alunos que tenham altura acima da média (a média
# aritmética das alturas de todos os alunos lidos).
#
# Também disponível em https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/fundamentos-python/TP3/

Aluno = namedtuple('Aluno', ['nome', 'altura'])
alunos = []

campos = [
    {'label': 'Informe o nome do aluno:', 'valor': 0},
    {'label': 'Informe a altura do aluno (em centimetros):', 'valor': 0},
]

def calcula_media(alunos):
    somatorio = 0

    for aluno in alunos:
        somatorio += int(aluno.altura)

    return int(somatorio // len(alunos))

def filtra_alunos_por_altura_media(alunos):
    media = calcula_media(alunos)

    alunos_acima_media = []

    for aluno in alunos:
        if int(aluno.altura) > media:
            alunos_acima_media.append(aluno.nome)

    return [media, alunos_acima_media]

executando = True
while executando:
    aluno = []
    for index, campo in enumerate(campos):
        if not executando: continue

        while True:
            campo['valor'] = input(f"{campo['label']} ") or ''

            if index == 0 and campo['valor'] == 'sair':
                executando = False
                break

            if not campo['valor']:
                print("O valor informado é inválido.")
            elif index == 1 and not campo['valor'].isnumeric():
                print("O valor informado é inválido.")
            else:
                aluno.append(campo['valor'])
                break
    if len(aluno) == 2:
        # adiciona os dados captados no array de alunos
        alunos.append(Aluno(nome=aluno[0], altura=aluno[1]))

# calcula o resultado
resultado = filtra_alunos_por_altura_media(alunos)

print(f"Os alunos abaixo estão acima da média de {resultado[0]}cm")
print("\n".join(resultado[1]))
