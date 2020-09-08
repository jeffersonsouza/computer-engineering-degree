'''
--- Enunciado ---

Ao usuário do programa serão solicitados o valor total do consumo,
em reais, o número total de pessoas e o percentual do serviço prestado, entre 0 e 100.

Fluxo de exceção:

O programa deve verificar se o número total de pessoas é maior do que zero.
O programa deve verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100.
Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro “Valor inválido” e
o programa deve ser interrompido.
 Dica: Em Python, o valor monetário calculado ao final pode ser informado, na função print(),
 usando vírgula como separador de casa decimal, em vez de pontos.
'''

def calcula_valor_total(valor_conta, taxa_servico = 0):
    valor_conta = float(valor_conta)
    taxa_servico = float(taxa_servico + '.0')
    valor_servico = float(taxa_servico) * valor_conta / 100

    return round(valor_conta + valor_servico, 2)

def calcula_valor_dividido(valor_conta, numero_pessoas):
    valor_conta = float(valor_conta)
    numero_pessoas = int(numero_pessoas)

    return round((valor_conta / numero_pessoas), 2)

while True:
    # Pergunta e valida o valor da conta
    valor_conta = input("Informe o valor total do consumo (ex.: 34,50): R$ ") or 0
    valor_conta = valor_conta.replace(',', '.')

    if(not valor_conta.replace(',', '').replace('.', '').isnumeric()):
        print("Valor inválido.")
        break
    elif(float(valor_conta) <= 0):
        print("Por favor, informe o valor total da conta.")
        break

    # Pergunta e valida numero de pessoas
    numero_pessoas = input("Informe o total de pessoas: ") or 0
    if(not numero_pessoas.isnumeric()):
        print("Valor inválido.")
        break
    elif(int(numero_pessoas) <= 0):
        print("Por favor, informe o número de pessoas que dividirão a conta.")
        break

    # Pergunta e valida a taxa de serviço
    taxa_servico = input("Informe o percentual do serviço, entre 0 e 100: ") or -1
    if(not taxa_servico.isnumeric()):
        print("Valor inválido.")
        break
    if(int(taxa_servico) <= 0 or int(taxa_servico) > 100):
        print("Por favor, o valor da taxa de serviço deve ser um valor em %, entre 0 e 100.")
        break

    valor_total = calcula_valor_total(valor_conta, taxa_servico)

    print(f"O valor total da conta, com a taxa de serviço, será de R$ {str(valor_total).replace('.', ',')}")
    print(f"Dividindo a conta por {numero_pessoas} pessoa(s), cada pessoa deverá pagar R$ {str(calcula_valor_dividido(valor_total, numero_pessoas)).replace('.', ',')}")
    break
