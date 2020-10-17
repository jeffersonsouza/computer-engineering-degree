grupos = [0, 0, 0, 0]

while True:
    data = input('Informe um número: ')
    data = int(data) if not data.isalpha() else 999

    if data < 0:
        print(f"Temos {grupos[0]} números entre 0 e 25")
        print(f"Temos {grupos[1]} números entre 26 e 50")
        print(f"Temos {grupos[2]} números entre 51 e 75")
        print(f"Temos {grupos[3]} números entre 76 e 100")
        break
    elif data >= 0 and data <= 25:
        grupos[0] += 1
    elif data <= 50:
        grupos[1] += 1
    elif data <= 75:
        grupos[2] += 1
    elif data <= 100:
        grupos[3] += 1
