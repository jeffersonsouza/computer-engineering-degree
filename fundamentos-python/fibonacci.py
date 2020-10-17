fibbonacci = []

previous = 0
current = 1

fibbonacci.append(previous)
fibbonacci.append(current)

for number in range(2, 100):
    next = previous + current

    fibbonacci.append(next)

    previous = current
    current = next


print(fibbonacci)
