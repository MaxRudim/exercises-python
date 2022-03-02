print('-=' * 40)

print('Extraindo dados de uma lista.')

print('-=' * 40)

numbers = list()
go_on = 'S'

while go_on != 'N':
    num = int(input('Digite um número inteiro e positivo: '))
    numbers.append(num)
    go_on = str(input('Voce deseja continuar? [S/N] ')).strip().upper()

print('\n')
print('-' * 40)
print(f'Você digitou a lista: {numbers}')

print(f'Esta lista contém: {len(numbers)} elementos.')

numbers.sort(reverse=True)

print(f'Em ordem decrescente, esta lista é: {numbers}')

if 5 in numbers:
    print('O número 5 ESTÁ na lista.')
else:
    print('O número 5 NÃO ESTÁ na lista.')
