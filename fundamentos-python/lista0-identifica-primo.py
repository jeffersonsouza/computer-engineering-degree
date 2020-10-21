def isPrime(number):
    if number <= 1: return False
    if number == 2 or number == 3 or number == 5 or number == 7: return True
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        return False

    if number > 2:
        for n in range(2, number):
            if number % n == 0:
                return False
            else:
                return True

    return False

while True:
    data = input(f"Informe um número inteiro: ")
    data = int(data) if data.isnumeric() else False
    if data:
        break

print(f"O número {data} {'é' if isPrime(data) else 'não é'} primo")
