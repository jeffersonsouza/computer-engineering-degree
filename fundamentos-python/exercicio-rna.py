aminoacidos = {
    'UUU': 'Phe',
    'CUU': 'Leu',
    'UUA': 'Leu',
    'AAG': 'Lisina',
    'UCU': 'Ser',
    'UAU': 'Tyr',
    'CAA': 'Gln',
}

def traducao_rnaM(trinca):

    traducao = []

    for n in range(0, len(trinca), 3):
        traducao.append(aminoacidos[trinca[n:n + 3]])

    return '-'.join(traducao)

# 'UUU UUA UCU'
print(traducao_rnaM('UUUUUAUCU'))
