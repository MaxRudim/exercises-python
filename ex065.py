print('-=' * 40)

print('Maior e menor valores.')

print('-=' * 40)

numbers = list()
go_on = 'S'

while go_on != 'N':
    num = int(input('Digite um número inteiro positivo: '))
    numbers.append(num)
    go_on = str(input('Voce deseja continuar? [S/N] ')).strip().upper()

print(f'A média dos números foi: {sum(numbers) / len(numbers)}')
print(f'O maior número foi: {max(numbers)} e o menor foi: {min(numbers)}')
