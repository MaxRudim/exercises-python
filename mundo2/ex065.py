print('-=' * 40)

print('Maior e menor valores.')

print('-=' * 40)

numbers = list()

while True:
    num = int(input('Digite um número inteiro positivo: '))
    numbers.append(num)
    go_on = str(input('Voce deseja continuar? [S/N] ')).strip().upper()
    if go_on in 'Nn':
        break

print(f'A média dos números foi: {sum(numbers) / len(numbers)}')
print(f'O maior número foi: {max(numbers)} e o menor foi: {min(numbers)}')
