sum = 0

print('Somador de números pares. Digite 6 números abaixo: ')

for element in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        sum += n

print(f'Total: {sum}')
