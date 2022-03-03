print('-=' * 40)

print('Lista com pares e ímpares.')

print('-=' * 40)

print('Digite 07 números abaixo:\n')

numbers = list()
pars = list()
impars = list()
for n in range(0, 7):
    num = int(input('Digite um número: '))

    if num % 2 == 0:
        pars.append(num)
    else:
        impars.append(num)

pars.sort()
impars.sort()
numbers.append(pars)
numbers.append(impars)

print('-' * 80)
print('')
print(f'A lista dos números digitados é: {numbers}')
print(f'A lista dos números pares digitados é: {numbers[0]}')
print(f'A lista dos números ímpares digitados é: {numbers[1]}')
