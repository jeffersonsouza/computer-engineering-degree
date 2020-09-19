'''
--- Enunciado ---

Desenvolva uma função que recebe a idade de uma pessoa e informe se essa pessoa é:

Eleitor obrigatório (18 anos completos e menos de 70 anos de idade)
Eleitor facultativo (16 anos completos e menos de 18 anos ou 70 anos de idade ou mais).
Não tem direito a voto (menor de 16 anos).

Fluxo de exceção:
    - O programa deve verificar se a idade da pessoa é maior do que zero.

https://github.com/jeffersonsouza/computer-engineering-degree/blob/master/introducao-logica/TP3/02-idade-eleitoral.py
'''

def valida_situacao_eleitoral(idade):
    idade = int(idade)
    situacao_eleitoral = ''

    if(idade < 16):
        situacao_eleitoral = 'não tem direito a voto'
    elif(idade >= 18 and idade < 70):
        situacao_eleitoral = 'é eleitor obrigatório'
    else:
        situacao_eleitoral = 'é eleitor facultativo'

    return situacao_eleitoral

while True:
    # Pergunta e valida a idade
    idade = input("Informe a idade do cidadão: ")

    if(not idade.isnumeric() or int(idade) <= 0):
        print("Idade inválida.")
    else:
        print(f"O eleitor tem {int(idade)} ano(s), por isso {valida_situacao_eleitoral(idade)}.")
        break
