UNIDADES = { 0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: ' V', 6: 'VI', 7: 'V II', 8: 'VIII', 9: 'IX' }
DEZENAS = { 0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: ' LX', 7: 'LXX', 8: 'LXXX', 9: 'XC' }
CENTENAS = { 0: '', 1: 'C', 2: 'CC', 3: ' CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9:'CM' }

def converter_inteiro(numero):
    numero = int(numero)

    romano = []

    c = numero //100
    d = (numero - (c * 100)) //10
    u = (numero - (c * 100)) - (d * 10)

    return CENTENAS[c] + DEZENAS[d] + UNIDADES[u]

while True:
    data = input(f"Informe um número inteiro: ")
    data = int(data) if data.isnumeric() else False
    if data:
        break

print(converter_inteiro(data))
