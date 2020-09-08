'''
--- Enunciado ---

Em um concurso de fantasias, os jurados precisam digitar os nomes dos 5 participantes e
suas respectivas notas, variando de 0 até 10. Crie uma função que leia os nomes dos
participantes e, ao final, apresente apenas o nome e a nota do vencedor.

Fluxo de exceção:

O programa deve verificar se a nota da pessoa é maior ou igual a zero e menor ou igual a dez.
'''

def calcula_notas_concurso(participantes):
    participantes = sorted(participantes, key=lambda participante: participante[1])

    vencedor = participantes[len(participantes) - 1]

    print(f"O(a) vencedor(a) foi {vencedor[0]} com nota {vencedor[1]}!")

participantes = []

for i in range(1, 6):
    # pergunta o nome do participante
    nome_participante = input(f"informe o nome do participante #{i}: ")

    if(not nome_participante):
        print(f"É necessário informar o nome do participante #{i}.")
        break

    nota_participante = input(f"informe a nota do participante #{i}: ")

    if(not nota_participante.replace(',', '').replace('.', '').isnumeric()):
        print(f"A nota informada para o participante #{i} é inválida.")
        break
    elif(float(nota_participante) <= 0 or float(nota_participante) > 10):
        print(f"A nota do participante #{i} deve ser entre zero e dez.")
        break

    participantes.append((nome_participante, float(nota_participante)))

# verifica se todos os participantes foram informados
if(len(participantes) == 5):
    calcula_notas_concurso(participantes)
