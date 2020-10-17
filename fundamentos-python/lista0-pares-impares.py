numeros = {
    'pares': [],
    'impares': [],
}

for numero in range(10):
    data = input(f"Informe um número inteiro ({numero + 1}/10): ")
    n = int(data)
    if(n % 2 == 0):
        numeros['pares'].append(n)
        continue

    numeros['impares'].append(n)

print(f"Foram informados {len(numeros['pares'])} números pares e {len(numeros['impares'])} números ímpares")
