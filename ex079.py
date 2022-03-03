print('-=' * 40)

print('Valores únicos em uma lista.')

print('-=' * 40)

numbers = list()

while True:
    num = int(input('Digite um número inteiro e positivo inédito: '))
    if num not in numbers:
        numbers.append(num)
        print('Número adicionado com sucesso!')
    else:
        print('Número duplicado, não vou adicionar!')
    go_on = str(input('Voce deseja continuar? [S/N] ')).strip().upper()
    if go_on in 'Nn':
        break

numbers.sort()
print(f'Você digitou os valores: {numbers}')
