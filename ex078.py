lista = list()

for num in range(0, 5):
    n = int(input(f'Digite um número inteiro positivo para a posição {num}: '))
    lista.append(n)

print(f'Você digitou os valores: {lista}')

print(f'O maior valor digitado foi: {max(lista)}, \
nas posições: ', end='')

for index, number in enumerate(lista):
    if number == max(lista):
        print(f'{index}... ', end='')

print(f'O menor valor digitado foi: {min(lista)}, \
nas posições: ', end='')
for index, number in enumerate(lista):
    if number == min(lista):
        print(f'{index}... ', end='')
print('')
