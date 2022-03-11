print('-=' * 40)

print('Dividindo valores em várias listas.')

print('-=' * 40)

numbers = list()
pars = list()
impars = list()

while True:
    num = int(input('Digite um número inteiro e positivo: '))
    numbers.append(num)
    go_on = str(input('Voce deseja continuar? [S/N] ')).strip().upper()
    if go_on in 'Nn':
        break

for num in numbers:
    if num % 2 == 0:
        pars.append(num)
    else:
        impars.append(num)

print(f'Lista digitada: {numbers}')
print(f'Lista de números pares: {pars}')
print(f'Lista de números ímpares: {impars}')
